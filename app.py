import os
import logging
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from config import (
    HOST,
    PORT,
    DEBUG,
    ALLOWED_EXTENSIONS,
    MAX_CONTENT_LENGTH,
    CLASS_NAMES,
    IMAGE_SIZE,
    CLASS_ORDER_MODE,
    PROJECT_ROOT
)
from model_service import model_service
from skincare_data import SKINCARE_GUIDE, GENERAL_SKINCARE_PRINCIPLES, DISCLAIMER_TEXT

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("AcneCare_AI")

FRONTEND_DIST = os.path.join(PROJECT_ROOT, "frontend", "dist")

# Initialize Flask application
app = Flask(__name__, static_folder=FRONTEND_DIST, static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

# Enable CORS for all frontend requests
CORS(app, resources={r"/api/*": {"origins": "*"}})

def is_allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve frontend single-page application if dist is built
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(FRONTEND_DIST, path)):
        return send_from_directory(FRONTEND_DIST, path)
    elif os.path.exists(os.path.join(FRONTEND_DIST, "index.html")):
        return send_from_directory(FRONTEND_DIST, "index.html")
    else:
        return jsonify({
            "message": "AcneCare AI Backend is running.",
            "frontend_status": "Run 'npm run dev' inside the frontend directory, or 'npm run build' to bundle.",
            "api_health": "/api/health",
            "api_classes": "/api/classes"
        }), 200

@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint to verify backend status and model readiness."""
    return jsonify({
        "status": "healthy",
        "service": "AcneCare AI Backend",
        "model_loaded": model_service.model is not None,
        "input_resolution": f"{IMAGE_SIZE[0]}x{IMAGE_SIZE[1]}",
        "classes": CLASS_NAMES,
        "class_order_mode": CLASS_ORDER_MODE
    }), 200

@app.route("/api/model-info", methods=["GET"])
def model_info():
    """Academic model details including layer architecture, params count, and preprocessing specs."""
    try:
        info = model_service.get_model_info()
        return jsonify(info), 200
    except Exception as e:
        logger.error(f"Error retrieving model info: {e}")
        return jsonify({"error": "Unable to load model metadata"}), 500

@app.route("/api/classes", methods=["GET"])
def get_classes():
    """Returns educational descriptions of all 5 classified acne types."""
    return jsonify({
        "classes": CLASS_NAMES,
        "skincare_guide": SKINCARE_GUIDE,
        "general_principles": GENERAL_SKINCARE_PRINCIPLES,
        "disclaimer": DISCLAIMER_TEXT
    }), 200

@app.route("/api/analyze", methods=["POST"])
def analyze_skin():
    """
    Main image analysis endpoint.
    Accepts:
      - 'image': File (multipart/form-data)
      - 'class_order': Optional string ('syllabus' or 'alphabetical')
    Returns:
      - predicted_class: string
      - confidence: float (percentage)
      - probabilities: array of {class_name, probability, raw_score}
      - skincare_info: dict of care instructions
      - metadata: preprocessing specifications
      - disclaimer: academic project notice
    """
    if "image" not in request.files:
        return jsonify({
            "error": "No image file provided in request. Please upload an acne image."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "error": "No file selected. Please choose an image file."
        }), 400

    if not is_allowed_file(file.filename):
        return jsonify({
            "error": f"Unsupported file type. Allowed formats: {', '.join(ALLOWED_EXTENSIONS)}"
        }), 400

    try:
        image_bytes = file.read()
        if len(image_bytes) == 0:
            return jsonify({"error": "Uploaded image file is empty."}), 400

        class_order = request.form.get("class_order", None)

        logger.info(f"Processing image analysis request for: {file.filename} ({len(image_bytes)} bytes)")
        result = model_service.predict(image_bytes, class_order_override=class_order)

        return jsonify({
            "success": True,
            "filename": file.filename,
            **result
        }), 200

    except ValueError as ve:
        logger.warning(f"Validation error: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logger.exception(f"Unexpected inference error: {e}")
        return jsonify({
            "error": f"An error occurred while analyzing the image: {str(e)}"
        }), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    return jsonify({
        "error": f"File is too large. Maximum allowed file size is {MAX_CONTENT_LENGTH // (1024 * 1024)}MB."
    }), 413

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Requested API endpoint not found."}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error occurred."}), 500

if __name__ == "__main__":
    logger.info(f"Starting AcneCare AI Backend on http://{HOST}:{PORT}")
    app.run(host=HOST, port=PORT, debug=DEBUG)
