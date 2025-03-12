anio_vehiculo = int(input("Ingrese el año del vehículo: "))
ultimo_digito_placa = int(input("Ingrese el último dígito de la placa del vehículo: "))

antiguedad = 2025 - anio_vehiculo

if antiguedad > 25:
    print("Advertencia: Mantenimiento obligatorio")

if anio_vehiculo >= 2001:

    if ultimo_digito_placa % 2 == 0:
        print("NO circula los lunes")
    else:
        print("NO circula los viernes")

    if anio_vehiculo % 2 == 0:
        print("Y solo circula hasta el mediodía los sábados")

elif anio_vehiculo >= 1998:

    if ultimo_digito_placa % 2 == 0:
        print("NO circula los lunes")
    else:
        print("NO circula los viernes")

    if anio_vehiculo % 2 == 0:
        print("Y solo circula hasta el mediodía los sábados")