"""
Nuestra calculadora realiza operaciones basicas tales como suma, resta, multiplicación y división.
El programa permite al usuario elegir la operación deseada y luego ingresar los números para realizar el cálculo.

"""

while True:  
    #Menu de PyCalc
    print("Favor seleccione una Operación")
    print("1. Quiero Sumar")
    print("2. Quiero Restar")
    print("3. Quiero Mulpiplicar")
    print("4. Deseo Dividir")
    print("5. Es todo gracias, Salir")
    print("Selecciona una opcion")

    #El comando "try" hara lo que se indique que se pida
    try:
        operacion = int(input("Favor selecciona una operación (1-5): "))

        if operacion == 5:
            print("Gracias por usar PyCalc!")
            break
        elif operacion in [1, 2, 3, 4]:
            x = float(input("Ingresa X1: "))
            y = float(input("Ingresa X2: "))

            if operacion == 1:
                resultado = x + y
                print("Resultado de Suma es:", resultado)
            elif operacion == 2:
                resultado = x - y
                print("Resultado de Resta es:", resultado)
            elif operacion == 3:
                resultado = x * y
                print("Resultado de Multiplicación es:", resultado)
            elif operacion == 4:
                if y == 0:
                    print("Imposible Dividor por Cero. Intentemos otra cosa")
                    continue
                resultado = x / y
                print("Resultado de División es:", resultado)
        else:
            print("Error: Debes ingresar una opción del Menú.")
    except ValueError: ###arroja el error si es algun caracter no solicitado.
        print("Error: Ingresa solo números válidos.")

    seguir = input("¿Quieres continuar? (s/n): ").lower()
    if seguir == "n":
        print("Hasta Pronto")
        break
    elif seguir == "s":
        continue
    else:
        print("Intente otra vez..")
        