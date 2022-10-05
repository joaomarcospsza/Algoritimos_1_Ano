import random
import lista_exercicios_funcoes_principal 

#1
def pedirNumero(a):
    while(a < 0):
        print("Número invalido")
        a = int(input("informe um número inteiro dessa vez: "))   
    else:
        print("Número valido")
        return a

#2
def numeroAle(b):
    numAle = random.randint(1, b())
    return numAle

#3
def retornarMes(c):
    if(c == 1):
        return "Janeiro"
    elif(c == 2):
        return "Fevereiro"
    elif(c == 3):
        return "Março" 
    elif(c == 4):
        return "Abril"
    elif(c == 5):
        return "Maio"
    elif(c == 6):
        return "Junho"
    elif(c == 7):
        return "Julho"
    elif(c == 8):
        return "Agosto"
    elif(c == 9):
        return "Setembro"
    elif(c == 10):
        return "Outubro"
    elif(c == 11):
        return ("novembro")
    elif(c == 12):
        return "Dezembro"
    else:
        return"Mês Invalido"

#4
def calcularQuadrado(d):
    quad = d ** 2
    return quad
def calcularRetangulo(e,f):
    retangulo = e * f
    return retangulo
def calcularTriangulo(g, h):
    tri = (g * h)/2
    return tri
def calcularTrapezio(i, j):
    tra = ((i + i)*j)/2
    return tra

#5
def fatorial(n):
    fat = 1
    i = 2
    while( i <= n):
        fat = fat*i
        i+=1
    return fat
    
#6
