# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9

numero = int(input("Digite o número inteiro que deseja ver o sucessor e o antecessor dele:"))
sucessor = numero +1
antecessor = numero -1

print(f"O sucessor desse número é: {sucessor}, e seu antecessor é: {antecessor}")