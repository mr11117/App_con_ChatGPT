import streamlit as st

# Título de la app
st.title("Conversor Universal de Unidades")

# Autor de la app
st.write("Autor: Esta app fue elaborada por MIGUEL ANGEL RAMIREZ GAVIRIA")

# Selección de categoría
categoria = st.selectbox(
    "Selecciona la categoría de conversión:",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de Datos"
    ]
)

# Conversión según la categoría seleccionada
if categoria == "Temperatura":
    conversion = st.selectbox(
        "Selecciona la conversión de temperatura:",
        [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius",
            "Celsius a Kelvin",
            "Kelvin a Celsius"
        ]
    )
    temperatura = st.number_input("Introduce el valor:")
    if temperatura:
        if conversion == "Celsius a Fahrenheit":
            resultado = (temperatura * 9/5) + 32
            st.write(f"{temperatura} °C es igual a {resultado} °F")
        elif conversion == "Fahrenheit a Celsius":
            resultado = (temperatura - 32) * 5/9
            st.write(f"{temperatura} °F es igual a {resultado} °C")
        elif conversion == "Celsius a Kelvin":
            resultado = temperatura + 273.15
            st.write(f"{temperatura} °C es igual a {resultado} K")
        elif conversion == "Kelvin a Celsius":
            resultado = temperatura - 273.15
            st.write(f"{temperatura} K es igual a {resultado} °C")

elif categoria == "Longitud":
    conversion = st.selectbox(
        "Selecciona la conversión de longitud:",
        [
            "Pies a metros",
            "Metros a pies",
            "Pulgadas a centímetros",
            "Centímetros a pulgadas"
        ]
    )
    longitud = st.number_input("Introduce el valor:")
    if longitud:
        if conversion == "Pies a metros":
            resultado = longitud * 0.3048
            st.write(f"{longitud} pies es igual a {resultado} metros")
        elif conversion == "Metros a pies":
            resultado = longitud / 0.3048
            st.write(f"{longitud} metros es igual a {resultado} pies")
        elif conversion == "Pulgadas a centímetros":
            resultado = longitud * 2.54
            st.write(f"{longitud} pulgadas es igual a {resultado} centímetros")
        elif conversion == "Centímetros a pulgadas":
            resultado = longitud / 2.54
            st.write(f"{longitud} centímetros es igual a {resultado} pulgadas")

elif categoria == "Peso/Masa":
    conversion = st.selectbox(
        "Selecciona la conversión de peso/masa:",
        [
            "Libras a kilogramos",
            "Kilogramos a libras",
            "Onzas a gramos",
            "Gramos a onzas"
        ]
    )
    masa = st.number_input("Introduce el valor:")
    if masa:
        if conversion == "Libras a kilogramos":
            resultado = masa * 0.453592
            st.write(f"{masa} libras es igual a {resultado} kg")
        elif conversion == "Kilogramos a libras":
            resultado = masa / 0.453592
            st.write(f"{masa} kg es igual a {resultado} libras")
        elif conversion == "Onzas a gramos":
            resultado = masa * 28.3495
            st.write(f"{masa} onzas es igual a {resultado} gramos")
        elif conversion == "Gramos a onzas":
            resultado = masa / 28.3495
            st.write(f"{masa} gramos es igual a {resultado} onzas")

elif categoria == "Volumen":
    conversion = st.selectbox(
        "Selecciona la conversión de volumen:",
        [
            "Galones a litros",
            "Litros a galones",
            "Pulgadas cúbicas a centímetros cúbicos",
            "Centímetros cúbicos a pulgadas cúbicas"
        ]
    )
    volumen = st.number_input("Introduce el valor:")
    if volumen:
        if conversion == "Galones a litros":
            resultado = volumen * 3.78541
            st.write(f"{volumen} galones es igual a {resultado} litros")
        elif conversion == "Litros a galones":
            resultado = volumen / 3.78541
            st.write(f"{volumen} litros es igual a {resultado} galones")
        elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
            resultado = volumen * 16.387
            st.write(f"{volumen} pulgadas cúbicas es igual a {resultado} centímetros cúbicos")
        elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
            resultado = volumen / 16.387
            st.write(f"{volumen} centímetros cúbicos es igual a {resultado} pulgadas cúbicas")

elif categoria == "Tiempo":
    conversion = st.selectbox(
        "Selecciona la conversión de tiempo:",
        [
            "Horas a minutos",
            "Minutos a segundos",
            "Días a horas",
            "Semanas a días"
        ]
    )
    tiempo = st.number_input("Introduce el valor:")
    if tiempo:
        if conversion == "Horas a minutos":
            resultado = tiempo * 60
            st.write(f"{tiempo} horas es igual a {resultado} minutos")
        elif conversion == "Minutos a segundos":
            resultado = tiempo * 60
            st.write(f"{tiempo} minutos es igual a {resultado} segundos")
        elif conversion == "Días a horas":
            resultado = tiempo * 24
            st.write(f"{tiempo} días es igual a {resultado} horas")
        elif conversion == "Semanas a días":
            resultado = tiempo * 7
            st.write(f"{tiempo} semanas es igual a {resultado} días")

