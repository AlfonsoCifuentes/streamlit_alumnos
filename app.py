#Primero importamos las librerias necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

#Setup de la app
#De layout podemos usar wide or centered
st.set_page_config(page_title="My streamlit app", layout="wide", page_icon=":eggplant:")

#TITULO
st.title("My streamlit app")


#ENCABEZADOS
st.header("Header")
st.subheader("Subheader")

#TEXTO NORMAL
st.write("Hello, world!")

#MARKDOWN
st.markdown("Hello, **world!**")



st.sidebar.title("Sidebar")
st.sidebar.subheader("Sidebar subheader")
st.sidebar.write("Hello, world!")
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
        st.image("https://via.placeholder.com/150", caption="Placeholder image")
    with col2:
        st.write("Columna 2")
        st.image("https://via.placeholder.com/150", caption="Placeholder image")
    with col3:
        st.write("Columna 3")
        st.image("https://via.placeholder.com/150", caption="Placeholder image")