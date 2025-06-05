# Proyecto de Enseñanza de Inglés con IA

Este proyecto utiliza modelos de IA para enseñar conceptos de gramática inglesa y crear evaluaciones. Implementa agentes utilizando \`crewAI\` y Google Generative AI.

## Requisitos

- Python 3.11
- \`dotenv\` para gestionar variables de entorno
- \`crewAI\` para la gestión de agentes
- \`google-generativeai\` para acceder a modelos de IA de Google

## Instalación

1. **Clonar este repositorio:**

   \`\`\`bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   \`\`\`

2. **Crear un entorno virtual y activarlo:**

   \`\`\`bash
   python3 -m venv .venv
   source .venv/bin/activate  # En Windows usa \`.\.venv\Scripts\activate\`
   \`\`\`

3. **Instalar dependencias:**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Configurar variables de entorno:**

   Crea un archivo \`.env\` con tu clave API de Google:

   \`\`\`env
   GEMINI_API_KEY=tu_api_key_aqui
   \`\`\`

## Uso

1. **Configurar una tarea educativa:**

   Define agentes y tareas, utilizando modelos de \`Gemini\`:

   \`\`\`python
   from google import generativeai
   from dotenv import load_dotenv
   import os
   from crewai import Agent, Task, LLM, Crew

   load_dotenv()
   GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

   # Configura modelos de IA
   gemini_api_key = generativeai.configure(api_key=GEMINI_API_KEY)

   # Agente Profesor
   profesor = Agent(
       role=\"Profesor de Inglés\",
       goal=\"Explicar conceptos de gramática y vocabulario en inglés de manera clara y efectiva.\",
       verbose=True,
       llm=LLM(model='gemini/gemini-2.0-flash', api_key=gemini_api_key)
   )

   # Agente Evaluador
   evaluador = Agent(
       role=\"Evaluador de Inglés\",
       goal=\"Diseñar preguntas de evaluación y revisar las respuestas del estudiante.\",
       verbose=True,
       llm=LLM(model='gemini/gemini-2.0-flash', api_key=gemini_api_key)
   )

   # Definir tareas
   explicacion_ingles = Task(
       description=\"Explica la diferencia entre los tiempos verbales 'Present Perfect' y 'Past Simple' con ejemplos.\",
       agent=profesor
   )

   evaluacion_ingles = Task(
       description=\"Crea un test de 3 preguntas basado en la explicación dada por el profesor y evalúa respuestas.\",
       agent=evaluador
   )

   # Crear y ejecutar la Crew
   crew = Crew(
       agents=[profesor, evaluador],
       tasks=[explicacion_ingles, evaluacion_ingles],
       verbose=True
   )

   resultado = crew.kickoff()
   print(resultado)
   \`\`\`

2. **Ejecutar el proyecto:**

   \`\`\`bash
   python main.py
   \`\`\`

## Contribuir

Contribuciones son bienvenidas. Siéntete libre de abrir un Issue o enviar un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT." > README.md