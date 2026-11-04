import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)

# Path to the trained Keras model
MODEL_PATH = os.environ.get(
    "ACNE_MODEL_PATH",
    os.path.join(PROJECT_ROOT, "acne_cnn_model.keras")
)

# Model configuration
IMAGE_SIZE = (128, 128)
INPUT_SHAPE = (128, 128, 3)
CHANNELS = 3
RESCALE_FACTOR = 1.0 / 255.0

# Class Order Configuration
# Default: Follows the project syllabus / user prompt ordering (1-5):
# 1. Blackheads, 2. Whiteheads, 3. Papules, 4. Pustules, 5. Cyst
# Alternative: Alphabetical folder ordering if dataset subfolders were unsorted.
CLASS_ORDER_MODE = os.environ.get("CLASS_ORDER_MODE", "syllabus").lower()

SYLLABUS_CLASSES = [
    "Blackheads",
    "Whiteheads",
    "Papules",
    "Pustules",
    "Cyst"
]

ALPHABETICAL_CLASSES = [
    "Blackheads",
    "Cyst",
    "Papules",
    "Pustules",
    "Whiteheads"
]

if CLASS_ORDER_MODE == "alphabetical":
    CLASS_NAMES = ALPHABETICAL_CLASSES
else:
    CLASS_NAMES = SYLLABUS_CLASSES

# Server configuration
HOST = os.environ.get("HOST", "0.0.0.0")
# macOS AirPlay often listens on port 5000, so port 5001 avoids collisions by default
PORT = int(os.environ.get("PORT", 5001))
DEBUG = os.environ.get("FLASK_ENV", "development") == "development"

# Allowed upload extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB max file upload

