while True:  
    ###Menu Calculadora
    print ("SELECCIONA LA OPERACIÓN")
    print("1 Sumar")
    print("2 Restar")
    print("3 Mulpiplicar")
    print("4 Dividir")
    print ("5 Exit")
    print ("Nombra una opcion")

    #### try hara lo que se indique que esta solcitando
    try:
        operacion = int(input("Selecciona una operación (1-5): "))

        if operacion == 5:
            print("Gracias por usar la Calculadora.")
            break
        elif operacion in [1, 2, 3, 4]:
            x = float(input("Ingresa n1: "))
            y = float(input("Ingresa n2: "))

            if operacion == 1:
                resultado = x + y
                print("Resultado de Suma es:", resultado)
            elif operacion == 2:
                resultado = x - y
                print("Resultado deResta es:", resultado)
            elif operacion == 3:
                resultado = x * y
                print("Resultado deMultiplicación es:", resultado)
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
        