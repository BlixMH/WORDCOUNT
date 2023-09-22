# Blix Modeweg-hansen

# WORD_COUNTER

def count_word():  # définir la fonction pour que le programme compte des mots
    texte = str(input('Mettre une phrase et je vous direz le nombre de mots:'))  # entrer la phrase voulu
    return print(len(texte.split()))


count_word()
