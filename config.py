from google import generativeai
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener la API key del archivo .env
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Verificar que se cargó correctamente
if GEMINI_API_KEY:
    print("API Key cargada correctamente")
else:
    print("Error: No se encontró GEMINI_API_KEY en el archivo .env")

# Configurar la API key para Google GenerativeAI si es necesario
gemini_api_key = generativeai.configure(api_key=GEMINI_API_KEY)
