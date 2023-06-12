"""
Análisis de Sentimiento y Clasificación de Textos - Python + ChatGPT
"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Función para analizar sentimientos
def analizar_sentimientos(texto, tokens, temperatura, modelo="text-davinci-002"):
    """Función para Analizar Sentimientos"""
    prompt = f"Por favor, analiza el sentimiento predominante en el siguiente texto: '{texto}'. El sentimiento es:"
    respuesta = openai.Completion.create (
        engine=modelo,
        prompt=prompt,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Función para clasificar texto
def clasificar_texto(texto, tokens, temperatura, modelo="text-davinci-002"):
    """Función para Clasificar Texto"""
    categorias = [
        "Arte",
        "Ciencia",
        "Deportes",
        "Economía",
        "Educación",
        "Entretenimiento",
        "Medio Ambiente",
        "Politica",
        "Salud",
        "Tecnología"
    ]
    prompt = f"Por favor, clasifica el siguiente texto: '{texto}' en una de éstas categorías: {','.join(categorias)}. La categoría es: "
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=tokens,
        temperature=temperatura
    )
    return respuesta.choices[0].text.strip()

# Función Inicio de APP
def app():
    """APP"""

    opciones = [
        "[0] - ¿Quieres analizar el sentimiento de un texto?",
        "[1] - ¿Quieres clasificar un texto?",
        "[q] - Salir"
    ]

    while True:
        os.system("clear" or "cls")
        print("----------------------------------------------------------------------")
        print("     Bienvenido al Analizador y Clasificador de Textos de El Neto     ")
        print("----------------------------------------------------------------------")

        for opcion in opciones:
            print(opcion)

        print("\n")
        entrada_usuario = input("Escoge una opción: ")

        match entrada_usuario:
            case "0":
                os.system("clear" or "cls")
                print("---------------------------------------------------------------------")
                print("                          Analizar un Texto                          ")
                print("---------------------------------------------------------------------")
                print("\n")
                texto_para_analizar = input("\nIngresa un texto: ").rstrip("\n")
                tokens = int(input("¿Cuantos tokens máximos deseas?: "))
                temperatura = int(input("Del 1 al 10, ¿cuanta creatividad necesitas?: ")) / 10
                sentimiento = analizar_sentimientos(texto_para_analizar, tokens, temperatura)
                print("\n")
                print(f"El Sentimiento es: {sentimiento}.")
                print("\n")
                input("\nEnter para continuar")

            case "1":
                os.system("clear" or "cls")
                print("-----------------------------------------------------------------------")
                print("                          Clasificar un Texto                          ")
                print("-----------------------------------------------------------------------")
                print("\n")
                texto_para_clasificar = input("\nIngresa un texto: ").rstrip("\n")
                tokens = int(input("¿Cuantos tokens máximos deseas?: "))
                temperatura = int(input("Del 1 al 10, ¿cuanta creatividad necesitas?: ")) / 10
                clasificacion = clasificar_texto(texto_para_clasificar, tokens, temperatura)
                print("\n")
                print(f"La Clasificación es: {clasificacion}.")
                print("\n")
                input("\nEnter para continuar")

            case "q":
                os.system("clear" or "cls")
                print("----------------------------------------------------------------------")
                print("  Gracias por usar el Analizador y Clasificador de Textos de El Neto  ")
                print("----------------------------------------------------------------------")
                print("\n")
                break

            case otra:
                print(f"{otra} no es valido")
                input("\nEnter para continuar")

def inicio():
    """Inicio de APP"""
    app()

inicio()
