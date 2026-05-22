
import streamlit as st
import pandas as pd
import plotly.express as px

# TITULO
st.title("Dashboard Empresarial de Ventas y Finanzas")

# DATOS
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "Ventas": [12000, 15000, 18000, 17000, 21000],
    "Gastos": [8000, 9000, 10000, 9500, 11000]
}

# DATAFRAME
df = pd.DataFrame(data)

# UTILIDAD
df["Utilidad"] = df["Ventas"] - df["Gastos"]

# KPIs
st.subheader("Indicadores Financieros")

col1, col2, col3 = st.columns(3)

col1.metric("Ventas Totales", f"S/ {df['Ventas'].sum()}")
col2.metric("Gastos Totales", f"S/ {df['Gastos'].sum()}")
col3.metric("Utilidad Total", f"S/ {df['Utilidad'].sum()}")

# GRAFICO LINEAS
fig = px.line(
    df,
    x="Mes",
    y=["Ventas", "Gastos", "Utilidad"],
    title="Evolución Financiera"
)

st.plotly_chart(fig)

# GRAFICO BARRAS
fig2 = px.bar(
    df,
    x="Mes",
    y="Ventas",
    title="Ventas Mensuales",
    text_auto=True
)

st.plotly_chart(fig2)

# CONCLUSIONES
st.subheader("Conclusiones")

st.write("""
- Las ventas muestran crecimiento constante.
- La empresa mantiene utilidad positiva.
- Existe estabilidad financiera.
""")
