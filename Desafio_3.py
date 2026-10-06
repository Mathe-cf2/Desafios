# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# Exemplo:
# Você digitou o número : 10
# --------------- Tabuada do 10 ------------------
# 10 X 0 = 0
# 10 X 1 = 10
# E assim sucessivamente....

numero = int(input("Digite um número inteiro que deseja saber a tabuada:"))

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")