"""Elabore um algoritmo que receba 2 valores numéricos e um símbolo. Caso o símbolo seja um dos relacionados abaixo
efetue a operação correspondente com os valores. Cuidado não efetuar uma divisão por 0. Símbolos: “+” operação de soma,
“-” operação de subtração, “*” operação de multiplicação, “/” operação de divisão."""

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
simb = str(input("Oque desejas fazer?\n[+]Soma\n[-]Subtração\n[*]Multiplicação\n[/]Divisão\n> "))

if simb == "+":
    res = num1 + num2
    print(f"{num1} {simb} {num2} = {res}")
elif simb == "-":
    res = num1 - num2
    print(f"{num1} {simb} {num2} = {res}")
elif simb == "*":
    res = num1 * num2
    print(f"{num1} {simb} {num2} = {res}")
elif simb == "/":
    res = num1 / num2
    print(f"{num1} {simb} {num2} = {res}")