# Proyecto TripleTen Sprint 6 por Emilio Molina

Esta aplicación web, desarrollada con Streamlit proporciona una interfaz intuitiva y sencilla para explorar tendencias y relaciones dentro del conjunto de datos cargado.

## Funcionalidades

- **Histograma del Odómetro**: Visualiza la distribución de los valores del odómetro en los vehículos anunciados.
- **Gráfico de Dispersión**: Muestra la relación entre el precio y el odómetro de los vehículos, incluyendo una línea de tendencia.

## Requisitos del Proyecto

- **Python**: Lenguaje de programación principal.
- **Bibliotecas Utilizadas**:
  - `streamlit`: Para crear la aplicación web interactiva.
  - `pandas`: Para manipulación y análisis de datos.
  - `plotly.express`: Para generar gráficos interactivos.

## Cómo Ejecutar la Aplicación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. Instala las dependencias necesarias con:
   ```
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación con el comando:
   ```
   streamlit run app.py
   ```

## Despliegue en Render

Para hacer compatible la aplicación con Render, se incluye un archivo de configuración en `streamlit/config.toml` con los parámetros necesarios.

## Repositorio Github

https://github.com/imnoxer/triple-ten

## Enlace de Render

https://triple-ten.onrender.com/
