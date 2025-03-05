#Ejercicio 1


oracion = "Python es un lenguaje poderoso"
palabras = oracion.split()

p1 = palabras[0]
p2 = palabras[-1]    

print("Primera palabra:",p1,", Ultima palabra:",p2)


#Ejercicio 2

cadena = "Hola   mundo   en   Python"
cadena_limpia = " ".join(cadena.split())

print(cadena_limpia)


#Ejercicio 3


correo = "usuario@gmail.com"
dominio = correo.split('@')[1]

print(dominio)


#Ejercicio 4


archivo = "documento.pdf"
extension_correcta = archivo.endswith('.pdf')

print(extension_correcta)


#Ejercicio 5


texto = "Me gusta Python"
texto_invertido = " ".join(texto.split()[::-1])

print(texto_invertido)


#Ejercicio 6 


poema1 = """Podrá nublarse el sol eternamente;
Podrá secarse en un instante el mar;
Podrá romperse el eje de la tierra
Como un débil cristal."""

canto1 = """Eres como la noche, callada y constelada.
Tu silencio es de estrella, tan lejano y sencillo.
Me gustas cuando callas porque estás como ausente.
Distante y dolorosa como si hubieras muerto."""

poema2 = """El viento me susurra en las tardes,
Las olas del mar cantan su canción,
El cielo se cubre de sombras doradas,
Y la luna brilla con gran emoción."""

canto2 = """Tu voz es mi refugio en la tormenta,
Tus ojos el faro que me guía,
Cada palabra tuya es música en mi alma,
Y en tus brazos encuentro paz y melodía."""

poema3 = """En la quietud de la noche estrellada,
Tus pasos se mezclan con el viento,
Y la luz de la luna canta canciones
Que solo mi corazón sabe entender."""

texto = input("Ingrese un texto: ").lower()

if "poema" in texto:
    print(poema1)
elif "canción" in texto:
    print(canto1)
elif "viento" in texto:
    print(poema2)
elif "luz" in texto:
    print(canto2)
elif "noche" in texto:
    print(poema3)
else:
    print("Lo siento, no tengo una respuesta para eso.")
