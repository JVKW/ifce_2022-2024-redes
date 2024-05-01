"""Faça um algoritmo que leia uma sigla de um estado e imprima o gentílico:"""

# 1. Cearense
# 2. Alagoano
# 3. Maranhense
# 4. Baiano
# 5. Pernambucano
# 6. Piauiense
# 7. Potiguar
# 8. Sergipano
# 9. Paraibano
# 10. Não é do Nordeste

sigla = str(input("Digite a sigla de um estado do Ceará: ").lower())

if sigla in "ce":
    print("Cearense")
elif sigla in "al":
    print("Alagoano")
elif sigla in "ma":
    print("Maranhense")
elif sigla in "ba":
    print("Baiano")
elif sigla in "pe":
    print("Pernambucano")
elif sigla in "pi":
    print("Piauiense")
elif sigla in "rn":
    print("Potiguar")
elif sigla in "se":
    print("Sergipano")
elif sigla in "pb":
    print("Paraibano")
else:
    print("Não é do Ceará.")