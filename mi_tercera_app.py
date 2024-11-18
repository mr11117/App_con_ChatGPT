import streamlit as st
import pandas as pd
import datetime

# Título de la app
st.title("Registro de Finanzas Personales")

# Autor de la app
st.write("Autor: Esta app fue elaborada por MIGUEL ANGEL RAMIREZ GAVIRIA")

# Cargar datos: En este caso, simularemos la base de datos con pandas DataFrame
# Puedes modificar este código para integrarlo con una base de datos real
if 'finanzas' not in st.session_state:
    st.session_state.finanzas = pd.DataFrame(columns=["Fecha", "Categoría", "Descripción", "Monto", "Tipo"])

# Función para agregar un nuevo registro de ingreso/gasto
st.subheader("Registrar Ingreso/Gasto")

categoria = st.selectbox("Selecciona la categoría:", ["Ingreso", "Gasto"])
descripcion = st.text_input("Descripción del registro")
monto = st.number_input("Monto", min_value=0.0, step=0.01)

tipo = "Ingreso" if categoria == "Ingreso" else "Gasto"
fecha = st.date_input("Fecha", datetime.date.today())

# Agregar al DataFrame
if st.button("Registrar"):
    nuevo_registro = {
        "Fecha": fecha,
        "Categoría": categoria,
        "Descripción": descripcion,
        "Monto": monto,
        "Tipo": tipo
    }
    st.session_state.finanzas = pd.concat([st.session_state.finanzas, pd.DataFrame([nuevo_registro])], ignore_index=True)
    st.success(f"{categoria} registrado correctamente.")

# Mostrar los registros
st.subheader("Registros de Ingresos y Gastos")
st.dataframe(st.session_state.finanzas)

# Mostrar resúmenes mensuales y semanales
st.subheader("Reportes de Finanzas")

# Reporte semanal y mensual
fecha_actual = datetime.date.today()

# Filtrar los registros de esta semana y de este mes
finanzas_semanales = st.session_state.finanzas[st.session_state.finanzas["Fecha"] >= (fecha_actual - datetime.timedelta(days=7))]
finanzas_mensuales = st.session_state.finanzas[st.session_state.finanzas["Fecha"].dt.month == fecha_actual.month]

# Calcular la diferencia entre lo presupuestado y lo real
st.subheader("Reporte Semanal")

# Establecer presupuesto para cada categoría
presupuesto_semanal = {
    "Ingreso": 1000,  # Ejemplo de presupuesto semanal de ingresos
    "Gasto": 500,     # Ejemplo de presupuesto semanal de gastos
}

# Cálculo de lo real
ingresos_semanales = finanzas_semanales[finanzas_semanales["Tipo"] == "Ingreso"]["Monto"].sum()
gastos_semanales = finanzas_semanales[finanzas_semanales["Tipo"] == "Gasto"]["Monto"].sum()

# Mostrar el reporte semanal
st.write(f"Ingresos reales en la semana: {ingresos_semanales}")
st.write(f"Gastos reales en la semana: {gastos_semanales}")

st.write(f"Presupuesto de ingresos: {presupuesto_semanal['Ingreso']}")
st.write(f"Presupuesto de gastos: {presupuesto_semanal['Gasto']}")

st.write(f"Diferencia de ingresos: {ingresos_semanales - presupuesto_semanal['Ingreso']}")
st.write(f"Diferencia de gastos: {gastos_semanales - presupuesto_semanal['Gasto']}")

# Reporte mensual
st.subheader("Reporte Mensual")

# Establecer presupuesto mensual
presupuesto_mensual = {
    "Ingreso": 4000,  # Ejemplo de presupuesto mensual de ingresos
    "Gasto": 2000,    # Ejemplo de presupuesto mensual de gastos
}

# Cálculo de lo real
ingresos_mensuales = finanzas_mensuales[finanzas_mensuales["Tipo"] == "Ingreso"]["Monto"].sum()
gastos_mensuales = finanzas_mensuales[finanzas_mensuales["Tipo"] == "Gasto"]["Monto"].sum()

# Mostrar el reporte mensual
st.write(f"Ingresos reales en el mes: {ingresos_mensuales}")
st.write(f"Gastos reales en el mes: {gastos_mensuales}")

st.write(f"Presupuesto de ingresos: {presupuesto_mensual['Ingreso']}")
st.write(f"Presupuesto de gastos: {presupuesto_mensual['Gasto']}")

st.write(f"Diferencia de ingresos: {ingresos_mensuales - presupuesto_mensual['Ingreso']}")
st.write(f"Diferencia de gastos: {gastos_mensuales - presupuesto_mensual['Gasto']}")

# Mostrar las metas de ahorro
st.subheader("Metas de Ahorro")

# Establecer metas de ahorro
meta_ahorro = st.number_input("Meta de ahorro del mes", min_value=0.0, step=0.01)

# Calcular el ahorro real
ahorro_real = ingresos_mensuales - gastos_mensuales

# Mostrar el ahorro
st.write(f"Ahorro real hasta el momento: {ahorro_real}")
st.write(f"Meta de ahorro: {meta_ahorro}")
st.write(f"Diferencia con la meta de ahorro: {ahorro_real - meta_ahorro}")

