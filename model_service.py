import io
import os
import logging
import numpy as np
from PIL import Image
import keras
from keras import layers, models

from config import (
    MODEL_PATH,
    IMAGE_SIZE,
    INPUT_SHAPE,
    RESCALE_FACTOR,
    CLASS_NAMES,
    CLASS_ORDER_MODE,
    SYLLABUS_CLASSES,
    ALPHABETICAL_CLASSES
)
from skincare_data import SKINCARE_GUIDE, GENERAL_SKINCARE_PRINCIPLES, DISCLAIMER_TEXT

logger = logging.getLogger(__name__)

class AcneModelService:
    def __init__(self, model_path=MODEL_PATH):
        self.model_path = model_path
        self.model = None
        self.classes = CLASS_NAMES
        self.input_shape = INPUT_SHAPE
        self.load_model()

    def _build_architecture(self):
        """
        Recreates the exact sequential CNN architecture as saved in config.json.
        Serves as a reliable fallback for cross-version Keras compatibility.
        """
        model = models.Sequential([
            layers.Input(shape=self.input_shape, name="input_layer"),
            layers.RandomFlip("horizontal", name="random_flip"),
            layers.RandomRotation(0.1, name="random_rotation"),
            layers.RandomZoom(0.1, name="random_zoom"),
            layers.Conv2D(32, (3, 3), activation="relu", name="conv2d"),
            layers.MaxPooling2D((2, 2), name="max_pooling2d"),
            layers.Conv2D(64, (3, 3), activation="relu", name="conv2d_1"),
            layers.MaxPooling2D((2, 2), name="max_pooling2d_1"),
            layers.Conv2D(128, (3, 3), activation="relu", name="conv2d_2"),
            layers.MaxPooling2D((2, 2), name="max_pooling2d_2"),
            layers.Conv2D(128, (3, 3), activation="relu", name="conv2d_3"),
            layers.MaxPooling2D((2, 2), name="max_pooling2d_3"),
            layers.Flatten(name="flatten"),
            layers.Dense(128, activation="relu", name="dense"),
            layers.Dropout(0.5, name="dropout"),
            layers.Dense(5, activation="softmax", name="dense_1")
        ], name="sequential")
        return model

    def load_model(self):
        """
        Loads the trained model from acne_cnn_model.keras.
        First tries standard keras.models.load_model.
        If a deserialization or version mismatch occurs, loads weights into rebuilt architecture.
        """
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model file not found at: {self.model_path}")

        logger.info(f"Loading model from {self.model_path}...")
        try:
            self.model = keras.models.load_model(self.model_path)
            logger.info("Successfully loaded model via keras.models.load_model.")
        except Exception as e:
            logger.warning(f"Standard load_model encountered: {e}. Falling back to architecture + weight loading...")
            self.model = self._build_architecture()
            self.model.load_weights(self.model_path)
            logger.info("Successfully loaded model weights into reconstructed architecture.")

        # Warm up model with a dummy prediction
        try:
            dummy_input = np.zeros((1, *self.input_shape), dtype=np.float32)
            self.model.predict(dummy_input, verbose=0)
            logger.info("Model warmup prediction completed successfully.")
        except Exception as e:
            logger.error(f"Error during model warmup: {e}")

    def preprocess_image(self, image_bytes):
        """
        Preprocesses raw image bytes to match model input requirements:
        1. Open with PIL and convert to RGB
        2. Resize to (128, 128)
        3. Convert to float32 NumPy array
        4. Normalize pixel values to [0.0, 1.0] by dividing by 255.0
        5. Add batch dimension -> (1, 128, 128, 3)
        """
        try:
            image = Image.open(io.BytesIO(image_bytes))
        except Exception as e:
            raise ValueError(f"Invalid image file: {str(e)}")

        original_size = image.size  # (width, height)
        original_format = image.format or "Unknown"

        # Convert to RGB (handles RGBA, Grayscale, etc.)
        if image.mode != "RGB":
            image = image.convert("RGB")

        # Resize to 128x128 using high quality Lanczos resampling
        resized_image = image.resize(IMAGE_SIZE, Image.Resampling.LANCZOS)

        # Convert to NumPy array
        img_array = np.array(resized_image, dtype=np.float32)

        # Normalize to [0, 1]
        img_array = img_array * RESCALE_FACTOR

        # Expand dims for batch: (1, 128, 128, 3)
        tensor = np.expand_dims(img_array, axis=0)

        metadata = {
            "original_width": original_size[0],
            "original_height": original_size[1],
            "original_format": original_format,
            "target_dimensions": f"{IMAGE_SIZE[0]}x{IMAGE_SIZE[1]}",
            "channels": 3,
            "rescaling": "1 / 255.0 (0.0 to 1.0)",
            "tensor_shape": list(tensor.shape)
        }

        return tensor, metadata

    def predict(self, image_bytes, class_order_override=None):
        """
        Preprocesses the input image and performs inference.
        Returns predicted class, confidence, probability distribution, and skincare advice.
        """
        if self.model is None:
            raise RuntimeError("Model is not initialized.")

        tensor, metadata = self.preprocess_image(image_bytes)

        # Run inference (RandomFlip/Rotation/Zoom are automatically inactive in inference mode)
        raw_predictions = self.model.predict(tensor, verbose=0)[0]
        raw_probabilities = [float(p) for p in raw_predictions]

        # Select class order (syllabus default or alphabetical)
        if class_order_override == "alphabetical":
            active_classes = ALPHABETICAL_CLASSES
        elif class_order_override == "syllabus":
            active_classes = SYLLABUS_CLASSES
        else:
            active_classes = self.classes

        # Match classes with probabilities
        probabilities_breakdown = []
        for i, class_name in enumerate(active_classes):
            prob = raw_probabilities[i]
            probabilities_breakdown.append({
                "class_name": class_name,
                "probability": round(prob * 100, 2),
                "raw_score": float(prob),
                "index": i
            })

        # Sort breakdown by descending probability
        probabilities_breakdown.sort(key=lambda x: x["raw_score"], reverse=True)

        top_result = probabilities_breakdown[0]
        predicted_class = top_result["class_name"]
        confidence = top_result["probability"]

        # Fetch corresponding skincare information
        skincare_info = SKINCARE_GUIDE.get(predicted_class, {})

        return {
            "predicted_class": predicted_class,
            "confidence": confidence,
            "confidence_score": top_result["raw_score"],
            "probabilities": probabilities_breakdown,
            "skincare_info": skincare_info,
            "general_principles": GENERAL_SKINCARE_PRINCIPLES,
            "metadata": metadata,
            "class_order_mode": class_order_override or CLASS_ORDER_MODE,
            "disclaimer": DISCLAIMER_TEXT
        }

    def get_model_info(self):
        """
        Returns model architecture and training information for academic transparency.
        """
        total_params = self.model.count_params() if self.model else 0
        trainable_params = sum([keras.ops.size(w) for w in self.model.trainable_weights]) if self.model else 0

        layers_summary = []
        if self.model:
            for l in self.model.layers:
                layers_summary.append({
                    "name": l.name,
                    "type": l.__class__.__name__,
                    "output_shape": str(l.output_shape) if hasattr(l, "output_shape") else "Unknown",
                    "param_count": l.count_params()
                })

        return {
            "project_title": "AcneCare AI - Deep Learning Acne Classifier",
            "course": "Artificial Neural Networks & Deep Learning",
            "model_architecture": "Convolutional Neural Network (CNN)",
            "framework": "TensorFlow / Keras 3",
            "input_shape": list(self.input_shape),
            "input_resolution": f"{IMAGE_SIZE[0]} x {IMAGE_SIZE[1]} pixels (RGB)",
            "total_parameters": int(total_params),
            "trainable_parameters": int(trainable_params),
            "output_classes_count": len(self.classes),
            "classes": self.classes,
            "layers": layers_summary,
            "disclaimer": DISCLAIMER_TEXT
        }

# Global instance for efficient reuse across requests
model_service = AcneModelService()

