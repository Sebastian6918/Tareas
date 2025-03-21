saldo = 3000
intentos = 0

while True:
    print(f"Saldo actual: Q{saldo}")
    try:
        monto = int(input("Ingrese monto a retirar (o 0 para salir): "))
    except ValueError:
        print("Entrada no válida. Intente nuevamente.")
        continue
    
    # Salir si el usuario ingresa 0
    if monto == 0:
        print("Gracias por usar el cajero. Adiós.")
        break
    
    # Verificar si el monto es mayor al saldo disponible
    if monto > saldo:
        intentos += 1
        print(f"Saldo insuficiente. Intentos restantes: {3 - intentos}")
        
        # Terminar si se supera el límite de intentos
        if intentos >= 3:
            print("Demasiados intentos fallidos. Operación cancelada.")
            break
        continue
    
    # Verificar que el monto a retirar sea positivo
    if monto <= 0:
        print("Ingrese un monto válido mayor a 0.")
        continue
    
    # Realizar el retiro
    saldo -= monto
    print(f"Retiro exitoso. Nuevo saldo: Q{saldo}")
    
    # Si el saldo se agota, terminar el programa
    if saldo == 0:
        print("Retiro exitoso. Saldo agotado. Adiós.")
        break
    
    # Reiniciar el contador de intentos si el retiro fue exitoso
    intentos = 0