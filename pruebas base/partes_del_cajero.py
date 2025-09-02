usuarios = {
    11222345: ("alberto", "alberto123&", 1500000),
    111422123: ("yuka ", "1234abcd#", 2000000),
    1114233200: ("benito", "hola1234%", 3000000),
    94316677: ("lauyen", "", 1200000),
    746238621: ("luyz", "contrasena1234/", 1800000)
}

def inicio_de_sesion():
    print("""----------------------------------------
------------CAJERO AUTOMATICO-----------
----------------------------------------""")
    print("Bienvenido al banco aguila 3000")

historial = []

def consultar_saldo(cuenta):
    saldo = usuarios[cuenta][2]
    print(f"Tu saldo actual es: ${saldo}.")

# funcion para retirar dinero 
def retirar_dinero():
    if cuenta_activa != 0:
        monto = input("monto a retirar: ")
        if monto.isdigit():
            monto = int(monto)
            saldo = usuarios[cuenta_activa][2]
            comision = int(monto * 0.015)
            total = monto + comision
            if monto > 0 and total <= saldo:
                nuevo_saldo = saldo - total
                usuarios[cuenta_activa] = (usuarios[cuenta_activa][0],
                                           usuarios[cuenta_activa][1],
                                           nuevo_saldo)
                print(f"retiro exitoso, comision: ${comision}")
                print(f"nuevo saldo: ${nuevo_saldo}")
                historial.append(f"retiro: ${monto} | comision: ${comision}")
            else:
                print("saldo insuficiente o monto invalido")
        else:
            print("debe ingresar un numero")



# funcion para depositar dinero
def depositar_dinero():
    if cuenta_activa != None:
        monto = input("monto a depositar: ")
        if monto.isdigit():
            monto = int(monto)
            if monto > 0:
                saldo = usuarios[cuenta_activa][2]
                nuevo_saldo = saldo + monto
                usuarios[cuenta_activa] = (usuarios[cuenta_activa][0],
                                           usuarios[cuenta_activa][1],
                                           nuevo_saldo)
                print("depósito exitoso.")
                print("nuevo saldo: $", nuevo_saldo)
                historial.append("depósito: $" + str(monto))
            else:
                print("el depósito debe ser mayor que 0.")
        else:
            print("debe ingresar un número.")