elif categoria == "Velocidad":
    conversion = st.selectbox(
        "Selecciona la conversión de velocidad:",
        [
            "Millas por hora a kilómetros por hora",
            "Kilómetros por hora a metros por segundo",
            "Nudos a millas por hora",
            "Metros por segundo a pies por segundo"
        ]
    )
    velocidad = st.number_input("Introduce el valor:")
    if velocidad:
        if conversion == "Millas por hora a kilómetros por hora":
            resultado = velocidad * 1.60934
            st.write(f"{velocidad} mph es igual a {resultado} km/h")
        elif conversion == "Kilómetros por hora a metros por segundo":
            resultado = velocidad / 3.6
            st.write(f"{velocidad} km/h es igual a {resultado} m/s")
        elif conversion == "Nudos a millas por hora":
            resultado = velocidad * 1.15078
            st.write(f"{velocidad} nudos es igual a {resultado} mph")
        elif conversion == "Metros por segundo a pies por segundo":
            resultado = velocidad * 3.28084
            st.write(f"{velocidad} m/s es igual a {resultado} ft/s")

elif categoria == "Área":
    conversion = st.selectbox(
        "Selecciona la conversión de área:",
        [
            "Metros cuadrados a pies cuadrados",
            "Pies cuadrados a metros cuadrados",
            "Kilómetros cuadrados a millas cuadradas",
            "Millas cuadradas a kilómetros cuadrados"
        ]
    )
    area = st.number_input("Introduce el valor:")
    if area:
        if conversion == "Metros cuadrados a pies cuadrados":
            resultado = area * 10.7639
            st.write(f"{area} m² es igual a {resultado} ft²")
        elif conversion == "Pies cuadrados a metros cuadrados":
            resultado = area / 10.7639
            st.write(f"{area} ft² es igual a {resultado} m²")
        elif conversion == "Kilómetros cuadrados a millas cuadradas":
            resultado = area * 0.386102
            st.write(f"{area} km² es igual a {resultado} mi²")
        elif conversion == "Millas cuadradas a kilómetros cuadrados":
            resultado = area / 0.386102
            st.write(f"{area} mi² es igual a {resultado} km²")

elif categoria == "Energía":
    conversion = st.selectbox(
        "Selecciona la conversión de energía:",
        [
            "Julios a calorías",
            "Calorías a kilojulios",
            "Kilovatios-hora a megajulios",
            "Megajulios a kilovatios-hora"
        ]
    )
    energia = st.number_input("Introduce el valor:")
    if energia:
        if conversion == "Julios a calorías":
            resultado = energia * 0.239006
            st.write(f"{energia} julios es igual a {resultado} calorías")
        elif conversion == "Calorías a kilojulios":
            resultado = energia * 0.004184
            st.write(f"{energia} calorías es igual a {resultado} kJ")
        elif conversion == "Kilovatios-hora a megajulios":
            resultado = energia * 3.6
            st.write(f"{energia} kWh es igual a {resultado} MJ")
        elif conversion == "Megajulios a kilovatios-hora":
            resultado = energia / 3.6
            st.write(f"{energia} MJ es igual a {resultado} kWh")

elif categoria == "Presión":
    conversion = st.selectbox(
        "Selecciona la conversión de presión:",
        [
            "Pascales a atmósferas",
            "Atmósferas a pascales",
            "Barras a libras por pulgada cuadrada",
            "Libras por pulgada cuadrada a bares"
        ]
    )
    presion = st.number_input("Introduce el valor:")
    if presion:
        if conversion == "Pascales a atmósferas":
            resultado = presion * 9.86923e-6
            st.write(f"{presion} pascales es igual a {resultado} atmósferas")
        elif conversion == "Atmósferas a pascales":
            resultado = presion / 9.86923e-6
            st.write(f"{presion} atmósferas es igual a {resultado} pascales")
        elif conversion == "Barras a libras por pulgada cuadrada":
            resultado = presion * 14.5038
            st.write(f"{presion} barras es igual a {resultado} psi")
        elif conversion == "Libras por pulgada cuadrada a bares":
            resultado = presion / 14.5038
            st.write(f"{presion} psi es igual a {resultado} bares")

elif categoria == "Tamaño de Datos":
    conversion = st.selectbox(
        "Selecciona la conversión de tamaño de datos:",
        [
            "Megabytes a gigabytes",
            "Gigabytes a Terabytes",
            "Kilobytes a megabytes",
            "Terabytes a petabytes"
        ]
    )
    datos = st.number_input("Introduce el valor:")
    if datos:
        if conversion == "Megabytes a gigabytes":
            resultado = datos / 1024
            st.write(f"{datos} MB es igual a {resultado} GB")
        elif conversion == "Gigabytes a Terabytes":
            resultado = datos / 1024
            st.write(f"{datos} GB es igual a {resultado} TB")
        elif conversion == "Kilobytes a megabytes":
            resultado = datos / 1024
            st.write(f"{datos} KB es igual a {resultado} MB")
        elif conversion == "Terabytes a petabytes":
            resultado = datos / 1024
            st.write(f"{datos} TB es igual a {resultado} PB")
