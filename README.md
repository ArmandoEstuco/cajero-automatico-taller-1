Consejo para mejorar tu cajero

Actualmente estás guardando a cada usuario en un diccionario con tupla inmutable:

usuarios = {11222345: ("alberto", "alberto123&", 1200000)}


Eso obliga a hacer cosas como:

usuarios[cuenta] = (usuarios[cuenta][0], usuarios[cuenta][1], nuevo_saldo)


Una mejora sería usar un diccionario anidado, donde cada cuenta tenga claves claras como "nombre", "clave" y "saldo".
Así se vuelve más legible, fácil de modificar y más mantenible.

Ejemplo refactorizado
usuarios = { 
    11222345: {"nombre": "alberto", "clave": "alberto123&", "saldo": 1200000},
    111422123: {"nombre": "yuka", "clave": "1234abcd#", "saldo": 2300000},
    1114233200: {"nombre": "benito", "clave": "hola1234%", "saldo": 3200000},
    94316677: {"nombre": "lauyen", "clave": "lau123", "saldo": 1500000},
    746238621: {"nombre": "luyz", "clave": "contrasena1234/", "saldo": 1800000}
}
Entonces tu código se simplifica así:

# consultar saldo
def consultar_saldo():
    print(f"saldo actual: ${usuarios[cuenta_activa]['saldo']}")

# retirar dinero
def retirar():
    monto = int(input("ingresa la cantidad de dinero a retirar: "))
    saldo = usuarios[cuenta_activa]["saldo"]
    comision = int(monto * 0.015)
    total = monto + comision
    if monto > 0 and total <= saldo:
        usuarios[cuenta_activa]["saldo"] -= total
        print(f"retiro: ${monto}, comision: ${comision}")
        print(f"nuevo saldo: ${usuarios[cuenta_activa]['saldo']}")
        guardar_movimiento(cuenta_activa, f"retiro: ${monto} | comision: ${comision}")
    else:
        print("saldo insuficiente o monto invalido")



y recuerda
Es importante que documenten cada línea de su código. 
Esto no solo facilitará su comprensión y repaso en el futuro, sino que también permitirá que otros usuarios o compañeros
que accedan al repositorio puedan entender claramente su funcionamiento."



