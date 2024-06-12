import random #Libreria random, para usar random.choice

x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #CARACTERE DISPONIBLES

y = int(input("¿Cual es la longitud de la contraseña?"))#PARA SABER CUANTOS CARACTERES hay en la contraseña

password = "" #GUARDAR LA CONTRASEÑA GENERADA

for i in range(y):
    z = random.choice(x)
    password += z    

print("La contraseña generada fue:",password)
