# Librerias a utilizar
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Carga de datos
df = pd.read_csv("Datasets/base.csv")

# Presentación
st.write("---")
st.write("# *Análisis de las preguntas de las encuestas*")
st.write("---")
st.write("")

preguntas = df.columns[9:14].tolist()
preguntas.append('10- ¿Qué tipo de reformas considera que se deberian implementar para mejorar la situacion de su sector?')
selected_pregunta = st.selectbox('Selecciona un una pregunta:', preguntas)
col1, col2 = st.columns(2)
with col1 :
# Selección de la pregunta
    
    if (selected_pregunta == '10- ¿Qué tipo de reformas considera que se deberian implementar para mejorar la situacion de su sector?') :
        columnas = df.columns[17:22]
        listaff = []
        for elemento in columnas : 
            df_columnas = df[elemento].value_counts().reset_index()
            listaff.append(df)
        for elemento in listaff :
            elemento.columns = listaff[0].columns    
        df_concat = pd.concat(listaff, ignore_index=True)    
        tabla = df_concat.groupby('10- ¿Qué tipo de reformas considera que se deberian implementar para mejorar la situacion de su sector?').sum().sort_values(by="count",ascending=False).reset_index()
        tabla2 = tabla = df_concat.groupby('10- ¿Qué tipo de reformas considera que se deberian implementar para mejorar la situacion de su sector?').sum().sort_values(by="count",ascending=False)
        tabla["%"] = (tabla["count"] / tabla["count"].sum()) * 100
        plt.figure(figsize=(10, 8))
        plt.grid(True)
        sns.set(style='whitegrid', font_scale=1.2, rc={"figure.figsize":(8,6)})
        # Creamos un grafico de barras horizontal
        ax = sns.barplot(x=selected_pregunta, y='%', data=tabla)
        # Añadimos las etiquetas y el título
        ax.set_ylabel('Porcentaje %',fontsize=12)
        ax.set_xlabel('')
        ax.set_title(selected_pregunta, fontsize=14)
        # Mostrar el gráfico
        gráfico = plt.gcf()
        st.pyplot(gráfico)

    else:
        tabla = df[selected_pregunta].value_counts().reset_index()
        tabla["%"] = (tabla["count"] / tabla["count"].sum()) * 100
        plt.figure(figsize=(8, 8))
        plt.grid(True)
        sns.set(style='whitegrid', font_scale=1.2, rc={"figure.figsize":(8,6)})
        # Creamos un grafico de barras horizontal
        ax = sns.barplot(x=selected_pregunta, y='%', data=tabla)
        # Añadimos las etiquetas y el título
        ax.set_ylabel('Porcentaje %',fontsize=12)
        ax.set_xlabel('')
            # Mostrar el gráfico
        gráfico = plt.gcf()
        st.pyplot(gráfico)

with col2 :
    tabla2 = tabla
    tabla2.rename(columns= {selected_pregunta : "categoria"},inplace=True)
    tabla2.set_index('categoria', inplace=True)
    st.dataframe(tabla2)


# Presentación 2do gráfico
st.write("# *Análisis de preguntas por rubro*")
st.write("---")

# Selección de país
seleccione_pregunta = ["5- Tiene planeado realizar inversiones en 2019?","6- ¿Cómo evalúa el momento actual para invertir en su empresa?",
                       "7- ¿Con qué porcentaje de su capacidad instalada está produciendo su empresa en la actualidad? ",
                       "8- Comparando los precios actuales de la economía con los que habrá dentro de un año, es decir, en diciembre de 2019, ¿en qué porcentaje espera que los precios suban en los próximos doce meses?"]
pregunta_seleccionada = st.selectbox("Selecciona una pregunta:", seleccione_pregunta)
if (pregunta_seleccionada == "7- ¿Con qué porcentaje de su capacidad instalada está produciendo su empresa en la actualidad? "):
    pregunta7 = df[["RUBRO","7- ¿Con qué porcentaje de su capacidad instalada está produciendo su empresa en la actualidad? "]].groupby("RUBRO").mean().reset_index()
    plt.figure(figsize=(10, 8))
    plt.grid(True)
    sns.set(style='whitegrid', font_scale=1.2, rc={"figure.figsize":(8,6)})
    # Creamos un grafico de barras horizontal
    ax = sns.barplot(x="%", y="RUBRO" ,data = pregunta7)
    # Añadimos las etiquetas y el título
    ax.set_xlabel('Porcentaje %',fontsize=12)
    ax.set_ylabel('')
    ax.set_title(pregunta_seleccionada, fontsize=14)
            # Mostrar el gráfico
    gráfico3 = plt.gcf()
    st.pyplot(gráfico3)

if (pregunta_seleccionada == "8- Comparando los precios actuales de la economía con los que habrá dentro de un año, es decir, en diciembre de 2019, ¿en qué porcentaje espera que los precios suban en los próximos doce meses?"):   
    pregunta8 = df[["RUBRO","8- Comparando los precios actuales de la economía con los que habrá dentro de un año, es decir, en diciembre de 2019, ¿en qué porcentaje espera que los precios suban en los próximos doce meses?"]].groupby("RUBRO").mean().reset_index()
    plt.figure(figsize=(10, 8))
    plt.grid(True)
    sns.set(style='whitegrid', font_scale=1.2, rc={"figure.figsize":(8,6)})
    # Creamos un grafico de barras horizontal
    ax = sns.barplot(x="%", y="RUBRO" ,data = pregunta8)
    # Añadimos las etiquetas y el título
    ax.set_xlabel('Porcentaje %',fontsize=12)
    ax.set_ylabel('')
    ax.set_title(pregunta_seleccionada, fontsize=14)
            # Mostrar el gráfico
    gráfico3 = plt.gcf()
    st.pyplot(gráfico3)
else:
    x = df[["RUBRO",pregunta_seleccionada]].value_counts().reset_index()
    df_pivot = x.pivot_table(index="RUBRO", columns=[pregunta_seleccionada], values='count', fill_value=0)
    df_pivot["Total"] = df_pivot.sum(axis=1)
    columns = df_pivot.columns[0:]
    for n in columns :
        df_pivot[n] = ((df_pivot[n] / df_pivot["Total"] ) ).round(2)
    df_pivot.pop("total")  
    df_pivot = df_pivot.reset_index()
    plt.figure(figsize=(10, 8))
    plt.grid(True)
    sns.set(style='whitegrid', font_scale=1.2, rc={"figure.figsize":(8,6)})
    ax = sns.barplot(x="Lo estoy evaluando", y="RUBRO", data=df_pivot, color="tab:orange", label="Lo estoy evaluando")
    ax = sns.barplot(x="NS/NC", y="RUBRO", data=df_pivot, color="tab:orange", label="NS/NC")
    ax = sns.barplot(x="No", y="RUBRO", data=df_pivot, color="tab:blue", label="No", left=df_pivot["NS/NC"])
    ax = sns.barplot(x="Si", y="RUBRO", data=df_pivot, color="tab:green", label="Si", left=df_pivot["NS/NC"] + df_pivot["No"])
    # Configuar etiquetas y leyenda
    plt.legend(title="Respuestas", bbox_to_anchor=(1.05, 1), loc='upper left')
    # Etiquetas de los ejes y título
    plt.xlabel("Porcentaje")
    plt.ylabel("")
    plt.title(pregunta_seleccionada, fontsize=14)
    # Mostrar el gráfico
    plt.tight_layout()
    gráfico2 = plt.gcf()
    st.pyplot(gráfico2)
