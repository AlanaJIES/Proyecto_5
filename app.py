#Importamos los paquetes necesarios:
import pandas as pd
import plotly.express as px
import streamlit as st

#Leemos los datos y eliminamos las columnas que no usaremos. 
try:
    car_data = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error(f"Error: No se pudo encontrar el archivo 'vehicles_us.csv' en la ruta actual.")
except pd.errors.EmptyDataError:
    st.error("Error: El archivo 'vehicles_us.csv' está vacío o no es un archivo CSV válido.")

car_data.drop(columns=["date_posted", "days_listed"], inplace=True)

#Ponemos un Título
st.title('Aplicación del proyecto 5, visualizador de datos de anuncio de ventas de coche')

#Ponemos un header
st.header('Generador de gráficos')

#Mensaje acerca de como usar la aplicación.
st.write('Usando esta aplicación se podrán observar algunos de los datos de la tabla ya sea en un histograma, gráfico de dispersión y/o burbujas.')

st.divider()
#Mensaje acerca de la tabla
st.write('Tabla con la  información del conjunto de datos de anuncio de ventas de coches')
st.dataframe(car_data)

st.divider()
st.header('Gráficos')

st.subheader('Histograma')
#Histograma
st.write("Usando el siguiente botón podemos construir un histograma para observar la relación entre el precio y el tipo de vehículo.")
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Podemos identificar por coloración de acuerdo a la transmisión de los vehículos.')
    # crear un histograma
    fig = px.histogram(car_data, x="type", y= "price", color="transmission")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.subheader('Gráfico de Burbujas')
#Gráfico de burbujas
st.write('Haciendo click en el siguiente botón se generará gráfico de dispersión interactivo que proporciona información visual sobre la relación entre la cantidad de millas recorridas, el año del modelo, el precio, el tipo de vehículo y el nombre del modelo para los anuncios de ventas de coches.')
bubble_button = st.button('Construir gráfico de burbuja') # Construyendo botón para el gráfico de burbuja.
if bubble_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('En esta gráfica usamos la combinación de color (el tipo de coche), tamaño (el precio) y posición de las burbujas (con la medición del millaje y el año del modelo) para ayudar a visualizar patrones y tendencias en los datos.')
    # crear un histograma
    fig_2 = px.scatter(car_data, x="odometer", y="model_year", size="price", color="type", hover_name="model", size_max=55)
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)

st.subheader('Gráfico de Dispersión')
#Gráfico de dispersión
st.write('Eligiendo en la siguiente casilla de verificación se creará un gráfico de dispersión para mostrar la relacion entre el precio de un vehiculo con respecto al odómetro y su condición.')
scatter_box = st.checkbox('Construir gráfico de dispersión') # crear un botón
if scatter_box: # al hacer clic en el la casilla de verificación.
    # escribir un mensaje
    st.write('Observamos que las condiciones van desde nuevo ("new"), pasando por justo ("fair"), hasta llegar a siniestro total ("salvage"). Carvana compra los coches en condición de "salvage" en 300 dólares. ¿Puedes ver en cuanto se venden estos coches?')
    # crear un histograma
    fig_3 = px.scatter(car_data, x="odometer", y="price", color="condition") # crear un gráfico de dispersión
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_3, use_container_width=True)