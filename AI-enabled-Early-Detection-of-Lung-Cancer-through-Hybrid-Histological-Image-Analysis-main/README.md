# 🧠 Advancing Oncology Diagnostics: AI-enabled Early Detection of Lung Cancer through Hybrid Histological Image Analysis
![image](https://github.com/user-attachments/assets/a68892c1-9b28-4d38-a08e-48e91abcf8fe)

## 🎯 Objective
This project aims to leverage artificial intelligence to assist in the **early detection of lung cancer** by analyzing histological images. It uses a **hybrid deep learning model** and provides a **Gradio-based UI** for clinicians and researchers to upload images and receive real-time diagnostic predictions.

---

## 📁 Dataset
We use a publicly available histopathology image dataset for lung cancer diagnosis.

🔗 **Dataset Link (Kaggle):**  
[Lung and Colon Cancer Histopathological Images](https://www.kaggle.com/datasets/andrewmvd/lung-and-colon-cancer-histopathological-images)

- Images are labeled into:
  - **Lung Adenocarcinoma**
  - **Lung Benign Tissue**
  - **Lung Squamous Cell Carcinoma**
  - **Colon Adenocarcinoma**
  - **Colon Benign Tissue**

---

## 🧠 Model Architecture
- A hybrid deep learning model combining **CNN** layers for spatial feature extraction and **dense layers** for classification.
- Trained on augmented histological image data for better generalization.
- Final layer uses **Softmax** activation for multi-class classification.

📊 **Model Accuracy:** Achieved over **96% accuracy** on the validation set.

---

## 💻 Gradio UI Overview
The project features an intuitive UI built with **Gradio** that allows:
- 📤 Uploading histopathological images (JPG/PNG format)
- 🔍 Real-time prediction of cancerous vs. non-cancerous tissue
- 📈 Confidence score visualization
![Screenshot 2025-04-08 144708](https://github.com/user-attachments/assets/53f099ea-e63e-4e76-ad09-faa9af89a0dc)

---

## 🚀 How to Run

### 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/lung-cancer-detection.git
   cd lung-cancer-detection
