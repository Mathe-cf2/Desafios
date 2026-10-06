# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00

salario = float(input("Digite o seu salário:"))
porcentagem = 15

conta = salario * porcentagem/100
salario_novo = conta + salario

print(f"O seu novo salário será: {salario_novo}")