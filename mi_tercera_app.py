import streamlit as st
import pandas as pd
from datetime import datetime

# Título de la app
st.title("Registro de Finanzas Personales")

# Autor
st.write("Esta app fue elaborada por COLOQUE AQUÍ SU NOMBRE")

# Definir un contenedor para el formulario de entrada
st.header("Registro de Finanzas")

# Ingresar presupuesto mensual
presupuesto_mensual = st.number_input("Presupuesto mensual:", min_value=0, value=2000, step=50)

# Ingresar ingresos
ingreso = st.number_input("Ingreso recibido:", min_value=0, value=1500, step=50)

# Ingresar gastos
gasto = st.number_input("Gasto realizado:", min_value=0, value=500, step=50)

# Ingresar metas de ahorro
meta_ahorro = st.number_input("Meta de ahorro mensual:", min_value=0, value=300, step=50)

# Registrar la fecha actual
fecha_actual = datetime.now().date()

# Almacenar los registros en un DataFrame (para ejemplo)
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=['Fecha', 'Ingreso', 'Gasto', 'Presupuesto', 'MetaAhorro'])

# Botón para agregar datos al registro
if st.button("Registrar transacción"):
    # Agregar nueva fila al DataFrame
    st.session_state.df = st.session_state.df.append({
        'Fecha': fecha_actual,
        'Ingreso': ingreso,
        'Gasto': gasto,
        'Presupuesto': presupuesto_mensual,
        'MetaAhorro': meta_ahorro
    }, ignore_index=True)
    
    st.success("Registro agregado correctamente.")

# Mostrar los registros
st.subheader("Historial de Finanzas")
st.write(st.session_state.df)

# Funciones para calcular diferencias entre lo presupuestado y lo real

# Reporte semanal
st.subheader("Reporte Semanal")
fecha_inicio_semana = fecha_actual - pd.Timedelta(days=7)
df_semanal = st.session_state.df[st.session_state.df['Fecha'] >= fecha_inicio_semana]

total_ingreso_semanal = df_semanal['Ingreso'].sum()
total_gasto_semanal = df_semanal['Gasto'].sum()
total_presupuesto_semanal = df_semanal['Presupuesto'].sum()
total_meta_ahorro_semanal = df_semanal['MetaAhorro'].sum()

diferencia_ingreso_semanal = total_ingreso_semanal - total_presupuesto_semanal
diferencia_gasto_semanal = total_gasto_semanal - total_presupuesto_semanal
diferencia_ahorro_semanal = total_meta_ahorro_semanal - (total_ingreso_semanal - total_gasto_semanal)

st.write(f"Ingreso total esta semana: ${total_ingreso_semanal}")
st.write(f"Gasto total esta semana: ${total_gasto_semanal}")
st.write(f"Presupuesto total esta semana: ${total_presupuesto_semanal}")
st.write(f"Meta de ahorro esta semana: ${total_meta_ahorro_semanal}")

st.write(f"Diferencia de ingreso respecto al presupuesto: ${diferencia_ingreso_semanal}")
st.write(f"Diferencia de gasto respecto al presupuesto: ${diferencia_gasto_semanal}")
st.write(f"Diferencia en ahorro respecto a la meta: ${diferencia_ahorro_semanal}")

# Reporte mensual
st.subheader("Reporte Mensual")
fecha_inicio_mes = datetime(fecha_actual.year, fecha_actual.month, 1).date()
df_mensual = st.session_state.df[st.session_state.df['Fecha'] >= fecha_inicio_mes]

total_ingreso_mensual = df_mensual['Ingreso'].sum()
total_gasto_mensual = df_mensual['Gasto'].sum()
total_presupuesto_mensual = df_mensual['Presupuesto'].sum()
total_meta_ahorro_mensual = df_mensual['MetaAhorro'].sum()

diferencia_ingreso_mensual = total_ingreso_mensual - total_presupuesto_mensual
diferencia_gasto_mensual = total_gasto_mensual - total_presupuesto_mensual
diferencia_ahorro_mensual = total_meta_ahorro_mensual - (total_ingreso_mensual - total_gasto_mensual)

st.write(f"Ingreso total este mes: ${total_ingreso_mensual}")
st.write(f"Gasto total este mes: ${total_gasto_mensual}")
st.write(f"Presupuesto total este mes: ${total_presupuesto_mensual}")
st.write(f"Meta de ahorro este mes: ${total_meta_ahorro_mensual}")

st.write(f"Diferencia de ingreso respecto al presupuesto: ${diferencia_ingreso_mensual}")
st.write(f"Diferencia de gasto respecto al presupuesto: ${diferencia_gasto_mensual}")
st.write(f"Diferencia en ahorro respecto a la meta: ${diferencia_ahorro_mensual}")
