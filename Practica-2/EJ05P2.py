def count_word(str,wrd):
    count = 0
    for item in str:
        if item == wrd:
            count += 1
    return f"Se encontro la palabra {wrd} {count} veces"


phrase = input("Ingresar una frase: ")

word = input("Ingresar una palabra para buscar en la frase: ").lower()

word_list = phrase.lower().split()

print(count_word(word_list,word))