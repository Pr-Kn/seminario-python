import string

texto = """ El salario promedio de un hombre en Argentina es de $60.000, mientras que
            el de una mujer es de $45.000. Ademas, las mujeres tienen menos
            posibilidades de acceder a puestos de liderazgo en las empresas. """

mayusculas = 0

minusculas = 0

no_letra = 0

lista_palabras = texto.split()

for palabra in lista_palabras:
    if palabra[0] not in string.ascii_letters:
        no_letra += 1
    elif palabra[0].isupper():
        mayusculas += 1
    else:
        minusculas += 1

print(mayusculas)

print(minusculas)

print(no_letra)