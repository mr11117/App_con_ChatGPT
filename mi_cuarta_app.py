import streamlit as st

# Título de la aplicación
st.title("Cálculo del P.A.P.A. (Promedio Acumulado Ponderado Académico)")

st.write("Autor: Esta app fue elaborada por MIGUEL ANGEL RAMIREZ GAVIRIA")

# Descripción
st.write("Esta aplicación permite calcular el P.A.P.A. ingresando las notas y los créditos de cada asignatura.")

# Entrada de datos para las asignaturas
st.write("### Ingrese los datos de las asignaturas")
num_asignaturas = st.number_input("Número de asignaturas:", min_value=1, step=1)

# Crear listas para almacenar créditos y notas
creditos = []
notas = []

# Obtener los datos de las asignaturas
for i in range(num_asignaturas):
    st.write(f"#### Asignatura {i + 1}")
    credito = st.number_input(f"Créditos de la asignatura {i + 1}:", min_value=0, step=1, key=f"credito_{i}")
    nota = st.number_input(f"Nota de la asignatura {i + 1} (0.0 - 5.0):", min_value=0.0, max_value=5.0, step=0.1, key=f"nota_{i}")
    creditos.append(credito)
    notas.append(nota)

# Calcular el P.A.P.A. cuando se presiona el botón
if st.button("Calcular P.A.P.A."):
    if sum(creditos) > 0:  # Evitar división por cero
        papa = sum(c * n for c, n in zip(creditos, notas)) / sum(creditos)
        st.success(f"El P.A.P.A. calculado es: {papa:.2f}")
    else:
        st.error("El total de créditos no puede ser 0. Verifique los datos ingresados.")
