import random

palabras = ['casa','gato','manzana']
print('Bienvenidos al juego')
print('Deberas ingresar una letra para adivinar la palabra')
letra = input('ingresa la letra:').lower()
seleccion = random.choice(palabras)

for letras in seleccion:
    if letras==letra:
        print('Correcto')
    else:
        print('Incorrecto')