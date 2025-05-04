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

# Definir el menú de pestañas
pestaña = st.radio("Selecciona una pestaña:", ("Calendario Original", "Calendario Nuevo"))

# Crear el calendario original
if pestaña == "Calendario Original":
    # Definir el calendario original
    datos = {
        "Día": ["Sábado 22/03/25 (2h)", "Domingo 23/03/25 (2h)", "Sábado 29/03/25 (1h)", "Domingo 30/03/25 (0h)", "Sábado 05/04/25 (0h)", "Domingo 06/04/25 (2h)",
               "Sábado 12/04/25 (0h)", "Domingo 13/04/25 (2h)"],
        "Asignatura": ["Química y Física", "Geometría y Trigonometría","Repaso","No tuvimos clase", "Química y Física", "Geometría y Trigonometría",
                      "-", "-"],
        "Tema": ["Clasificación de la materia | Análisis dimensional y vectores", "Planteo de ecuaciones en Segmentos y Ángulos | Sistema sexagesimal, centesimal y radián. Conversiones", "Ejercicios", "No aplica","-","Resolución de exámenes y tareas-",
                "Postergado", "-"]
    }

    df = pd.DataFrame(datos)

    # Mostrar el calendario original
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

# Crear el calendario nuevo
elif pestaña == "Calendario Nuevo":
    st.markdown("<h2 style='text-align: center; color: #ff4500;'>📅 Nuevo Calendario de Clases</h2>", unsafe_allow_html=True)
    
    # Aquí puedes agregar nuevos campos para llenar el calendario
    nuevo_dia = st.text_input("Día (Ejemplo: Sábado 22/03/25 (2h))")
    nueva_asignatura = st.text_input("Asignatura")
    nuevo_tema = st.text_input("Tema")

    if st.button("Agregar al Calendario"):
        if nuevo_dia and nueva_asignatura and nuevo_tema:
            # Crear o actualizar un DataFrame con la nueva clase
            nuevo_dato = {"Día": [nuevo_dia], "Asignatura": [nueva_asignatura], "Tema": [nuevo_tema]}
            nuevo_df = pd.DataFrame(nuevo_dato)
            
            # Mostrar el nuevo calendario con la clase agregada
            st.markdown("<p class='big-font'>📖 Horarios Actualizados:</p>", unsafe_allow_html=True)
            st.dataframe(nuevo_df, hide_index=True)
            st.write(f"Total: {len(nuevo_df)} horas hasta el {datetime.now().strftime('%d de abril del 2025')}")
        else:
            st.warning("Por favor, completa todos los campos antes de agregar al calendario.")
