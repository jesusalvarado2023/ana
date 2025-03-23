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
    "Día": ["Sábado 22/03/25 OK", "Domingo 23/03/25 OK", "Sábado 22/03/25", "Domingo 30/03/25"],
    "Asignatura": ["Química y Física", "Geometría y Trigonometría", "Química y Física", "Geometría y Trigonometría"],
    "Tema": ["Clasificación de la materia | Análisis dimensional y vectores", "Planteo de ecuaciones en Segmentos y Ángulos", "Pendiente", "Pendiente"]
}

df = pd.DataFrame(datos)

# Mostrar el calendario
st.markdown("<p class='big-font'>📖 Horario de Clases:</p>", unsafe_allow_html=True)
st.dataframe(df, hide_index=True)

# Mensaje de motivación
st.markdown(
    "<p class='big-font' style='text-align: center;'>🌟 ¡Ana, sigue aprendiendo y divirtiéndote! 🌟</p>",
    unsafe_allow_html=True
)

# Imagen decorativa
st.image("img100.png", width=300)

# Mostrar fecha y hora actual
st.markdown(f"<p style='text-align: center;'>📅 Hoy es: {datetime.now().strftime('%A, %d de %B de %Y')}</p>", unsafe_allow_html=True)
