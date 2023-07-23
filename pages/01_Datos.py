import streamlit as st
import pandas as pd

# Leemos el archivo
df = pd.read_csv("Datasets/base.csv")
# Hacemos unas últimas transformaciones

# Título de la página
st.title("Tablas de datos")
st.write("---")

# Visualización de la tabla
st.subheader("Base general")
st.dataframe(df)

# Dimensión a mostrar (Filas o Columnas)
dim = st.radio("Dimensión a mostrar:", ("Filas", "Columnas"), index=0)

if dim == "Filas":
    st.write(f"Cantidad de registros: {df.shape[0]}")
else:
    st.write(f"Cantidad de columnas: {df.shape[1]}")

st.write("---")

# Vista de datos (Head o Tail)
st.subheader("Vista de datos")

show_head = st.checkbox("Mostrar primeros 5 registros")
show_tail = st.checkbox("Mostrar últimos 5 registros")

if show_head:
    st.write("primeros 5 registros:")
    st.dataframe(df.head())

if show_tail:
    st.write("últimos 5 registros:")
    st.dataframe(df.tail())

st.write("---")

# Filtrado por provincia
provincias = sorted(df["Provincia  "].unique().tolist())
selected_provincia = st.selectbox("Filtrar por provincia:", provincias)
df_filtered = df[df["Provincia  "] == selected_provincia]

st.subheader("Datos filtrados por provincia")
st.dataframe(df_filtered)

st.write("---")

# Filtrado por rubro
rubros = sorted(df["RUBRO"].unique().tolist())
selected_rubro = st.selectbox("Filtrar por rubro:", rubros)
df_filtered_rubro = df[df["RUBRO"] == selected_rubro]

st.subheader("Datos filtrados por rubro")
st.dataframe(df_filtered_rubro)

st.write("---")



