import streamlit as st

st.set_page_config(
    page_title="Prueba técnica - Matias Trovatto",
    page_icon="📊",
    layout="centred",
    initial_sidebar_state="expanded"
    )

# Título de la página
st.title("**Prueba Técnica - Dashboard**")

# Imagen
#st.image("ruta/a/tu/imagen.jpg", caption="Imagen de ejemplo", use_column_width=True)
# Línea divisoria
st.markdown("---")
# Encabezado
st.header("Bienvenido Claudio :)")

# Texto descriptivo
st.write("Bienvenido al **Dashboard** de la prueba técnica, una aplicación interactiva diseñada para visualizar los datos sobre el estado actual de las pymes del país en diciembre de 2019")

# Sección de información
st.subheader("¿Qué puedes encontrar aquí?")
st.write("En esta aplicación, podrás descubrir una dos secciones para el análisis y descubrimiento:")
st.write("+ **Datos**: Explora una visualización completa y actualizada de los datos recopilados.")
st.write("+ **Visualizaciones**: Explora gráficos interactivos y descubre de manera sencilla como se comportan los datos")

# Línea divisoria
st.markdown("---")

# Créditos
st.text("Desarrollado por: Matias Trovatto")
