consumo = float(input("Ingrese el consumo de agua en metros cúbicos (m³): "))
habitantes = int(input("Ingrese el número de habitantes en el apartamento: "))

if consumo < 15:
    tarifa = 5
elif 15 <= consumo <= 30:
    if habitantes > 3:
        tarifa = 4
    elif habitantes == 3:
        tarifa = 4.5
    else:
        tarifa = 5
else: 
    if habitantes % 2 == 0:  
        tarifa = 4
    elif habitantes > 5:
        tarifa = 3.5
    else:
        tarifa = 4.2


costo_total = consumo * tarifa

print(f"El costo del consumo de agua es: Q{costo_total}")