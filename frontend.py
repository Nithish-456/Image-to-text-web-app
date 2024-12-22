import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_description(image):
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    description = processor.decode(out[0], skip_special_tokens=True)
    return description

# Create the Gradio interface
iface = gr.Interface(fn=generate_description, inputs=gr.Image(type="pil"), outputs="text")

# Launch the interface
iface.launch(share=True)