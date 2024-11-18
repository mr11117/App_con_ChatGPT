import streamlit as st

# Título de la aplicación
st.title("Escalas Musicales")

# Descripción
st.write("PROGRAMA ELABORADO POR MIGUEL ANGEL RAMIREZ")
st.write("Esta aplicación muestra las notas que componen distintas escalas musicales a partir de una nota base seleccionada.")

# Notas musicales
notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Escalas y sus patrones (en semitonos)
escalas = {
    "Mayor": [2, 2, 1, 2, 2, 2, 1],
    "Menor Natural": [2, 1, 2, 2, 1, 2, 2],
    "Pentatónica Mayor": [2, 2, 3, 2, 3],
    "Pentatónica Menor": [3, 2, 2, 3, 2]
}

# Selección de la nota raíz
nota_base = st.selectbox("Seleccione una nota base:", notas)

# Selección de la escala
escala_seleccionada = st.selectbox("Seleccione una escala:", list(escalas.keys()))

# Mostrar las notas de la escala seleccionada
if st.button("Mostrar escala"):
    indice_base = notas.index(nota_base)
    patron = escalas[escala_seleccionada]
    
    # Generar las notas de la escala
    escala = [nota_base]
    indice_actual = indice_base
    for paso in patron:
        indice_actual = (indice_actual + paso) % len(notas)
        escala.append(notas[indice_actual])
    
    # Mostrar la escala resultante
    st.success(f"La escala {escala_seleccionada} basada en {nota_base} es: {' - '.join(escala)}")
