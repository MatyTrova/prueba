import streamlit as st

st.set_page_config(
    page_title="Prueba técnica - Matias Trovatto",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="expanded"
    )

# Título de la página
st.title("**Prueba Técnica - Dashboard**")

# Imagen
st.image("imgs/LOGO-CAME.jpg", use_column_width=True)
# Línea divisoria
st.markdown("---")
# Encabezado
st.header("¡Bienvenido, Claudio!")

# Texto descriptivo
st.write("Te doy la bienvenida a mi **Dashboard** de la prueba técnica, una aplicación interactiva diseñada para visualizar los datos sobre el estado actual de las pymes del país en diciembre de 2019")

# Sección de información
st.subheader("¿Qué puedes encontrar aquí?")
st.write("En esta aplicación, descubrirás dos secciones:")
st.write("+ **Datos**: Visualiza tablas de datos completas y actualizadas.")
st.write("+ **Visualizaciones**: Explora gráficos interactivos para comprender fácilmente el comportamiento de los datos.")

# Línea divisoria
st.markdown("---")

# Créditos
st.text("Desarrollado por: Matias Trovatto")
