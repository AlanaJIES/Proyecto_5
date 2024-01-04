# # Proyecto_5
# El código construye una aplicación web utilizando Streamlit para visualizar y explorar datos de anuncios de ventas de coches. 
#Proporciona una interfaz interactiva con gráficos visuales y controles para personalizar la experiencia del usuario. 
#Además, maneja posibles errores al cargar el archivo de datos. Aquí esta la URL de la aplicación en Render: https://proyecto-5-zli7.onrender.com

# 1.-Importación de Librerías:
## Se importan las librerías necesarias, incluyendo pandas para el manejo de datos, plotly.express para la creación de gráficos y 
## streamlit para la creación de la aplicación web.

# 2.- Lectura de Datos:
## Lee un archivo CSV llamado 'vehicles_us.csv' y lo llama "car_data".
## Maneja excepciones en caso de que el archivo no se encuentre o esté vacío.

# 3.-Preprocesamiento de Datos:
## Elimina las columnas "date_posted" y "days_listed" del DataFrame car_data.

# 4.-Diseño de la Interfaz:
## Utiliza Streamlit para diseñar la interfaz de la aplicación web.
## Incluye títulos y encabezados descriptivos para las secciones.
## Muestra un mensaje de construcción y una tabla con la información del conjunto de datos.

# 5.-Gráficos Interactivos:
## Proporciona botones y controles para construir diferentes tipos de gráficos interactivos.
## Incluye un histograma, un gráfico de burbujas y un gráfico de dispersión.
## Cada gráfico se construye al hacer clic en un botón o seleccionar una casilla de verificación.

# 6.-Descripciones y Mensajes:
## Incluye mensajes descriptivos sobre el propósito de cada sección y gráfico.
## Proporciona información sobre cómo usar la aplicación y qué esperar de cada gráfico.
