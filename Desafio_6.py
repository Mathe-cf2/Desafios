# Crie uma função chamada cumprimentar ela deve receber o nome e a hora, essa função deve gerar cumprimentos baseado no periodo do dia
# Periodos :    Manhã: 5 até 12, Tarde: 13 até 18, Noite: 18 até 24

from datetime import datetime

nome = input("Digite seu nome: ")

def cumprimentar(nome):
    hora = datetime.now().hour

    if hora <= 12:
        print(f"Bom dia {nome}!")
    elif hora <= 18:
        print(f"Boa tarde {nome}!")
    else:
        print(f"Boa noite {nome}!")

cumprimentar(nome)


nome = input("Digite seu nome:")
hora = input("Horas:")

def cumprimentar(nome,hora):
    if hora <=12:
        print(f"Bom dia {nome}!")
    elif hora <=18:
        print(f"Boa Tarde {nome}!")
    else:
        print(f"Boa noite {nome}!")

cumprimentar(nome,hora)


# Exemplo: 
# Nome: Allana
# Hora : 9
# Bom dia, Allana

# Exemplo2: 
# Nome: Gustavo B
# Hora : 15
# Boa Tarde, Gustavo B
