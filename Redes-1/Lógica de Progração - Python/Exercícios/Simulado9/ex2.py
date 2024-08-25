"""Receber uma palavra, calcule quantas vogais (a, e, i, o, u) possui essa palavra e mostre essa informação. Em seguida, peça ao usuário para que ele entre com um caractere(vogal ou consoante) e substitua todas as vogais da palavra dada por esse caractere."""

name = str(input("Escreva um nome: "))

print(f"Letras a: {name.count('a')}")
print(f"Letras e: {name.count('e')}")
print(f"Letras i: {name.count('i')}")
print(f"Letras o: {name.count('o')}")
print(f"Letras u: {name.count('u')}")

carac = str(input("\nEscreva uma vogal ou consoante: "))

name = name.lower().replace("a", carac)
name = name.lower().replace("e", carac)
name = name.lower().replace("i", carac)
name = name.lower().replace("o", carac)
name = name.lower().replace("u", carac)

print(f"\nA string ficou assim: {name}")