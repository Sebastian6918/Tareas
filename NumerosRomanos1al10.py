numero = int(input("Ingresa un número entre 1 y 9: "))

if 1 <= numero <= 3:
   print("I" * numero)
elif numero == 4:
   print("IV")
elif 5 <= numero <= 8:

   print("V" + "I" * (numero -5))

elif numero == 9:

   print("IX")
else:
    print("El numero esta fuera de rango ")