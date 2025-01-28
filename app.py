import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
data_file = 'vehicles_us.csv'
df = pd.read_csv(data_file)

# Título de la aplicación
st.header("Cuadro de mandos de anuncios de venta de coches")

# Casillas de verificación para gráficos
show_histogram = st.checkbox("Mostrar histograma del odómetro")
show_scatter = st.checkbox("Mostrar gráfico de dispersión de precio vs. odómetro")

# Mostrar histograma
if show_histogram:
    st.write("Histograma para la columna 'odometer'")
    fig_hist = px.histogram(df, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Mostrar gráfico de dispersión
if show_scatter:
    st.write("Gráfico de dispersión: Precio vs. Odómetro")
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs. Odómetro", trendline="ols")
    st.plotly_chart(fig_scatter, use_container_width=True)
