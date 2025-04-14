"""
Nuestra calculadora realiza operaciones basicas tales como suma, resta, multiplicación y división.
El programa permite al usuario elegir la operación deseada y luego ingresar los números para realizar el cálculo.

"""

while True:
    # Menu de PyCalc
    print("Favor seleccione una Operación")
    print("1. Quiero Sumar")
    print("2. Quiero Restar")
    print("3. Quiero Mulpiplicar")
    print("4. Deseo Dividir")
    print("5. Es todo gracias, quiero Salir")
    print("Selecciona una opcion")

    # El comando "try" hara lo que se indique que se pida
    try:
        calcular = int(input("Favor selecciona una operación (1-5): "))

        if calcular == 5:
            print("Gracias por usar PyCalc!")
            break
        elif calcular in [1, 2, 3, 4]:
            x = float(input("Ingresa X1: "))
            y = float(input("Ingresa X2: "))

            if calcular == 1:
                resultado = x + y
                print("Su resultado es:", resultado)
            elif calcular == 2:
                resultado = x - y
                print("Su resultado es:", resultado)
            elif calcular == 3:
                resultado = x * y
                print("Su resultado es:", resultado)
            elif calcular == 4:
                if y == 0:
                    print("No puede dividir por 0.")
                    continue
                resultado = x / y
                print("Su resultado es:", resultado)
        else:
            print("Lo siento: Debes ingresar una opción dentro del Menú.")
    except ValueError:  # arroja el error si es algun caracter no solicitado.
        print("Error: Ingresa solo números válidos.")

    seguir = input("¿Quieres continuar? (s/n): ").lower()
    if seguir == "n":
        print("Nos vemos, y no olvides visitar nuestro Github")
        break
    elif seguir == "s":
        continue
    else:
        print("Intente otra vez..")
