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

# Función para la página de Calendario de Clases
def mostrar_calendario():
    # Tabla 2: Nueva tabla con el mismo formato
    datos2 = {
        "Día": ["Sábado 20/04/25 (2h)", "Domingo 21/04/25 (2h)", "Domingo 27/04/25 (2h)", "Domingo 04/05/25 (2h)"],
        "Asignatura": ["Química y Física", "Aritmética y Algebra", "Geometría y Trigonometría", "Trigonometría y Física"],
        "Tema": ["OK", 
                 "OK", 
                 "OK", 
                 "OK"]
    }

    df2 = pd.DataFrame(datos2)

    st.markdown("<p class='big-font'>📖 Actual:</p>", unsafe_allow_html=True)
    st.dataframe(df2, hide_index=True)

    st.write("Total: 15 horas hasta el 27 de abril del 2025.")  # Actualiza el total de horas
    
    # Tabla 1
    datos1 = {
        "Día": ["Sábado 22/03/25 (2h)", "Domingo 23/03/25 (2h)", "Sábado 29/03/25 (1h)", "Domingo 30/03/25 (0h)",
                "Sábado 05/04/25 (0h)", "Domingo 06/04/25 (2h)", "Sábado 12/04/25 (0h)", "Domingo 13/04/25 (2h)"],
        "Asignatura": ["Química y Física", "Geometría y Trigonometría", "Repaso", "No tuvimos clase",
                       "Química y Física", "Geometría y Trigonometría", "-", "-"],
        "Tema": ["Clasificación de la materia | Análisis dimensional y vectores",
                 "Planteo de ecuaciones en Segmentos y Ángulos | Sistema sexagesimal, centesimal y radián. Conversiones",
                 "Ejercicios", "No aplica", "-", "Resolución de exámenes y tareas-", "Postergado", "-"]
    }

    # Imagen decorativa
    st.image("img100.png", width=800)
    
    df1 = pd.DataFrame(datos1)

    st.markdown("<p class='big-font'>📖 Horario (Mes 1):</p>", unsafe_allow_html=True)
    st.dataframe(df1, hide_index=True)

    # Mensaje motivacional
    st.markdown(
        "<p class='big-font' style='text-align: center;'>🌟 ¡Ana, sigue aprendiendo y esforzándote! 🌟</p>",
        unsafe_allow_html=True
    )

    # Mostrar fecha actual
    st.markdown(f"<p style='text-align: center;'>📅 Hoy es: {datetime.now().strftime('%A, %d de %B de %Y')}</p>", unsafe_allow_html=True)

# Función para la página de Clases y Tareas
def mostrar_pendientes():
    tareas = {
        "Asignatura": ["Química y Física", "Geometría y Trigonometría", "Repaso", "Química y Física", "Geometría y Trigonometría", "Exámenes y Tareas"],
        "Tarea": ["A", "B", "C", "D", "E", "F"]
    }

    df_tareas = pd.DataFrame(tareas)

    st.markdown("<p class='big-font'>📚 Clases y Tareas Pendientes:</p>", unsafe_allow_html=True)
    st.dataframe(df_tareas, hide_index=True)

    st.markdown(
        "<p class='big-font' style='text-align: center;'>🌟 ¡No hay pendientes! 🌟</p>",
        unsafe_allow_html=True
    )

# Selector de página
pagina = st.radio("Selecciona una página:", ("Calendario de Clases", "Pendientes"))

# Mostrar según selección
if pagina == "Calendario de Clases":
    mostrar_calendario()
else:
    mostrar_pendientes()
