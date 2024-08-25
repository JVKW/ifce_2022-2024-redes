"""As maçãs custam R$ 0,30 cada se forem compradas menos do que uma dúzia, e R$ 0,25 se forem compradas pelo menos doze. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra."""

apples = int(input("Quantas maçãs você comprou? "))

if apples > 12:
    print(f"Preço: R${apples*0.25}")
elif apples < 12:
    print(f"Preço: R${apples*0.30}")