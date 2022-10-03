
import math


def somar(a, b):
    somar = n1 + n2
    print("A soma dos números {} + {}  fica: {}".format(a, b, somar))

def multiplicar(x, y):
    resultado =  n1 * n2
    print("A multiplicação dos números {} x {} fica: {}".format(x, y, resultado))

def calcularRaiz(d):
    raiz = math.sqrt(n1)
    print("A raiz de {} fica: {}".format(d, raiz))

def calcularPotencia(e, f):
    potencia = math.pow(b, p)
    print("A pôtencia de {}^{} fica: {}".format(e, f, potencia))

def calcularTabuada(g):

    for i in range(1, 10+1):
        tabuada = numero * i
        print("{} X {} = {}".format(g, i, tabuada))


opc = 0
while(opc != 6):
    print(" \n == == == Menu Principal == == == \n 1. Somar \n 2. Multiplicar \n 3. Calcular Raiz \n 4. Calcular Potencia \n 5. Calcular Tabuada \n 6. Sair")

    opc = int(input("Informe a opção: "))

    if(opc == 1):
        print("Você entrou em 'Somar...'")
        n1 =  int(input("Informe o valor do primeiro número para soma: "))
        n2 = int(input("Informe o valor do segundo número par asoma: "))
        somar(n1, n2)

    elif(opc == 2):
        print("Você entrou em 'Multiplicação...'")
        n1 = int(input("Informe o primeiro número para multiplicação: "))
        n2 = int(input("Informe o segundo número para multiplicação: "))
        multiplicar(n1, n2)
    
    elif(opc == 3):
        print("Você entrou em 'Calcular Raiz...'")
        n1 = int(input("Informe o valor: "))
        calcularRaiz(n1)
    
    elif(opc == 4):
        print("Você entrou em 'Calcular Potência...'")
        b = int(input("Informe o valor da Base: "))
        p = int(input("Informe o valor do expoente: "))
        calcularPotencia(b, p)

    elif(opc == 5):
        print("Você entrou em 'Calcular Tabuada...'")
        numero = int(input("Informe o número da tabuada: "))
        calcularTabuada(numero)
    
    elif(opc == 6):
        print("Finalizando o programa...")
        break
    else:
        print("Número Informado é invalido;")

    


