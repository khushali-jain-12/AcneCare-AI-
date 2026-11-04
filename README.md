# AcneCare AI
### Deep Learning Acne Classification & Skincare Guidance Web Application
**5th Semester Artificial Neural Networks & Deep Learning Project**

AcneCare AI is a full-stack, deep-learning-powered web application that classifies facial skin acne images into **5 clinical classes** using a trained Convolutional Neural Network (CNN) in Keras/TensorFlow, and provides tailored, evidence-based skincare advice, daily routines, and medical precautions.

---

## Project Overview

* **Course**: 5th Semester Artificial Neural Networks and Deep Learning
* **Model File**: `acne_cnn_model.keras`
* **Dataset Scope**: Acne Vulgaris (5 classes)
* **Medical Exclusion**: **Does NOT classify melanoma, atypical moles, or skin cancer.** This application is solely focused on acne vulgaris.
* **Disclaimer**: This is an experimental academic project for educational demonstration, not a clinical diagnostic tool.

---

##CNN Model Architecture & Technical Specs

| Property | Value |
| :--- | :--- |
| **Model Type** | Sequential Convolutional Neural Network (CNN) |
| **Input Shape** | `(128, 128, 3)` (Height × Width × RGB Channels) |
| **Preprocessing** | Lanczos Resizing to 128×128, Normalization to `[0.0, 1.0]` (`x / 255.0`) |
| **Total Parameters** | 831,429 parameters (~3.17 MB) |
| **Trainable Parameters** | 831,429 |
| **Loss Function** | Categorical Crossentropy |
| **Optimizer** | Adam (`learning_rate = 0.001`) |
| **Output Activation** | Softmax (5 output units) |

### 5 Classified Acne Types

1. **Blackheads** (*Open Comedones*) – Mild, non-inflammatory sebum plugs oxidized by air.
2. **Whiteheads** (*Closed Comedones*) – Mild, non-inflammatory sebum trapped beneath the skin layer.
3. **Papules** (*Inflammatory Bumps*) – Moderate, tender red bumps colonized by *C. acnes* bacteria without visible pus.
4. **Pustules** (*Pus-Filled Lesions*) – Moderate, red inflammatory base with yellow/white leukocyte fluid center.
5. **Cysts** (*Nodulocystic Acne*) – Severe, deep, painful dermal nodules; high scarring potential requiring dermatologist care.

### Class Ordering & Configuration

* **Default (Syllabus Order)**:
  * Index 0: `Blackheads`
  * Index 1: `Whiteheads`
  * Index 2: `Papules`
  * Index 3: `Pustules`
  * Index 4: `Cyst`
* **Alphabetical Order**:
  * Index 0: `Blackheads`, Index 1: `Cyst`, Index 2: `Papules`, Index 3: `Pustules`, Index 4: `Whiteheads`
  * Switchable via the UI toggle button or environment variable `CLASS_ORDER_MODE=alphabetical`.

---

## Technology Stack

* **Frontend**: React 18, Vite, Lucide Icons, Modern Responsive CSS
* **Backend**: Python 3, Flask, Flask-CORS, Werkzeug
* **Deep Learning Engine**: TensorFlow / Keras 3, NumPy, Pillow (PIL)
* **Model Storage**: `acne_cnn_model.keras`

---

## Installation & Running the Application

### 1. Prerequisites
Ensure you have the following installed on your system:
* **Python**: 3.9, 3.10, 3.11, or 3.12
* **Node.js**: v18 or newer (with `npm`)

### 2. Install Python Dependencies
Open your terminal in the project root directory and run:

```bash
pip install -r requirements.txt
```

*(Or inside your preferred virtual environment)*.

### 3. Install Frontend Dependencies
```bash
cd frontend
npm install
npm run build
cd ..
```

---

## Running the Application

### Option A: One-Command All-In-One Mode (Recommended for College Viva/Demo)
Because Flask is configured to serve the compiled React production build directly, you can start the complete application with a single terminal command:

