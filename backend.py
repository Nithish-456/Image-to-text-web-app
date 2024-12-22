from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

app = FastAPI()

# Load the pre-trained model and processor from the hugging face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Post page to upload image and get the description
@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Read the image file
    image = Image.open(file.file).convert("RGB")
    
    # Process the image and generate a description
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    description = processor.decode(out[0], skip_special_tokens=True)
    
    return {"description": description}

# Main page to upload the image
@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <html>
        <head>
            <title>Image Description App</title>
            <style>
                body { font-family: Arial, sans-serif; }
                input[type="file"] { margin: 20px; }
                #description { margin-top: 20px; }
            </style>
        </head>
        <body>
            <h1>Upload an Image for Description</h1>
            <input type="file" id="fileInput" accept="image/*">
            <button onclick="uploadImage()">Upload</button>
            <div id="description"></div>
            <script>
                async function uploadImage() {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    const formData = new FormData();
                    formData.append('file', file);
                    
                    const response = await fetch('/upload/', {
                        method: 'POST',
                        body: formData
                    });
                    const result = await response.json();
                    document.getElementById('description').innerText = result.description;
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(content=content)

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)