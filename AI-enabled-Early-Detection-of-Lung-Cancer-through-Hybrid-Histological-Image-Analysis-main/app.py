import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# ✅ Load the trained model
model = tf.keras.models.load_model("lung_cancer_classifier.h5")

# ✅ Define class labels
categories = ['Benign case', 'Malignant case', 'Normal case']
img_size = 256

def predict_lung_cancer(image):
    # Convert image to grayscale, resize, normalize
    image = image.convert('L')  # Grayscale
    image = image.resize((img_size, img_size))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, img_size, img_size, 1)

    # Predict
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    confidence_scores = {categories[i]: float(prediction[0][i]) for i in range(len(categories))}

    return categories[predicted_index], confidence_scores

# ✅ Build the Gradio interface
demo = gr.Interface(
    fn=predict_lung_cancer,
    inputs=gr.Image(type="pil", label="Upload Chest X-ray"),
    outputs=[
        gr.Label(label="Prediction"),
        gr.Label(label="Confidence Scores")
    ],
    title="Lung Cancer Classifier",
    description="Upload a chest X-ray image to predict lung cancer category: Benign, Malignant, or Normal."
)

# ✅ Launch the app (for local use) or comment this out if deploying on Hugging Face
if __name__ == "__main__":
    demo.launch()
