def encontrar_en_tupla(tupla,elemento):
    encontro = False
    i = 0
    while i < len(tupla) and not encontro:
        if elemento == tupla[i]:
            encontro = True
        else:
            i += 1
    return encontro

scrable = {
    ("A","E","I","O","U","L","N","R","S","T"): 1,
    ("D","G"): 2,
    ("B","C","M","P"): 3,
    ("F","H","V","W","Y"): 4,
    "K": 5,
    ("J","X"): 8,
    ("Q","Z"): 10
    }

palabra = input("Ingresar una palabra: ")

lista_llaves = list(scrable)

puntaje = 0

for letra in palabra:
    encontrado = False
    i = 0
    while i < len(lista_llaves) and not encontrado:
        tupla_actual = lista_llaves[i]
        if encontrar_en_tupla(tupla_actual,letra.upper()):
            encontrado = True
            puntaje += scrable.get(tupla_actual)
        else:
            i += 1
    
print(puntaje)
