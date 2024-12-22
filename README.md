# 🖼️ Image Description Web Application  

## ✨ Overview  
This project is a web application that allows users to upload an image and receive a **textual description** of its content using a pre-trained **image captioning model** from Hugging Face.  

The application combines the power of **FastAPI** for the backend and **Gradio** for a sleek, user-friendly interface. 🚀  

---

## 💡 Approach  

### 🔍 Model Selection  
We utilized the **BLIP (Bootstrapping Language-Image Pre-training)** model from Salesforce, available on Hugging Face. This state-of-the-art model excels in generating descriptive captions for images.  

### 🛠️ Backend Development  
- Built with **FastAPI** for creating a fast and efficient RESTful API.  
- Includes an endpoint to handle image uploads and process them with the BLIP model.  

### 🎨 Frontend Development  
- Developed with **Gradio**, providing an intuitive web interface.  
- Users can upload images, and captions are generated in real-time!  

### 🚢 Deployment  
- Run the application locally or use **Docker** for easy deployment.  
- Step-by-step instructions are provided for both methods.  

---

## ✨ Features  

- 📤 **Upload images** and get descriptive captions instantly.  
- 🔍 Powered by a **pre-trained image captioning model** for high accuracy.  
- 🌟 Simple, intuitive, and user-friendly interface using Gradio.  
- ⚡ Option to run as a REST API with **FastAPI**.  

---

## 📦 Installation  

### 🔧 Prerequisites  

- 🐍 Python 3.7 or higher  
- 📦 pip (Python package installer)  

### 🛠️ Step-by-Step Guide  

1. **Clone the Repository**  
   ```bash  
   git clone <https://github.com/Nithish-456/Image-to-text-web-app.git>  
   cd <image_to_text>  
'''
### Step 2: Create a Virtual Environment (Optional)
### Step 3: Install requierd packages: pip install gradio transformers pillow
### Step 4: Run Frontend
 - python frontend.py
 - Open your web browser and navigate to http://localhost:7860 to access the interface.
### Step 5: Run Backend
 - If you prefer to use FastAPI, you can run the FastAPI application with the following code in backend.py
 - Access the application at http://localhost:8000
