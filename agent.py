from crewai import Agent, Task, LLM
from config import gemini_api_key

# Agente Profesor: Explica conceptos de inglés
profesor = Agent(
    role="Profesor de Inglés",
    goal="Explicar conceptos de gramática y vocabulario en inglés de manera clara y efectiva.",
    backstory="Eres un profesor con experiencia en enseñar inglés a estudiantes de todos los niveles.",
    verbose=True,
    allow_delegation=False,
    llm=LLM(model='gemini/gemini-2.0-flash', api_key=gemini_api_key)
)

# Agente Evaluador: Crea ejercicios y corrige respuestas
evaluador = Agent(
    role="Evaluador de Inglés",
    goal="Diseñar preguntas de evaluación y revisar las respuestas del estudiante.",
    backstory="Eres un experto en pruebas de inglés y puedes dar retroalimentación detallada.",
    verbose=True,
    allow_delegation=False,
    llm=LLM(model='gemini/gemini-2.0-flash', api_key=gemini_api_key)
)

# Tarea 1: El profesor debe explicar un concepto de inglés
explicacion_ingles = Task(
    description="Explica la diferencia entre los tiempos verbales 'Present Perfect' y 'Past Simple' con ejemplos.",
    agent=profesor,
    expected_output="Una explicación clara y concisa de la diferencia entre 'Present Perfect' y 'Past Simple', incluyendo ejemplos."  # Agregar expected_output
)

# Tarea 2: El evaluador debe crear una prueba basada en la explicación
evaluacion_ingles = Task(
    description="Crea un test de 3 preguntas basado en la explicación dada por el profesor y evalúa respuestas.",
    agent=evaluador,
    expected_output="Un test de 3 preguntas con sus respuestas correctas, relacionado con la diferencia entre 'Present Perfect' y 'Past Simple'."  # Agregar expected_output
)
