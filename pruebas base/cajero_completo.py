# datos de los usuarios: numero de cuenta : (nombre, clave, saldo)
usuarios = { 
    11222345: ("alberto", "alberto123&", 1200000),
    111422123: ("yuka", "1234abcd#", 2300000),
    1114233200: ("benito", "hola1234%", 3200000),
    94316677: ("lauyen", "lau123", 1500000),
    746238621: ("luyz", "contrasena1234/", 1800000)
}

# variable para saber que cuenta esta activa
cuenta_activa = 0

# crear los archivos para cada usuario
# archivo para alberto
archivo = open("11222345.txt", "w")
archivo.write("no hay movimientos registrados\n")
archivo.close()

# archivo para yuka
archivo = open("111422123.txt", "w")
archivo.write("no hay movimientos registrados\n")
archivo.close()

# archivo para benito
archivo = open("1114233200.txt", "w")
archivo.write("no hay movimientos registrados\n")
archivo.close()

# archivo para lauyen
archivo = open("94316677.txt", "w")
archivo.write("no hay movimientos registrados\n")
archivo.close()

# archivo para luyz
archivo = open("746238621.txt", "w")
archivo.write("no hay movimientos registrados\n")
archivo.close()

# funcion para guardar movimiento en el archivo
def guardar_movimiento(cuenta, texto):
    archivo = open(str(cuenta) + ".txt", "r")
    contenido = archivo.read()
    archivo.close()

    # si el archivo solo tiene "no hay movimientos registrados", lo reemplaza por el nuevo movimiento
    if "no hay movimientos registrados" in contenido:
        archivo = open(str(cuenta) + ".txt", "w")
        archivo.write(texto + "\n")
        archivo.close()
    else:
        # si ya hay movimientos, se agrega al final el movimiento nuevo
        archivo = open(str(cuenta) + ".txt", "a")
        archivo.write(texto + "\n")
        archivo.close()

# funcion para inicio de sesion
def inicio_sesion():
    global cuenta_activa
    print("""----------------------------------------
------------CAJERO AUTOMATICO-----------
----------------------------------------""")
    print("Bienvenido al banco aguila")
    cuenta = int(input("ingresa el numero de la cuenta: "))
    if cuenta in usuarios:
        clave = input("clave: ")
        if clave == usuarios[cuenta][1]:
            print(f"bienvenido {usuarios[cuenta][0]}")
            cuenta_activa = cuenta
        else:
            print("la clave es incorrecta")
    else:
        print("esa cuenta no existe")
        inicio_sesion()

# funcion para consultar saldo
def consultar_saldo():
    saldo = usuarios[cuenta_activa][2]
    print(f"saldo actual: ${saldo}")

# funcion para retirar dinero
def retirar():
    global usuarios
    monto = int(input("ingresa la cantidad de dinero a retirar: "))
    saldo = usuarios[cuenta_activa][2]
    comision = int(monto * 0.015)
    total = monto + comision
    if monto > 0 and total <= saldo:
        nuevo_saldo = saldo - total
        usuarios[cuenta_activa] = (usuarios[cuenta_activa][0],
                                   usuarios[cuenta_activa][1],
                                   nuevo_saldo)
        print(f"retiro: ${monto}, comision: ${comision}")
        print(f"nuevo saldo: ${nuevo_saldo}")
        guardar_movimiento(cuenta_activa, f"retiro: ${monto} | comision: ${comision}")
    else:
        print("saldo insuficiente o monto invalido")
        print("ingresa una cantidad valida")
        retirar()

# funcion para depositar dinero
def depositar():
    global usuarios
    monto = int(input("ingresa la cantidad de dinero a depositar: "))
    if monto > 0:
        saldo = usuarios[cuenta_activa][2]
        nuevo_saldo = saldo + monto
        usuarios[cuenta_activa] = (usuarios[cuenta_activa][0],
                                   usuarios[cuenta_activa][1],
                                   nuevo_saldo)
        print(f"deposito: ${monto}")
        print(f"nuevo saldo: ${nuevo_saldo}")
        guardar_movimiento(cuenta_activa, f"deposito: ${monto}")
    else:
        print("el deposito debe ser mayor que 0")
        print("ingresa una cantidad valida")
        depositar()

# funcion para ver historial de movimientos
def ver_historial():
    archivo = open(str(cuenta_activa) + ".txt", "r")
    contenido = archivo.read()
    archivo.close()
    print("- - - historial de movimientos - - -")
    print(contenido)

# funcion para el menu principal
def menu():
    opcion = 0
    while opcion != 5:
        print("\n1. consultar saldo")
        print("2. retirar")
        print("3. depositar")
        print("4. ver historial")
        print("5. salir")
        opcion = int(input("opcion: "))
        if opcion == 1:
            consultar_saldo()
        elif opcion == 2:
            retirar()
        elif opcion == 3:
            depositar()
        elif opcion == 4:
            ver_historial()
        elif opcion == 5:
            print("sesion cerrada")
            print("gracias por preferirnos")

# programa principal
inicio_sesion()
if cuenta_activa != 0:
    menu()
