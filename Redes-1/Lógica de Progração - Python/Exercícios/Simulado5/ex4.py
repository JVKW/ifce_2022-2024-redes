"""Elabore um algoritmo que dada a idade de um nadador classifique-o em uma das seguintes categorias:"""

# E. Infantil A = 5 a 7 anos
# F. Infantil B = 8 a 11 anos
# G. Juvenil A = 12 a 13 anos
# H. Juvenil B = 14 a 17 anos
# I. Adultos = Maiores de 18 anos

age = int(input("Digite sua idade: "))

if age >= 5 <= 7:
    print("Classe: Infantil A")
elif age >= 8 <= 11:
    print("Classe: Infantil B")
elif age >= 12 <= 13:
    print("Classe: Juvenil A")
elif age >= 14 <= 17:
    print("Classe: Juvenil B")
elif age >= 18:
    print("Classe: Adultos")
