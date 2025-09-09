# datos de los usuarios: numero de cuenta : {nombre, clave, saldo, movimientos}
usuarios = {
    # usuario: alberto, cuenta: 11222345, clave: 123456789
    11222345: {"nombre": "alberto", 
               "clave": "123456789", 
               "saldo": 1200000, 
               "movimientos": []},
    # usuario: yuka, cuenta: 111422123, clave: 987654321
    111422123: {"nombre": "yuka", 
                "clave": "987654321", 
                "saldo": 2300000, 
                "movimientos": []},
    # usuario: benito, cuenta: 1114233200, clave: 123454321
    1114233200: {"nombre": "benito", 
                 "clave": "123454321", 
                 "saldo": 3200000, 
                 "movimientos": []},
    # usuario: lauyen, cuenta: 94316677, clave: 13579
    94316677: {"nombre": "lauyen", 
               "clave": "13579", 
               "saldo": 1500000, 
               "movimientos": []},
    # usuario: luyz, cuenta: 746238621, clave: 272612
    746238621: {"nombre": "luyz", 
                "clave": "272612", 
                "saldo": 1800000, 
                "movimientos": []}
}

# variable para saber que cuenta esta activa
cuenta_activa = 0

# funcion para inicio de sesion
def inicio_sesion():
    # se usa la variable global cuenta_activa para modificar su valor
    global cuenta_activa
    print("""----------------------------------------
------------CAJERO AUTOMATICO-----------
----------------------------------------""")
    print("Bienvenido al banco aguila")
    cuenta = int(input("ingresa el numero de la cuenta: "))
    # si cuenta existe en usuarios
    if cuenta in usuarios:
        # pedir la clave
        clave = input("clave: ")
        # si la clave es correcta
        if clave == usuarios[cuenta]["clave"]:
            print(f"bienvenido {usuarios[cuenta]['nombre']}")
            # cambiar el valor de cuenta_activa a la cuenta ingresada
            cuenta_activa = cuenta
        # si la clave es incorrecta
        else:
            print("la clave es incorrecta")
    # si la cuenta no existe
    else:
        print("esa cuenta no existe")
        # volver a pedir la cuenta
        inicio_sesion()

# funcion para consultar saldo
def consultar_saldo():
    saldo = usuarios[cuenta_activa]["saldo"]
    print(f"saldo actual: ${saldo}")

# funcion para retirar dinero
def retirar():
    # usar la variable global usuarios para poder modificar su valor
    global usuarios
    # pedir el monto a retirar
    monto = int(input("ingresa la cantidad de dinero a retirar: "))
    saldo = usuarios[cuenta_activa]["saldo"]
    comision = int(monto * 0.015)
    total = monto + comision
    if monto > 0 and total <= saldo:
        nuevo_saldo = saldo - total
        usuarios[cuenta_activa]["saldo"] = nuevo_saldo
        print(f"retiro: ${monto}, comision: ${comision}")
        print(f"nuevo saldo: ${nuevo_saldo}")
        usuarios[cuenta_activa]["movimientos"].append(f"retiro: ${monto} | comision: ${comision}")
    else:
        print("saldo insuficiente o monto invalido")
        print("ingresa una cantidad valida")
        retirar()

# funcion para depositar dinero
def depositar():
    global usuarios
    monto = int(input("ingresa la cantidad de dinero a depositar: "))
    if monto > 0:
        saldo = usuarios[cuenta_activa]["saldo"]
        nuevo_saldo = saldo + monto
        usuarios[cuenta_activa]["saldo"] = nuevo_saldo
        print(f"deposito: ${monto}")
        print(f"nuevo saldo: ${nuevo_saldo}")
        usuarios[cuenta_activa]["movimientos"].append(f"deposito: ${monto}")
    else:
        print("el deposito debe ser mayor que 0")
        print("ingresa una cantidad valida")
        depositar()

# funcion para ver historial de movimientos
def ver_historial():
    movimientos = usuarios[cuenta_activa]["movimientos"]
    if len(movimientos) == 0:
        print("no hay movimientos registrados")
    else:
        print("- - - historial de movimientos - - -")
        for m in movimientos:
            print(m)

# funcion para el menu principal
def menu():
    opcion = 0
    while opcion != 5:
        print("\n1. consultar saldo")
        print("2. retirar")
        print("3. depositar")
        print("4. ver historial de movimientos")
        print("5. salir")
        opcion = int(input("opcion: "))
        if opcion == 1:
            consultar_saldo()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
                print("gracias por preferirnos")
                exit()
        elif opcion == 2:
            retirar()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
                print("gracias por preferirnos")
                exit()
        elif opcion == 3:
            depositar()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
                print("gracias por preferirnos")
                exit()
        elif opcion == 4:
            ver_historial()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
            print("gracias por tu confianza y preferencia")
            exit()
        elif opcion == 5:
            cerrar_sesion = input("estas seguro que deseas salir?, [1], \no deseas volver al menu?, [2]\n: ")
            if cerrar_sesion == "2":
                menu()
            elif cerrar_sesion == "1":
                print("sesion cerrada")
                print("gracias por tu confianza y preferencia")

# programa principal
inicio_sesion()
if cuenta_activa != 0:
    menu()
