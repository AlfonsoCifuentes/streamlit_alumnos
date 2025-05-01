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
st.balloons()
st.snow()
st.map()
st.image("https://via.placeholder.com/150", caption="Placeholder image")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
st.file_uploader("Upload a file", type=["csv", "txt"])
st.download_button("Download a file", data="Hello, world!", file_name="hello.txt")


#Importando la libreria pandas para leer el csv
df = pd.read_csv(r'E:\Proyectos\VisualStudio\Upgrade_Data_AI\streamlit_alumnos\titanic_limpio.csv')

#Mostrando el dataframe en la app con streamlit
st.dataframe(df)

st.sidebar.title("Sidebar")
st.sidebar.subheader("Sidebar subheader")
st.sidebar.write("Hello, world!")
st.sidebar.markdown("Hello, **world!**")
