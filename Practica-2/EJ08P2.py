def encontrar_repetido(lista,i=0,j=1):
    if j < len(lista):
        if lista[i] == lista[j]:
            return True
        return True and encontrar_repetido(lista,i+1,j+1)
    else:
        return False

palabra = input("Ingresar palabra: ")

palabra_ordenada = sorted(palabra)

print(palabra_ordenada)

print(encontrar_repetido(palabra_ordenada))