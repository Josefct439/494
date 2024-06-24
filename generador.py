import random
chars = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
long = int(input("Introduzca la longitud de la contraseña"))
newpass = ("")
for i in range (long):
    newpass = newpass + random.choice(chars)

print(newpass)
