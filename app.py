import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header("Cuadro de mandos - Vehículos")


# Casilla 1: Histograma de odómetro
if st.checkbox("Mostrar histograma de Odómetro"):
    fig_hist = px.histogram(df, x="odometer", nbins=30,
                            title="Distribución del Odómetro")
    st.write("Aquí puedes ver cómo se distribuye el odómetro en el dataset:")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla 2: Dispersión Precio vs Odómetro
if st.checkbox("Mostrar dispersión Precio vs Odómetro"):
    df_scatter = df[["price", "odometer"]].dropna()
    fig_scatter = px.scatter(
        df_scatter,
        x="odometer",
        y="price",
        title="Relación entre Odómetro y Precio",
        labels={"odometer": "Odómetro", "price": "Precio"}
    )
    st.write("Gráfico de dispersión entre el odómetro y el precio:")
    st.plotly_chart(fig_scatter, use_container_width=True)
