#Primero importamos las librerias necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Setup de la app (DEBE IR PRIMERO)
st.set_page_config(
    page_title="Titanic Analysis",
    layout="wide",
    page_icon="🚢"
)

# Custom CSS (ahora va después de set_page_config)
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    h1 {
        color: white;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        text-align: center;
        padding: 1.5rem 0;
        background: linear-gradient(90deg, #1a237e 0%, #3949ab 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    h2 {
        color: #283593;
        font-family: 'Helvetica Neue', sans-serif;
        border-bottom: 2px solid #3949ab;
        padding-bottom: 0.5rem;
    }
    .stTab {
        background-color: #e8eaf6;
        border-radius: 5px;
        padding: 1rem;
    }
    .stButton>button {
        background-color: #3949ab;
        color: white;
        border-radius: 5px;
    }
    .sidebar .sidebar-content {
        background-color: #f5f5f5;
        border-radius: 10px;
    }
    div[data-testid="stSidebarNav"] {
        background-color: rgba(57, 73, 171, 0.1);
        padding: 1rem;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar mejorado
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #1a237e;'>🚢 Navegación</h2>", unsafe_allow_html=True)
    
    page = st.radio(
        "",
        ["📊 Resumen", "📋 Datos", "📈 Gráficos", "📑 Análisis"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### 📌 Filtros")
    
    # Añadir filtros útiles
    if 'df' in locals():
        survived = st.checkbox("Mostrar solo supervivientes")
        class_filter = st.multiselect("Clase", ["1ra", "2da", "3ra"])
        age_range = st.slider("Rango de edad", 0, 100, (0, 100))

# Contenido principal
st.markdown("<h1>🚢 Análisis del Titanic</h1>", unsafe_allow_html=True)

# Imagen del Titanic en la página de inicio
if page == "📊 Resumen":
    # Mostrar la imagen centrada y al 50% del ancho usando HTML para padding
    left, center, right = st.columns([1,2,1])
    with center:
        st.markdown(
            """
            <div style="padding:3rem 0;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg"
                     alt="RMS Titanic"
                     style="display:block; margin-left:auto; margin-right:auto; width:50%;">
                <div style="text-align:center; color: #666; font-size: 0.9rem;">
                    RMS Titanic (Fuente: Wikimedia Commons)
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Pasajeros", "891", "100%")
    with col2:
        st.metric("Supervivientes", "342", "+38.4%")
    with col3:
        st.metric("Edad Media", "29.7 años")
        
    st.markdown("""
    ### 🎯 Objetivo del Análisis
    Explorar los patrones de supervivencia en el desastre del Titanic.
    """)

elif page == "📋 Datos":
    try:
        df = pd.read_csv('titanic_limpio.csv')
        st.markdown("### 📋 Dataset del Titanic")
        
        # Mostrar info básica del dataset
        st.markdown("#### 📊 Información del Dataset")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Número de filas:** {df.shape[0]}")
            st.write(f"**Número de columnas:** {df.shape[1]}")
        with col2:
            st.write(f"**Columnas:** {', '.join(df.columns.tolist())}")
        
        # Mostrar los datos sin estilo
        st.markdown("#### 🔍 Datos")
        st.dataframe(df)
        
        # Estadísticas descriptivas para columnas numéricas
        st.markdown("#### 📈 Estadísticas Descriptivas")
        st.dataframe(df.describe())
        
    except Exception as e:
        st.error(f"Error al cargar los datos: {str(e)}")

elif page == "📈 Gráficos":
    df = pd.read_csv('titanic_limpio.csv')
    st.markdown("### 📈 Visualización de Datos")
    
    # Gráficos mejorados
    tab1, tab2, tab3 = st.tabs(["Supervivencia", "Edad", "Tarifa"])
    
    with tab1:
        fig = px.pie(df, names='Survived', title='Tasa de Supervivencia')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        fig = px.histogram(df, x="Age", color="Survived", 
                          title='Distribución de Edad por Supervivencia')
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        fig = px.box(df, x="Pclass", y="Fare", color="Survived",
                    title='Distribución de Tarifas por Clase')
        st.plotly_chart(fig, use_container_width=True)

elif page == "📑 Análisis":
    try:
        # Cargar el dataset al inicio de la sección
        df = pd.read_csv('titanic_limpio.csv')
        
        st.markdown("### 📑 Conclusiones Principales")
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("💡 La tasa de supervivencia fue mayor en mujeres")
            st.info("💡 Los pasajeros de primera clase tuvieron mejor chance")
        
        with col2:
            st.info("💡 Los niños tuvieron prioridad en el rescate")
            st.info("💡 La mayoría de las víctimas fueron hombres")
        
    except Exception as e:
        st.error(f"Error al cargar los datos: {str(e)}")