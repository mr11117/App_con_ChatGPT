import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la app
st.title('Control de Finanzas Personales')
st.sidebar.header('Menú de navegación')

# Cargar los datos
if 'datos' not in st.session_state:
    st.session_state.datos = pd.DataFrame(columns=['Fecha', 'Categoría', 'Tipo', 'Monto', 'Descripción'])

# Función para agregar una transacción
def agregar_transaccion(fecha, categoria, tipo, monto, descripcion):
    nueva_transaccion = pd.DataFrame({
        'Fecha': [fecha],
        'Categoría': [categoria],
        'Tipo': [tipo],
        'Monto': [monto],
        'Descripción': [descripcion]
    })
    st.session_state.datos = pd.concat([st.session_state.datos, nueva_transaccion], ignore_index=True)

# Sección para agregar ingresos y gastos
st.sidebar.subheader('Registrar una transacción')
fecha = st.sidebar.date_input('Fecha', min_value=datetime(2020, 1, 1), value=datetime.today())
categoria = st.sidebar.selectbox('Categoría', ['Alquiler', 'Alimentación', 'Transporte', 'Ocio', 'Otros'])
tipo = st.sidebar.selectbox('Tipo de transacción', ['Ingreso', 'Gasto'])
monto = st.sidebar.number_input('Monto', min_value=0.01, step=0.01, value=0.0)
descripcion = st.sidebar.text_input('Descripción', value='')

# Botón para agregar la transacción
if st.sidebar.button('Agregar transacción'):
    if monto > 0 and descripcion != '':
        agregar_transaccion(fecha, categoria, tipo, monto, descripcion)
        st.sidebar.success('Transacción agregada exitosamente!')
    else:
        st.sidebar.error('Por favor complete todos los campos correctamente.')

# Mostrar el registro de transacciones
st.subheader('Registro de transacciones')
st.dataframe(st.session_state.datos)

# Funciones para calcular las diferencias entre presupuestos y lo real
def reporte_diferencias(periodo='mensual'):
    # Convertir la columna 'Fecha' a tipo datetime
    st.session_state.datos['Fecha'] = pd.to_datetime(st.session_state.datos['Fecha'])
    
    # Filtrar por el periodo (mensual o semanal)
    if periodo == 'mensual':
        st.session_state.datos['Mes'] = st.session_state.datos['Fecha'].dt.month
        st.session_state.datos['Año'] = st.session_state.datos['Fecha'].dt.year
        periodo_actual = st.session_state.datos.groupby(['Año', 'Mes', 'Categoría', 'Tipo'])['Monto'].sum().reset_index()
    elif periodo == 'semanal':
        st.session_state.datos['Semana'] = st.session_state.datos['Fecha'].dt.isocalendar().week
        st.session_state.datos['Año'] = st.session_state.datos['Fecha'].dt.year
        periodo_actual = st.session_state.datos.groupby(['Año', 'Semana', 'Categoría', 'Tipo'])['Monto'].sum().reset_index()
    
    # Mostrar el reporte
    st.subheader(f'Reporte de {periodo} - Diferencias Presupuesto vs Real')
    st.dataframe(periodo_actual)

# Mostrar los reportes
st.sidebar.subheader('Generar reporte')
periodo = st.sidebar.radio('Selecciona el periodo', ['mensual', 'semanal'])
if st.sidebar.button(f'Reporte {periodo}'):
    reporte_diferencias(periodo)

# Meta de ahorro
st.sidebar.subheader('Metas de Ahorro')
meta_ahorro = st.sidebar.number_input('Meta de ahorro para este mes', min_value=0.0, value=0.0, step=0.01)
ahorrado = st.sidebar.number_input('Ahorro realizado hasta ahora', min_value=0.0, value=0.0, step=0.01)

# Calcular el progreso hacia la meta de ahorro
progreso = (ahorrado / meta_ahorro) * 100 if meta_ahorro > 0 else 0
st.sidebar.write(f'Progreso hacia la meta de ahorro: {progreso:.2f}%')

# Gráfico de progreso
st.sidebar.progress(progreso)


st.write(f"Meta de ahorro: {meta_ahorro}")
st.write(f"Diferencia con la meta de ahorro: {ahorro_real - meta_ahorro}")

