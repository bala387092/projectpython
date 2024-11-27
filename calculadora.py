#funcion para sumar dos numeros

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir entre 0"

#funcion principal para pedir los numeros y mostrar el resultado
def main():
    print("Calculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    try:
        opcion = int(input("Ingrese el número de operación(1/2/3/4)"))

        if opcion in [1, 2, 3, 4]:

            num1 = float(input("Introduce el primer numero: "))
            num2 = float(input("Introduce el segundo numero: "))

    #Realizar la operación
            if opcion == 1:   
                resultado = sumar(num1, num2)
            if opcion == 2:   
                resultado = restar(num1, num2)        
            if opcion == 3:   
                resultado = multiplicar(num1, num2)
            if opcion == 4:   
                resultado = dividir(num1, num2)

            print(f"el resultado es: {resultado}")
        else:
            print("Opción no valida. elige del 1 al 4")
    
    except ValueError:
        print("Por favor introduce valores válidos")
if __name__ == "__main__":
    main()      