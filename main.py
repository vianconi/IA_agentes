from agent import profesor, evaluador, explicacion_ingles, evaluacion_ingles
from crewai import Crew

# # Crear un equipo (Crew) con ambos agentes y sus tareas
crew = Crew(
    agents=[profesor, evaluador],
    tasks=[explicacion_ingles, evaluacion_ingles],
    verbose=True # Esto nos permitirá ver cómo interactúan los agentes
)
# Ejecutar la Crew
resultado = crew.kickoff()

# Mostrar el resultado final
print(resultado)
