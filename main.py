from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def menu():
    while True:
        print("\nCalculadora Open Source")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Suma avanzada (varios números)")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == "2":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == "3":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == "4":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            try:
                resultado = dividir(a, b)
                print(f"Resultado: {resultado}")
            except ValueError as e:
                print(e)
        elif opcion == "5":
            numeros = input("Introduce los números separados por espacio: ")
            lista_numeros = [float(num) for num in numeros.split()]
            print(f"Resultado: {suma_avanzada(*lista_numeros)}")
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()