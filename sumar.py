#funcion para sumar dos numeros
def sumar(a, b):
    return a + b

#funcion principal para pedir los numeros y mostrar el resultado
def main():

    num1 = float(input("Introduce el primer numero"))
    num2 = float(input("Introduce el segundo numero"))
#llamar a la funcion
    resultado = sumar(num1, num2)
    print(f"el resultado es: {resultado}")


if __name__ == "__main__":
    main()      