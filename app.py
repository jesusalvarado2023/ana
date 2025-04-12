#ana2025.streamlit.app
import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Calendario de Clases de Ana", page_icon="📚", layout="centered")

# Estilos infantiles
st.markdown(
    """
    <style>
        body {background-color: #ffebcd;}
        .big-font {font-size: 25px !important; color: #ff69b4;}
        .calendar {border-radius: 10px; background: #fffacd; padding: 10px; margin: 10px 0;}
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h1 style='text-align: center; color: #ff4500;'>📆 Calendario de Clases de Ana 🎨</h1>", unsafe_allow_html=True)

# Definir el calendario
datos = {
    "Día": ["Sábado 22/03/25 (2h)", "Domingo 23/03/25 (2h)", "Sábado 29/03/25 (1h)", "Domingo 30/03/25 (0h)", "Sábado 05/04/25 (0h)", "Domingo 06/04/25 (2h)",
           "Sábado 12/04/25 (0h)", "Domingo 13/04/25 (2h)"],
    "Asignatura": ["Química y Física", "Geometría y Trigonometría","Repaso","No tuvimos clase", "Química y Física", "Geometría y Trigonometría",
                  "-", "-"],
    "Tema": ["Clasificación de la materia | Análisis dimensional y vectores", "Planteo de ecuaciones en Segmentos y Ángulos | Sistema sexagesimal, centesimal y radián. Conversiones", "Ejercicios", "No aplica","-","Resolución de exámenes y tareas-",
            "Postergado", "-"]
}

df = pd.DataFrame(datos)

# Mostrar el calendario
st.markdown("<p class='big-font'>📖 Horarios:</p>", unsafe_allow_html=True)
st.dataframe(df, hide_index=True)

st.write("Total: 9 horas hasta el 13 de abril del 2025.")
# Imagen decorativa
st.image("img100.png", width=800)

# Mensaje de motivación
st.markdown(
    "<p class='big-font' style='text-align: center;'>🌟 ¡Ana, sigue aprendiendo y esforzándote! 🌟</p>",
    unsafe_allow_html=True
)

# Mostrar fecha y hora actual
st.markdown(f"<p style='text-align: center;'>📅 Hoy es: {datetime.now().strftime('%A, %d de %B de %Y')}</p>", unsafe_allow_html=True)
