import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def menu():
    print("Calculadora")
    print("1. Sumar dos numeros")
    print("2. Restar dos numeros")
    print("3. Multiplicar dos numeros")
    print("4. Dividir dos numeros")
    print("5. Sumar N numeros")
    print("6. Salir")

    opcion = input("Elige una opcion: ")
    if opcion == '1':
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        print(f"Resultado: {sumar.sumar(a, b)}")
    elif opcion == '2':
        a = float(input("Ingresa el primer nmero: "))
        b = float(input("Ingresa el segundo nmero: "))
        print(f"Resultado: {resta.restar(a, b)}")
    elif opcion == '3':
        a = float(input("Ingresa el primer nmero: "))
        b = float(input("Ingresa el segundo nmero: "))
        print(f"Resultado: {multiplicacion.multiplicar(a, b)}")
    elif opcion == '4':
        a = float(input("Ingresa el primer nmero: "))
        b = float(input("Ingresa el segundo numero: "))
        print(f"Resultado: {dividir.dividir(a, b)}")
    elif opcion == '5':
        numeros = input("Ingresa los numeros separados por espacios: ")
        lista_numeros = [float(num) for num in numeros.split()]
        print(f"Resultado: {suma_avanzada.sumar_numeros(lista_numeros)}")
    elif opcion == '6':
        print("Saliendo...")
        exit()
    else:
        print("Opcion no valida. Intenta de nuevo.")
        menu()

if __name__ == "__main__":
    while True:
        menu()
