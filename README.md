# Proyecto de Enseñanza de Inglés con IA

Este proyecto esta inspirado en la publicacion de @leslysandra en su cuenta: https://medium.com/@leslysandra en donde utiliza modelos de IA para enseñar conceptos de gramática inglesa y crear evaluaciones. Implementa agentes utilizando `crewAI` y Google Generative AI.

## Requisitos

- Python 3.11
- `dotenv` para gestionar variables de entorno
- `crewAI` para la gestión de agentes
- `google-generativeai` para acceder a modelos de IA de Google

## Instalación

1. **Clonar este repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   ```

2. **Crear un entorno virtual y activarlo:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows usa `.\.venv\Scripts\activate`
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**

   Crea un archivo `.env` con tu clave API de Google:

   ```env
   GEMINI_API_KEY=tu_api_key_aqui
   ```

## Uso

1. **Ejecutar el proyecto:**

   ```bash
   python main.py
   ```

## Fuente Original

https://medium.com/latinxinai/tendencia-en-ia-agentes-parte-2-e25f13bab4f6
