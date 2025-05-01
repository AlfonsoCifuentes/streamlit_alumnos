#Primero importamos las librerias necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# Setup de la app (DEBE IR PRIMERO)
st.set_page_config(
    page_title="Data Analysis Dashboard",
    layout="wide",
    page_icon="📊"
)

# Custom CSS (ahora va después de set_page_config)
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTitle {
        color: #1E88E5;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    .stHeader {
        color: #2E7D32;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #e0e0e0;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# TITULO con HTML personalizado
st.markdown("<h1 style='text-align: center; color: #1E88E5;'>Data Analysis Dashboard</h1>", unsafe_allow_html=True)

# ENCABEZADOS
st.markdown("<h2 style='color: #2E7D32;'>Welcome to the Dashboard</h2>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #424242;'>Explore your data</h3>", unsafe_allow_html=True)

# TEXTO NORMAL con estilo
st.markdown("<p style='font-size: 18px; color: #424242;'>Welcome to our interactive data analysis platform!</p>", unsafe_allow_html=True)

# Sidebar con estilo
st.sidebar.markdown("""
    <div style='background-color: #1E88E5; padding: 10px; border-radius: 5px;'>
        <h2 style='color: white; text-align: center;'>Dashboard Controls</h2>
    </div>
    """, unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='color: #2E7D32;'>Settings</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #424242;'>Adjust your parameters here</p>", unsafe_allow_html=True)
st.sidebar.markdown("Hello, **world!**")

#Pestañas

tab1, tab2,tab3, tab4 = st.tabs(["Inicio", "Datos", "Gráficos", "Columnas"])

with tab1:
    st.title("Inicio")
    st.write("Bienvenido a la app de streamlit")
    #LATEX
    st.latex(r'''a^2 + b^2 = c^2''')

    #code
    st.code('print("Hello, world!")', language='python')

    #iNFORMACIÓN, ADVERTENCIAS Y ERRORES
    st.info("This is an info message")
    st.warning("This is a warning message")
    st.error("This is an error message")
    st.success("This is a success message")
    st.exception("This is an exception message")
    st.help("This is a help message")
    st.json({"key": "value"})
    st.dataframe({"key": "value"})
    st.table({"key": "value"})
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    st.progress(50)
    st.spinner("Loading...")
    st.image("https://via.placeholder.com/150", caption="Placeholder image")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")


with tab2:
    st.title("Datos")
    st.write("Aquí puedes ver los datos")
    #Importando la libreria pandas para leer el csv
    df = pd.read_csv('titanic_limpio.csv')

    #Mostrando el dataframe en la app con streamlit
    st.dataframe(df)



with tab3:
    st.title("Gráficos")
    st.write("Aquí puedes ver los gráficos")
    fig = px.scatter(df, x="Age", y="Fare", color="Survived")
    st.plotly_chart(fig)
    fig = px.histogram(df, x="Age", color="Survived")
    st.plotly_chart(fig)
    fig = px.box(df, x="Age", y="Fare", color="Survived")
    st.plotly_chart(fig)
    st.map()

with tab4:
    st.title("Columnas")
    st.write("Aquí puedes ver las columnas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Columna 1")
        st.image("https://i.gifer.com/origin/92/92fee742dc7a3b5ae117ca8ca4bc5c07_w200.gif", caption="Placeholder image")
    with col2:
        st.write("Columna 2")
        st.image("https://i.pinimg.com/originals/88/81/d1/8881d18649eb272c6d00f345f7064b44.gif", caption="Placeholder image")
    with col3:
        st.write("Columna 3")
        st.image("https://giffiles.alphacoders.com/128/12839.gif", caption="Placeholder image")