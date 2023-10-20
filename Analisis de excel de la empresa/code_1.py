import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def centrar_texto(texto, ancho_total):
    longitud_texto = len(texto)
    margen_izquierdo = (ancho_total - longitud_texto) // 2
    texto_centralizado = " " * margen_izquierdo + texto
    return texto_centralizado

def menu(nombre_archivo):
    while True:
        ancho_total = 120  # Ajusta el ancho total deseado para el menú

        print("-" * ancho_total)
        print(centrar_texto("Menú", ancho_total))
        print("-" * ancho_total)
        print("1. Muestra una grafica que compara el porcentaje del bono contra la cantidad de bono.")
        print("-" * ancho_total)
        print("2. Muestra un histograma con la distribucion de las Etnias dentro de la empresa")
        print("-" * ancho_total)
        print("3. Muestra una grafica que compara el salario y la edad")
        print("-" * ancho_total)
        print("4. Muestra un histograma con la distribucion de la ciudad natal de cada uno de los empleados")
        print("-" * ancho_total)
        print("5. Salir")
        print("-" * ancho_total)
        opcion = input("Selecciona una opción (1-5): ")
        

        if opcion == "1":
            columna_variable1="Bonus %"
            columna_variable2="BONO"
            comparar_y_graficar_desde_excel(nombre_archivo, columna_variable1, columna_variable2)
            print("Elegiste la opción 1.")
        elif opcion == "2":
            nombre_de_columna="Ethnicity"
            crear_histograma_y_mostrar_numero_mas_alto(nombre_archivo, nombre_de_columna)
            print("Elegiste la opción 2.")
        elif opcion == "3":
            columna_variable1="Age"
            columna_variable2="Annual Salary"
            comparar_y_graficar_desde_excel(nombre_archivo, columna_variable1, columna_variable2)
            print("Elegiste la opción 3.")
        elif opcion == "4":
            nombre_de_columna="City"
            grafico = crear_histograma_y_mostrar_numero_mas_alto(nombre_archivo, nombre_de_columna)
            print("Elegiste la opción 4.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break  # Sale del bucle while para finalizar el programa
        else:
            print("Opción no válida. Introduce 1, 2, 3, 4 o 5.")
    
def crear_histograma_y_mostrar_numero_mas_alto(archivo_excel, nombre_columna):
    try:
        # Configuración de estilo utilizando seaborn
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))

        # Lee el archivo Excel en un DataFrame
        df = pd.read_excel(archivo_excel)

        # Verifica si la columna deseada existe en el DataFrame
        if nombre_columna in df.columns:
            columna = df[nombre_columna]

            # Calcula el histograma
            plt.hist(columna, bins=10, edgecolor="k", alpha=0.7)
            plt.xlabel(nombre_columna)
            plt.ylabel("Frecuencia")
            plt.title(f"Histograma de {nombre_columna}")

            # Muestra el histograma
            plt.show()

            # Encuentra el valor más alto en el histograma
            valor_mas_alto = max(columna)
            frecuencia_mas_alta = list(columna).count(valor_mas_alto)

            # Muestra en la consola el número más alto con estilo
            print(f"El número más alto en la columna '{nombre_columna}' es '{valor_mas_alto}' con una frecuencia de {frecuencia_mas_alta}.")

        else:
            print(f"La columna '{nombre_columna}' no existe en el archivo Excel.")
    except FileNotFoundError:
        print(f"El archivo {archivo_excel} no se encontró.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

def comparar_y_graficar_desde_excel(archivo_excel, columna_variable1, columna_variable2):
    try:
        # Lee el archivo Excel en un DataFrame
        df = pd.read_excel(archivo_excel)

        # Obtén las columnas de las variables que deseas comparar
        variable1 = df[columna_variable1]
        variable2 = df[columna_variable2]

        # Compara las variables
        if variable1.equals(variable2):
            mensaje = f"{columna_variable1} y {columna_variable2} son iguales."
        else:
            mensaje = f"{columna_variable1} y {columna_variable2} son diferentes."

        # Crea un gráfico de dispersión
        plt.figure(figsize=(8, 6))
        plt.scatter(variable1, variable2, color='b', label=mensaje)

        # Configuración del gráfico
        plt.xlabel(columna_variable1)
        plt.ylabel(columna_variable2)
        plt.title('Comparación de Variables')
        plt.legend(loc='upper right')

        # Muestra el gráfico
        plt.show()

    except FileNotFoundError:
        print(f"El archivo {archivo_excel} no se encontró.")
    except Exception as e:
        print(f"Se produjo un error: {e}")




def main():
    nombre_archivo = "Base_empleados_PrimeraEntrega.xlsx"
    menu(nombre_archivo)
    

main()




