import random

Lista_de_palabras = ['Practica', 'Puente', 'Bebedero']

palabra_elegida = random.choice(Lista_de_palabras).lower()
print(f"La palabra elegida es: {palabra_elegida}")

display = []
for palabra in palabra_elegida:
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    acierto = input("Ingrese su acierto: ").lower()

    for posicion in range(len(palabra_elegida)):
        palabra = palabra_elegida[posicion]
        if palabra == acierto:
            display[posicion] = palabra

    print(display)
    if "_" not in display:
        end_of_game = True
        print("Has Ganado.")