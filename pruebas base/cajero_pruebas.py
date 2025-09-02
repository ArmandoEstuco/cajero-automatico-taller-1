print("""----------------------------------------
------------CAJERO AUTOMATICO-----------
----------------------------------------""")

saldo = 0
print("Bienvenido al banco aguila 3000")

def contraseña():
    c = input("Ingresa tu contraseña, la contraseña debe tener letras y numeros: ")
    if c == "abc123":
        print("La contraseña es correcta")
    else:
        print("Contraseña incorrecta. Vuelve a intentarlo.")
        contraseña()

def menu():
    print("""\n¿Qué deseas hacer?
1. Consignar
2. Retirar
3. Consultar saldo
4. Salir""")
    opcion = int(input("Ingresa una opción: "))
    return opcion

def salir_o_menu():
    salir_o_menu = input("\nSalir [1] o ir al menú [2]: ")
    if salir_o_menu == "1":
         print("Gracias por usar el cajero automático 3000")
         exit()
    elif salir_o_menu == "2":
        print("regresando al menu principal...")
        seleccionar_opcion_menu()
    else:
        print("por favor ingresa una opcion valida")
        salir_o_menu()

def seleccionar_opcion_menu():
    global saldo  
    while True:  
        opcion = menu()
        if opcion == 1:
            consignacion = float(input("Ingresa la cantidad que quieres consignar: "))
            saldo += consignacion
            print("Acabas de consignar", consignacion, "pesos. Ahora tu saldo es", saldo, "pesos.")
            salir_o_menu()
        elif opcion == 2:
            retirar = float(input("Ingresa la cantidad que quieres retirar: "))
            if retirar <= saldo:
                saldo -= retirar
                print("Acabas de retirar", retirar, "pesos. Ahora tu saldo es", saldo, "pesos.")
                salir_o_menu()
            else:
                print("No tienes suficiente saldo.")
        elif opcion == 3:
            print("Tu saldo actual es", saldo, "pesos.")
            salir_o_menu()
        elif opcion == 4:
            print("Gracias por usar el cajero automático 3000")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Bucle principal
contraseña()
seleccionar_opcion_menu()