# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma palavra: "))

if len(letra) == 1:
    if letra in "aeiouAEIOU":
        print("A letra é uma vogal!")
    else:
        print("A letra é uma consoante!")
else:
    print("Digite apenas 1 palavra!")