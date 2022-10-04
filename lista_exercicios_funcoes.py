import random
import lista_exercicios_funcoes_principal 

def pedirNumero(a):
    while(a < 0):
        print("Número invalido")
        a = int(input("informe um número inteiro dessa vez: "))   
    else:
        print("Número valido")
        return a


def numeroAle(b):
    numAle = random.randint(1, pedirNumero())

    return numAle

def retornarMes():
    if(pedirNumero() == 1):
        return "Janeiro"
    elif(pedirNumero() == 2):
        return "Fevereiro"
    elif(pedirNumero() == 3):
        return "Março" 
    elif(pedirNumero() == 4):
        return "Abril"
    elif(pedirNumero() == 5):
        return "Maio"
    elif(pedirNumero() == 6):
        return "Junho"
    elif(pedirNumero() == 7):
        return "Julho"
    elif(pedirNumero() == 8):
        return "Agosto"
    elif(pedirNumero() == 9):
        return "Setembro"
    elif(pedirNumero() == 10):
        return "Outubro"
    elif(pedirNumero() == 11):
        return ("novembro")
    elif(pedirNumero() == 12):
        return "Dezembro"
    else:
        return"Mês Invalido"

def calcularQuadrado():
    quad = numeroAle() ** 2

def calcularRetangulo():
    print()

def calcularTriangulo():
    print()

def calcularTrapezio():
    print()
