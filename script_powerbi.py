# Realizamos la carga de datos a power bi
import pandas as pd

base = pd.read_csv(r"C:\Users\matia\OneDrive\Desktop\prueba\Datasets\base.csv")

consigna4 = base[["Provincia  ","1. Variación de la Producción    (diciembre 2018 \nvs. \ndiciembre 2017:)"]].groupby("Provincia  ").mean().round(2).reset_index()
consigna4["1. Variación de la Producción    (diciembre 2018 \nvs. \ndiciembre 2017:)"] =consigna4["1. Variación de la Producción    (diciembre 2018 \nvs. \ndiciembre 2017:)"] / 100
consigna4

delta_por_rubro = base[["RUBRO","1. Variación de la Producción    (diciembre 2018 \nvs. \ndiciembre 2017:)"]].groupby("RUBRO").mean().round(2).reset_index()
delta_por_rubro["1. Variación de la Producción    (diciembre 2018 \nvs. \ndiciembre 2017:)"] = delta_por_rubro["1. Variación de la Producción    (diciembre 2018 \nvs. \ndiciembre 2017:)"] / 100
delta_por_rubro

columnas = base.columns[9:14].tolist()
lista_tablas = []
for elemento in columnas :     
    tabla = base[elemento].value_counts().reset_index()
    tabla["%"] = (tabla["count"] / tabla["count"].sum())
    tabla.loc[len(tabla)] = ["Total",tabla["count"].sum(),tabla["%"].sum()]
    lista_tablas.append(tabla)
df2 = lista_tablas[0]    
df3 = lista_tablas[1]    
df4 = lista_tablas[2]    
df5 = lista_tablas[3]    
df6 = lista_tablas[4]    


aux = ["5- Tiene planeado realizar inversiones en 2019?","6- ¿Cómo evalúa el momento actual para invertir en su empresa?"]
tablas_5_6_rubro = []
for i in aux : 
    x = base[["RUBRO",i]].value_counts().reset_index()
    df_pivot = x.pivot_table(index="RUBRO", columns=[i], values='count', fill_value=0)
    df_pivot["Total"] = df_pivot.sum(axis=1)
    columns = df_pivot.columns[0:]
    for n in columns :
        df_pivot[n] = ((df_pivot[n] / df_pivot["Total"] ) ).round(2)
    tablas_5_6_rubro.append(df_pivot)    
df7 = tablas_5_6_rubro[0].reset_index()
df8 = tablas_5_6_rubro[1].reset_index()    

pregunta7 = base[["RUBRO","7- ¿Con qué porcentaje de su capacidad instalada está produciendo su empresa en la actualidad? "]].groupby("RUBRO").mean().reset_index()
pregunta7["7- ¿Con qué porcentaje de su capacidad instalada está produciendo su empresa en la actualidad? "] = pregunta7["7- ¿Con qué porcentaje de su capacidad instalada está produciendo su empresa en la actualidad? "]/100
pregunta7

pregunta8 = base[["RUBRO","8- Comparando los precios actuales de la economía con los que habrá dentro de un año, es decir, en diciembre de 2019, ¿en qué porcentaje espera que los precios suban en los próximos doce meses?"]].groupby("RUBRO").mean().reset_index()
pregunta8["8- Comparando los precios actuales de la economía con los que habrá dentro de un año, es decir, en diciembre de 2019, ¿en qué porcentaje espera que los precios suban en los próximos doce meses?"] = pregunta8["8- Comparando los precios actuales de la economía con los que habrá dentro de un año, es decir, en diciembre de 2019, ¿en qué porcentaje espera que los precios suban en los próximos doce meses?"] /100
pregunta8

columnas = base.columns[17:22]
listaff = []
for elemento in columnas : 
    df = base[elemento].value_counts().reset_index()
    listaff.append(df)
for elemento in listaff :
    elemento.columns = listaff[0].columns    
df_concat = pd.concat(listaff, ignore_index=True)    
pregunta10 = df_concat.groupby('10- ¿Qué tipo de reformas considera que se deberian implementar para mejorar la situacion de su sector?').sum().sort_values(by="count",ascending=False).reset_index()
pregunta10

empleados_por_rubro = base[["RUBRO","CANTIDAD DE EMPLEADOS DE LA EMPRESA"]].groupby(["RUBRO"]).mean().round(2).reset_index()
empleados_por_rubro = empleados_por_rubro.sort_values(by = "CANTIDAD DE EMPLEADOS DE LA EMPRESA" ,ascending=False)
empleados_por_rubro

rubros = base["RUBRO"].value_counts().reset_index()
rubros