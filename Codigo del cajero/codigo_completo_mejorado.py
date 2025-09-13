# datos de los usuarios: numero de cuenta : {nombre, clave, saldo, movimientos}
usuarios = {
    # usuario: alberto, cuenta: 11222345, clave: 123456789
    11222345: {"nombre": "alberto", 
               "clave": "123456789", 
               "saldo": 1200000, 
               "movimientos": [],
               "bloqueado": False},
    # usuario: yuka, cuenta: 111422123, clave: 987654321
    111422123: {"nombre": "yuka", 
                "clave": "987654321", 
                "saldo": 2300000, 
                "movimientos": [],
                "bloqueado": False},
    # usuario: benito, cuenta: 1114233200, clave: 123454321
    1114233200: {"nombre": "benito", 
                 "clave": "123454321", 
                 "saldo": 3200000, 
                 "movimientos": [],
                 "bloqueado": False},
    # usuario: lauyen, cuenta: 94316677, clave: 13579
    94316677: {"nombre": "lauyen", 
               "clave": "13579", 
               "saldo": 1500000, 
               "movimientos": [],
               "bloqueado": False},
    # usuario: luyz, cuenta: 746238621, clave: 272612
    746238621: {"nombre": "luyz", 
                "clave": "272612", 
                "saldo": 1800000, 
                "movimientos": [],
                "bloqueado": False}
}

# variable para saber que cuenta esta activa
cuenta_activa = 0

# funcion para inicio de sesion
def inicio_sesion():
    # se usa la variable global cuenta_activa para modificar su valor
    global cuenta_activa
    print("""----------------------------------------
------------CAJERO AUTOMATICO-----------
-------BIENVENIDO AL BANCO AGUILA-------
----------------------------------------""")
    # pedimos el numero de la cuenta
    cuenta = int(input("ingresa el numero de la cuenta: "))
    
    # si la cuenta existe en usuarios
    if cuenta in usuarios:
        # si la cuenta ya fue bloqueada
        if usuarios[cuenta]["bloqueado"] == True:
            print("esta cuenta esta bloqueada durante 24 horas, no puedes iniciar sesion")
            inicio_sesion()
        else:
            # variable intentos, se empieza con 3 intentos
            intentos = 3
            
            # mientras tenga intentos y no se haya iniciado sesion
            while intentos > 0 and cuenta_activa == 0:
                # pedir la clave
                clave = input("clave: ")
                
                # si la clave es correcta
                if clave == usuarios[cuenta]["clave"]:
                    # mostrar mensaje de bienvenida
                    print(f"bienvenido {usuarios[cuenta]['nombre']}")
                    # guardar que la cuenta esta activa
                    cuenta_activa = cuenta
                else:
                    # si la clave es incorrecta se resta un intento
                    intentos = intentos - 1
                    print(f"clave incorrecta, te quedan {intentos} intentos")
            
            # si despues de gastar los 3 intentos no se inicio sesion
            if cuenta_activa == 0:
                print("has superado el numero maximo de intentos")
                print("tu cuenta ha sido bloqueada durante 24 horas")
                # se marca la cuenta como bloqueada
                usuarios[cuenta]["bloqueado"] = True
                inicio_sesion()
    
    # si la cuenta no existe
    else:
        print("esa cuenta no existe")
        # vuelve a pedir la cuenta
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
    limite_retirar = 7000000
    
    if monto > limite_retirar:
        print(f"no se puede retirar mas de ${limite_retirar}, por favor ingresa otro valor nuevamente")
        retirar()
    elif monto > 0 and total <= saldo:
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
    # obtiene la lista de movimientos del usuario activo
    movimientos = usuarios[cuenta_activa]["movimientos"]   
    # si la lista está vacía
    if len(movimientos) == 0:                             
        # muestra mensaje de vacío
        print("no hay movimientos registrados")           
        # si la lista tiene elementos
    else:                                                 
        print("- - - historial de movimientos - - -")
        # inicializa un contador en 0
        i = 0                                             
        # mientras i sea menor que la cantidad de elementos
        while i < len(movimientos):                       
            # imprime el movimiento en la posición i
            print(movimientos[i])                         
            # aumenta el contador en 1 para pasar al siguiente
            i += 1                                        


# funcion para el menu principal
def menu():
    opcion = 0
    # mientras la opcion sea diferente a 5
    while opcion != 5:
        print("\n------ ¿Que podemos hacer hoy por ti? ------")
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
                print("-------GRACIAS POR TU CONFIANZA Y PREFERENCIA-------")
                exit()
        elif opcion == 2:
            retirar()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
                print("-------GRACIAS POR TU CONFIANZA Y PREFERENCIA-------")
                exit()
        elif opcion == 3:
            depositar()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
                print("-------GRACIAS POR TU CONFIANZA Y PREFERENCIA-------")
                exit()
        elif opcion == 4:
            ver_historial()
            ir_al_menu = input("deseas ir al menu?[1], \no deseas salir?[2]\n: ")
            if ir_al_menu == "1":
                menu()
            elif ir_al_menu == "2":
                print("sesion cerrada")
            print("-------GRACIAS POR TU CONFIANZA Y PREFERENCIA-------")
            exit()
        elif opcion == 5:
            cerrar_sesion = input("estas seguro que deseas salir?, [1], \no deseas volver al menu?, [2]\n: ")
            if cerrar_sesion == "2":
                menu()
            elif cerrar_sesion == "1":
                print("sesion cerrada")
                print("-------GRACIAS POR TU CONFIANZA Y PREFERENCIA-------")

# programa principal
inicio_sesion()
if cuenta_activa != 0:
    menu()