```bash
python3 backend/app.py
```

Then open your browser and visit:
👉 **[http://localhost:5001](http://localhost:5001)**

---

### Option B: Development Mode (Hot Reloading)

If you wish to make live modifications to frontend React code or backend Flask routes, run both servers concurrently:

#### Terminal 1 (Flask Backend):
```bash
python3 backend/app.py
```
*(Runs on `http://localhost:5001`)*

#### Terminal 2 (React Vite Frontend):
```bash
cd frontend
npm run dev
```
*(Runs on `http://localhost:5173` with automatic API proxying to port 5001)*

---

## Project Directory Structure

```text
AcneCare_AI/
├── acne_cnn_model.keras          # Trained Keras CNN model (128x128x3)
├── acne_cnn_model.original.keras # Original model backup
├── requirements.txt              # Backend Python dependencies
├── README.md                     # Project documentation & run guide
├── backend/
│   ├── app.py                    # Flask REST API & static file server
│   ├── config.py                 # Hyperparameters, paths & class configuration
│   ├── model_service.py          # Keras model loader, preprocessing & inference
│   └── skincare_data.py          # Evidence-based skincare routines & do's/don'ts
└── frontend/
    ├── index.html                # Entry HTML with custom typography
    ├── package.json              # React & Vite dependencies
    ├── vite.config.js            # Vite build & proxy configuration
    ├── public/
    │   └── samples/              # 5 pre-generated verified sample acne images
    └── src/
        ├── App.jsx               # Main application component & state flow
        ├── App.css               # Skincare-aesthetic modern stylesheet
        ├── index.css             # Base resets & design system tokens
        ├── main.jsx              # React DOM root entry
        └── components/
            ├── Navbar.jsx        # Sticky glassmorphism header & status indicator
            ├── Hero.jsx          # Welcome banner & project highlights
            ├── ImageUploader.jsx # Drag-and-drop file upload with preview
            ├── AnalysisResult.jsx# Predicted class, confidence & probability distribution
            ├── SkincareGuide.jsx # Tailored morning/evening routines & active ingredients
            ├── AcneEncyclopedia.jsx # 5-class clinical reference explorer
            ├── ModelDetailsModal.jsx# Academic CNN architecture inspector for examiners
            ├── Disclaimer.jsx    # Medical safety and non-cancer disclaimer
            └── Footer.jsx        # Project credits and tech stack badges
```

---

##Testing the Classifier

1. Open **[http://localhost:5001](http://localhost:5001)** in your browser.
2. In the upload card, drag and drop an acne photo or click to browse.
3. Alternatively, click any of the **5 sample test buttons** under the dropzone (`Blackheads Sample`, `Whiteheads Sample`, `Papules Sample`, `Pustules Sample`, `Cystic Acne Sample`) to test instantly without searching for photos.
4. Click **"Analyze Skin"**.
5. Observe:
   * **Predicted Acne Class** with severity rating.
   * **Confidence Percentage** and progress bar.
   * **5-Class Softmax Probability Breakdown**.
   * **Input Preprocessing Trace** (128×128 RGB normalization).
   * **Tailored Morning & Evening Skincare Routines**.
   * **Active Ingredients Guide** (Salicylic Acid, Benzoyl Peroxide, Adapalene, Niacinamide).
   * **Essential Do's & Don'ts**.
6. Click **"CNN Architecture"** in the navigation bar to present layer-by-layer architectural decomposition to your project evaluators.

---

##Academic & Medical Disclaimer

* This application is an academic software project completed for a **5th Semester Artificial Neural Networks & Deep Learning** curriculum.
* It is created solely for experimental and educational demonstration.
* It does **NOT** provide medical diagnoses, treatment prescriptions, or clinical triage.
* It does **NOT** screen for or detect melanoma or skin cancer.
* Always consult a licensed board-certified dermatologist for professional clinical skincare evaluation.

