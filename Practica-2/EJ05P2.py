def count_word(str,wrd):
    count = 0
    for item in str:
        if item == wrd:
            count += 1
    return f"Se encontro la palabra {wrd} {count} veces"

phrase = input("Ingresar una frase: ")

#Recorro el string buscando signos de puntuacion y reemplazandolos con un espacio en blanco
delete = (".",",",":",";")

for sign in delete:
    phrase = phrase.replace(sign,"")

word = input("Ingresar una palabra para buscar en la frase: ").lower()

word_list = phrase.lower().split()

print(count_word(word_list,word))