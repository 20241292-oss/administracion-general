
import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACION
st.set_page_config(
    page_title="Dashboard Empresarial",
    layout="wide"
)

# TITULO
st.title("📊 Dashboard Empresarial de Ventas y Finanzas")

st.markdown("### Análisis financiero y administrativo")

# DATOS
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
    "Ventas": [12000, 15000, 18000, 17000, 21000],
    "Gastos": [8000, 9000, 10000, 9500, 11000]
}

df = pd.DataFrame(data)

# UTILIDAD
df["Utilidad"] = df["Ventas"] - df["Gastos"]

# KPIs
ventas_totales = df["Ventas"].sum()
gastos_totales = df["Gastos"].sum()
utilidad_total = df["Utilidad"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Ventas Totales", f"S/ {ventas_totales}")
col2.metric("💸 Gastos Totales", f"S/ {gastos_totales}")
col3.metric("📈 Utilidad Total", f"S/ {utilidad_total}")

st.divider()

# GRAFICOS
col4, col5 = st.columns(2)

with col4:
    fig1 = px.line(
        df,
        x="Mes",
        y=["Ventas", "Gastos", "Utilidad"],
        title="Evolución Financiera",
        markers=True
    )

    fig1.update_layout(template="plotly_dark")

    st.plotly_chart(fig1, use_container_width=True)

with col5:
    fig2 = px.bar(
        df,
        x="Mes",
        y="Ventas",
        title="Ventas Mensuales",
        text_auto=True
    )

    fig2.update_layout(template="plotly_dark")

    st.plotly_chart(fig2, use_container_width=True)

# GRAFICO CIRCULAR
areas = {
    "Area": ["Marketing", "RRHH", "Operaciones", "Logística"],
    "Gastos": [3000, 2000, 4000, 2500]
}

df2 = pd.DataFrame(areas)

fig3 = px.pie(
    df2,
    names="Area",
    values="Gastos",
    title="Distribución de Gastos"
)

fig3.update_layout(template="plotly_dark")

st.plotly_chart(fig3, use_container_width=True)

# CONCLUSIONES
st.subheader("📌 Conclusiones")

st.success("Las ventas muestran crecimiento constante.")
st.success("La empresa mantiene utilidad positiva.")
st.success("Existe estabilidad financiera.")
