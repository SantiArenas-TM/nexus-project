import os

from dotenv import load_dotenv
from google import genai

# Carga las variables guardadas en el archivo .env
load_dotenv(override=True)

# La API Key se lee desde el archivo .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Modelo rápido y optimizado para texto
MODEL_NAME = "gemini-3.6-flash"


# Función que configura las credenciales y devuelve el cliente listo para usar
def get_gemini_client():
    if not GEMINI_API_KEY:
        raise ValueError("Falta la variable GEMINI_API_KEY en el archivo .env")

    return genai.Client(api_key=GEMINI_API_KEY)