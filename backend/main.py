from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
import base64
import openai
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar API key de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # O ["*"] para permitir todos los orígenes (menos seguro)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("L")

        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        prompt = "Describe esta imagen SAR en lenguaje sencillo para un cliente:"

        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de imágenes satelitales."},
                {"role": "user", "content": prompt},
                {"role": "user", "content": {"image": img_str, "type": "image"}}
            ]
        )

        description = response['choices'][0]['message']['content']
        return {"description": description}
    except Exception as e:
        return {"error": str(e)}
