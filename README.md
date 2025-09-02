# 🚢 Streamlit Titanic Analysis Dashboard

<div align="center">

![Streamlit Titanic Banner](https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg)

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

**📊 Dashboard interactivo para explorar los datos del Titanic con visualizaciones dinámicas**

*Aplicación educativa desarrollada con Streamlit para el análisis de datos y machine learning*

[🚀 Demo en Vivo](#demo) • [📖 Características](#características) • [⚡ Instalación](#instalación) • [📊 Análisis](#análisis)

</div>

---

## 🎯 Descripción del Proyecto

**Streamlit Alumnos** es una aplicación web interactiva desarrollada con **Streamlit** que permite explorar y analizar los famosos datos del desastre del Titanic. Esta herramienta educativa está diseñada para estudiantes y profesionales que desean aprender sobre análisis de datos, visualización interactiva y desarrollo de dashboards web con Python.

### 🔑 Características Principales

| Característica | Descripción | Tecnología |
|----------------|-------------|------------|
| **📊 Dashboard Interactivo** | Interfaz web responsive con múltiples pestañas | Streamlit |
| **📈 Visualizaciones Dinámicas** | Gráficos interactivos de alta calidad | Plotly Express |
| **🔍 Análisis Exploratorio** | Estadísticas descriptivas y filtros avanzados | Pandas |
| **🎨 UI/UX Personalizada** | Diseño moderno con CSS personalizado | HTML/CSS |
| **📱 Responsive Design** | Optimizado para dispositivos móviles y desktop | Streamlit Layout |

---

## 🛠️ Stack Tecnológico

### 🐍 **Backend & Análisis**
```python
# Dependencias principales
streamlit >= 1.0.0      # Framework web para aplicaciones de datos
pandas >= 1.3.0         # Manipulación y análisis de datos
plotly >= 5.0.0         # Visualizaciones interactivas
```

### 🎨 **Frontend & Estilo**
- **Streamlit Components**: Sidebar, columns, tabs, metrics
- **CSS Personalizado**: Gradientes, colores temáticos, typography
- **HTML Embebido**: Elementos custom para mejor UX

### 📊 **Visualización**
- **Plotly Express**: Gráficos interactivos (pie charts, histogramas, box plots)
- **Streamlit Charts**: Métricas y KPIs
- **Custom Styling**: Paletas de colores temáticas del Titanic

---

## 📋 Características del Dataset

### 📈 **Información General**
- **Filas**: 891 registros de pasajeros
- **Columnas**: Variables demográficas, socioeconómicas y de supervivencia
- **Calidad**: Dataset limpio y preprocesado
- **Origen**: Kaggle Titanic Dataset (versión educativa)

### 🔍 **Variables Analizadas**

#### 👥 **Demográficas**
- `Age` - Edad del pasajero
- `Sex` - Género (Male/Female)
- `Name` - Nombre completo
- `PassengerId` - Identificador único

#### 🚢 **Viaje**
- `Pclass` - Clase del boleto (1ª, 2ª, 3ª)
- `Ticket` - Número de boleto
- `Fare` - Tarifa pagada
- `Cabin` - Número de cabina
- `Embarked` - Puerto de embarque (C/Q/S)

#### 👨‍👩‍👧‍👦 **Familia**
- `SibSp` - Hermanos/cónyuges a bordo
- `Parch` - Padres/hijos a bordo

#### 🎯 **Target Variable**
- `Survived` - Supervivencia (0: No, 1: Sí)

---

## 🎨 Funcionalidades del Dashboard

### 📊 **1. Página de Resumen**
- **KPIs Principales**: Total pasajeros, supervivientes, edad media
- **Imagen Histórica**: RMS Titanic con fuente
- **Métricas Visuales**: Cards con indicadores de rendimiento
- **Objetivo del Análisis**: Contexto educativo

### 📋 **2. Sección de Datos**
- **Vista Tabular**: DataFrame interactivo con scroll
- **Estadísticas Descriptivas**: Análisis automático de columnas numéricas
- **Información del Dataset**: Dimensiones y metadata
- **Validación de Datos**: Manejo de errores y excepciones

### 📈 **3. Visualizaciones Interactivas**

#### 🥧 **Supervivencia**
```python
# Gráfico de torta interactivo
fig = px.pie(df, names='Survived', 
            title='Tasa de Supervivencia')
```

#### 📊 **Distribución por Edad**
```python
# Histograma con codificación de color
fig = px.histogram(df, x="Age", color="Survived",
                  title='Distribución de Edad por Supervivencia')
```

#### 📦 **Análisis de Tarifas**
```python
# Box plot por clase y supervivencia
fig = px.box(df, x="Pclass", y="Fare", color="Survived",
            title='Distribución de Tarifas por Clase')
```

#### 🔢 **Contador Interactivo**
- **Session State**: Persistencia de datos entre interacciones
- **Botones de Control**: Incrementar, decrementar, resetear
- **Estado Global**: Demostración de manejo de estado en Streamlit

### 📑 **4. Análisis y Conclusiones**
- **Insights Clave**: Hallazgos principales del análisis
- **Patrones Identificados**: Factores de supervivencia
- **Cards Informativos**: Presentación visual de conclusiones

---

## 🚀 Instalación y Configuración

### 📋 **Prerrequisitos**
- Python 3.8 o superior
- pip o conda package manager
- 4GB RAM mínimo
- Navegador web moderno

### ⚡ **Instalación Rápida**

#### 1️⃣ **Clonar el Repositorio**
```bash
git clone https://github.com/AlfonsoCifuentes/streamlit_alumnos.git
cd streamlit_alumnos
```

#### 2️⃣ **Crear Entorno Virtual**
```bash
# Con venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Con conda
conda create -n streamlit-titanic python=3.9
conda activate streamlit-titanic
```

#### 3️⃣ **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

#### 4️⃣ **Ejecutar la Aplicación**
```bash
streamlit run app.py
```

#### 5️⃣ **Acceder al Dashboard**
- Abrir navegador en: `http://localhost:8501`
- La aplicación se recarga automáticamente al hacer cambios

### 🐳 **Docker (Opcional)**

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 📊 Guía de Uso

### 🧭 **Navegación Principal**

1. **🚢 Sidebar de Navegación**
   - Acceso rápido a todas las secciones
   - Diseño visual con gradientes temáticos
   - Filtros dinámicos (en desarrollo)

2. **📊 Resumen**
   - KPIs principales en cards visuales
   - Imagen histórica del Titanic
   - Contexto y objetivos del análisis

3. **📋 Datos**
   - Exploración completa del dataset
   - Estadísticas descriptivas automáticas
   - Validación y calidad de datos

4. **📈 Gráficos**
   - 4 pestañas con visualizaciones distintas
   - Gráficos interactivos con Plotly
   - Contador de estado para demostración

5. **📑 Análisis**
   - Conclusiones principales
   - Insights basados en datos
   - Recomendaciones educativas

### 🎛️ **Características Avanzadas**

#### 📱 **Diseño Responsive**
```python
# Layout adaptativo con columnas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pasajeros", "891", "100%")
```

#### 🎨 **Estilo Personalizado**
```css
.main {
    background-color: #fafafa;
}
h1 {
    background: linear-gradient(90deg, #1a237e 0%, #3949ab 100%);
    color: white;
    text-align: center;
}
```

#### 🔧 **Session State**
```python
# Persistencia de datos entre interacciones
if 'contador' not in st.session_state:
    st.session_state.contador = 0

def incrementa_contador():
    st.session_state.contador += 1
```

---

## 📈 Análisis y Hallazgos

### 🔍 **Insights Principales**

#### 💡 **Factores de Supervivencia**
1. **Género**: Las mujeres tuvieron una tasa de supervivencia significativamente mayor
2. **Clase Social**: Los pasajeros de primera clase tuvieron mejores oportunidades
3. **Edad**: Los niños recibieron prioridad en el proceso de evacuación
4. **Ubicación**: La cabina y el puerto de embarque influyeron en las posibilidades

#### 📊 **Estadísticas Clave**
```python
# Métricas principales
Total_Pasajeros = 891
Supervivientes = 342  # 38.4%
Edad_Media = 29.7
Tarifa_Promedio = 32.2
```

#### 🎯 **Patrones Identificados**
- **Protocolo "Mujeres y niños primero"**: Claramente visible en los datos
- **Desigualdad socioeconómica**: La clase del boleto correlaciona con supervivencia
- **Factor familiar**: Viajar en familia afectó las decisiones de evacuación
- **Geografia del desastre**: La ubicación en el barco fue determinante

### 📋 **Distribuciones Importantes**

#### 👥 **Por Género**
- Hombres: 577 (64.8%) - Supervivencia: 18.9%
- Mujeres: 314 (35.2%) - Supervivencia: 74.2%

#### 🚢 **Por Clase**
- Primera Clase: 216 (24.2%) - Supervivencia: 62.9%
- Segunda Clase: 184 (20.7%) - Supervivencia: 47.3%
- Tercera Clase: 491 (55.1%) - Supervivencia: 24.2%

#### 👶 **Por Edad**
- Niños (0-12): Mayor tasa de supervivencia
- Adultos jóvenes (13-30): Tasa variable por género
- Adultos mayores (30+): Menor supervivencia general

---

## 🎓 Valor Educativo

### 📚 **Conceptos Aprendidos**

#### 🐍 **Python & Data Science**
- **Pandas**: Manipulación y análisis de DataFrames
- **Plotly**: Visualizaciones interactivas y responsive
- **Data Cleaning**: Preprocesamiento y validación de datos
- **Statistical Analysis**: Estadísticas descriptivas y correlaciones

#### 🌐 **Web Development**
- **Streamlit Framework**: Desarrollo rápido de aplicaciones web
- **CSS Customization**: Personalización de interfaces
- **Responsive Design**: Layouts adaptativos
- **State Management**: Manejo de estado en aplicaciones web

#### 📊 **Data Visualization**
- **Chart Selection**: Elección apropiada de gráficos
- **Interactive Dashboards**: Dashboards dinámicos y filtros
- **Color Theory**: Paletas de colores efectivas
- **UX/UI Principles**: Principios de experiencia de usuario

### 🎯 **Casos de Uso Educativo**

1. **Bootcamps de Data Science**
   - Proyecto final de análisis de datos
   - Demostración de habilidades técnicas
   - Portfolio development

2. **Cursos Universitarios**
   - Estadística aplicada
   - Programación en Python
   - Visualización de datos

3. **Workshops Corporativos**
   - Introducción a herramientas de BI
   - Desarrollo de dashboards
   - Democratización de datos

---

## 🔧 Personalización y Extensiones

### 🎨 **Customización Visual**

#### 🌈 **Paleta de Colores**
```css
/* Colores principales del tema Titanic */
:root {
    --primary-blue: #1a237e;
    --secondary-blue: #3949ab;
    --accent-color: #e8eaf6;
    --text-dark: #283593;
    --background: #fafafa;
}
```

#### 📱 **Layouts Alternativos**
```python
# Wide layout para dashboards complejos
st.set_page_config(layout="wide")

# Sidebar personalizada
with st.sidebar:
    st.selectbox("Filtro por clase", options=[1, 2, 3])
    st.slider("Rango de edad", 0, 100, (0, 100))
```

### 🔌 **Extensiones Posibles**

#### 📊 **Análisis Avanzado**
- **Machine Learning**: Modelos predictivos de supervivencia
- **Statistical Tests**: Pruebas de hipótesis automatizadas
- **Time Series**: Análisis temporal si se añaden datos temporales
- **Clustering**: Segmentación de pasajeros por perfiles

#### 🌐 **Integración Externa**
- **Database Connectivity**: PostgreSQL, MongoDB
- **API Integration**: APIs de datos históricos
- **Cloud Deployment**: Heroku, Streamlit Cloud, AWS
- **Authentication**: Sistema de usuarios y roles

#### 📱 **Funcionalidades Adicionales**
```python
# Exportación de reportes
@st.cache_data
def generate_report():
    return df.to_csv(index=False)

# Filtros avanzados
def apply_filters(df, filters):
    return df.query(filters)

# Comparaciones entre grupos
def compare_survival_rates(df, group_by):
    return df.groupby(group_by)['Survived'].mean()
```

---

## 📁 Estructura del Proyecto

```
streamlit_alumnos/
├── 📱 app.py                      # Aplicación principal
├── 📊 titanic_limpio.csv          # Dataset preprocesado
├── 📋 requirements.txt            # Dependencias Python
├── 📖 README.md                   # Documentación
├── 🐳 .devcontainer/              # Configuración desarrollo
│   └── devcontainer.json
├── 🔧 .gitattributes              # Configuración Git
├── 📁 assets/                     # Recursos estáticos (futuro)
│   ├── images/
│   ├── styles/
│   └── data/
├── 📊 notebooks/                  # Jupyter notebooks (futuro)
│   ├── data_exploration.ipynb
│   └── model_development.ipynb
├── 🧪 tests/                      # Tests unitarios (futuro)
│   ├── test_data_processing.py
│   └── test_visualizations.py
└── 📚 docs/                       # Documentación adicional
    ├── deployment.md
    └── contributing.md
```

---

## 🚀 Deployment

### ☁️ **Streamlit Cloud (Recomendado)**

1. **Conectar Repositorio**
   ```bash
   # Push al repositorio GitHub
   git push origin main
   ```

2. **Configurar en Streamlit Cloud**
   - Visitar [share.streamlit.io](https://share.streamlit.io)
   - Conectar repositorio GitHub
   - Especificar `app.py` como entrypoint

3. **Variables de Entorno**
   ```toml
   # .streamlit/secrets.toml
   [database]
   url = "your_database_url"
   ```

### 🐳 **Docker Deployment**

```bash
# Build de la imagen
docker build -t streamlit-titanic .

# Run del contenedor
docker run -p 8501:8501 streamlit-titanic
```

### 🌐 **Heroku Deployment**

```bash
# Archivos necesarios
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile
echo "python-3.9.0" > runtime.txt

# Deploy
heroku create your-app-name
git push heroku main
```

---

## 🤝 Contribución

### 💡 **Cómo Contribuir**

1. **🍴 Fork del Proyecto**
   ```bash
   git clone https://github.com/tu-usuario/streamlit_alumnos.git
   ```

2. **🌿 Crear Rama de Feature**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```

3. **💻 Desarrollar**
   - Seguir convenciones de código PEP 8
   - Añadir documentación inline
   - Incluir tests si es aplicable

4. **📝 Commit Descriptivo**
   ```bash
   git commit -m "feat: añadir filtros avanzados en sidebar"
   ```

5. **🚀 Pull Request**
   - Describir cambios realizados
   - Incluir screenshots si hay cambios visuales
   - Referenciar issues relacionados

### 🎯 **Áreas de Mejora**

- [ ] **🔍 Filtros Dinámicos**: Implementar filtros interactivos en sidebar
- [ ] **🤖 Machine Learning**: Añadir modelos predictivos
- [ ] **📱 PWA**: Convertir en Progressive Web App
- [ ] **🌐 Multiidioma**: Soporte para múltiples idiomas
- [ ] **📊 Más Datasets**: Integrar otros datasets educativos
- [ ] **🔐 Autenticación**: Sistema de usuarios
- [ ] **📈 Analytics**: Tracking de uso y métricas
- [ ] **🧪 Testing**: Suite completa de tests

### 📋 **Guía de Estilo**

```python
# Estructura de funciones
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa el DataFrame del Titanic.
    
    Args:
        df: DataFrame con datos del Titanic
        
    Returns:
        DataFrame procesado
    """
    return df.dropna()

# Comentarios descriptivos
# Cargar y procesar datos del Titanic
@st.cache_data
def load_data():
    return pd.read_csv('titanic_limpio.csv')
```

---

## 📚 Recursos y Referencias

### 📖 **Documentación Oficial**

- [📚 Streamlit Documentation](https://docs.streamlit.io/)
- [🐼 Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [📊 Plotly Python Documentation](https://plotly.com/python/)
- [🐍 Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### 🎓 **Cursos Recomendados**

- [📊 Streamlit for Data Science](https://www.coursera.org/learn/streamlit)
- [📈 Data Visualization with Python](https://www.edx.org/course/data-visualization-python)
- [🧮 Pandas Fundamentals](https://www.datacamp.com/courses/pandas-foundations)
- [📊 Interactive Data Visualization](https://www.udacity.com/course/data-visualization-nanodegree)

### 🔗 **Enlaces Útiles**

- [🏆 Kaggle Titanic Competition](https://www.kaggle.com/c/titanic)
- [📊 Streamlit Gallery](https://streamlit.io/gallery)
- [🎨 Color Palettes for Data Viz](https://colorbrewer2.org/)
- [📈 Chart Chooser](https://extremepresentation.typepad.com/blog/2006/09/choosing_a_good.html)

### 🛠️ **Herramientas Complementarias**

- [🔧 VS Code Streamlit Extension](https://marketplace.visualstudio.com/items?itemName=streamlit.streamlit)
- [🐳 Docker Desktop](https://www.docker.com/products/docker-desktop)
- [☁️ Streamlit Cloud](https://streamlit.io/cloud)
- [📊 Observable](https://observablehq.com/) (para prototipos rápidos)

---

## 🏆 Reconocimientos

### 🙏 **Agradecimientos**

- **📊 Kaggle Community** - Por proporcionar el dataset del Titanic
- **🚀 Streamlit Team** - Por crear esta increíble herramienta
- **👨‍🎓 Comunidad Educativa** - Por feedback y mejoras continuas
- **📚 Open Source Contributors** - Por las bibliotecas utilizadas

### 🌟 **Inspiración**

> *"El análisis de datos es como ser detective en un mundo de números"*
> 
> **— Sherlock Holmes (versión data scientist)**

> *"La visualización nos da respuestas a preguntas que no sabíamos que teníamos"*
> 
> **— Ben Schneiderman**

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 Alfonso Cifuentes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 📊 Estadísticas del Proyecto

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/AlfonsoCifuentes/streamlit_alumnos?style=social)
![GitHub forks](https://img.shields.io/github/forks/AlfonsoCifuentes/streamlit_alumnos?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/AlfonsoCifuentes/streamlit_alumnos?style=social)

![GitHub last commit](https://img.shields.io/github/last-commit/AlfonsoCifuentes/streamlit_alumnos)
![GitHub issues](https://img.shields.io/github/issues/AlfonsoCifuentes/streamlit_alumnos)
![GitHub pull requests](https://img.shields.io/github/issues-pr/AlfonsoCifuentes/streamlit_alumnos)

**🚢 Desarrollado con ❤️ para la educación en Data Science**

</div>

---

<div align="center">

**¿Te gustó este proyecto? ¡Dale una ⭐ y compártelo!**

[⬆️ Volver al inicio](#-streamlit-titanic-analysis-dashboard)

</div>
