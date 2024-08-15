# contador de vocales

def num_vocal(texto):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in texto.lower():
        if letra in vocales:
            vocales[letra] += 1
    return vocales



cadena = input("ingresa una palabra: ")

resultado = num_vocal(cadena)

print("el numero  de veces que aparece cada volcal:")
for vocal, cantidad in resultado.items():
    print(f'{vocal}:{cantidad}')





