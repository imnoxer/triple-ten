import pandas as pd
import plotly.express as px
import streamlit as st

data_file = 'vehicles_us.csv'
df = pd.read_csv(data_file)

st.header("Cuadro de mandos de anuncios de venta de coches")

show_histogram = st.checkbox("Construir histograma")
show_scatter = st.checkbox("Construir Gráfico de Dispersión")


if show_histogram:
    st.write("Histograma para la columna 'odometer'")
    fig_hist = px.histogram(df, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

if show_scatter:
    st.write("Gráfico de dispersión: Precio vs. Odómetro")
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs. Odómetro", trendline="ols")
    st.plotly_chart(fig_scatter, use_container_width=True)
