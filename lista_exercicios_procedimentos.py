"""
1º - Crie procedimentos com parâmetros informados pelo usuário no programa principal:
Faça uma procedimento que soma dois números. Deve ser utilizado um procedimento chamado somar(), que deve receber os números a serem somados, somar os números e apresentar o resultado na tela.
Faça um procedimento que multiplica dois números. Deve ser utilizado um procedimento chamado multiplicar(), que deve receber os números e realizar a operação de multiplicação, apresentando o resultado na tela.
Faça um procedimento que calcule a raiz quadrada de um número chamado calcularRaiz(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.
Faça um procedimento que calcule a potência de um número(XY) chamado calcularPotencia(). O procedimento deve receber os números por parâmetro, efetuar o cálculo e apresentar o resultado.
Faça um procedimento que calcule a tabuada de 1 a 10 para um número chamado calcularTabuada(). O procedimento deve receber o número por parâmetro, efetuar o cálculo e apresentar o resultado.

2 º - Crie procedimentos com parâmetros:
Crie um procedimento que recebe um vetor de números inteiros por parâmetro. Esta função deve chamar imprimirVetor() e vai imprimir na tela todos os números do vetor informado.
Faça um procedimento chamado encontrarMaior() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o maior valor do vetor.
Faça um procedimento chamada encontrarMenor() que recebe um vetor de números inteiros como parâmetro, procure e informe somente o menor valor do vetor.

3º - Crie no programa principal um vetor e preencha com números. Em seguida, utilize as três funções criadas no exercício anterior.
"""

import math


def somar(a, b):
    somar = n1 + n2
    print("A soma dos números {}, {}  fica: {}".format(a, b, somar))

def multiplicar(x, y):
    resultado =  n1 * n2
    print("A multiplicação dos números {} x {} fica: {}".format(x, y, resultado))

def calcularRaiz(d):
    raiz = math.sqrt(n1)
    print("A multiplicação dos números {} x {} fica: {}".format(d, raiz))

def calcularPotencia():
    print()

def calcularTabuada():
    print()

opcao = 0
while(opcao != 6):
    print(" \n == == == Menu Principal == == == \n 1. Somar \n 2. Multiplicar \n 3. Calcular Raiz \n 4. Calcular Potencia \n 5. Calcular Tabuada \n 6. Sair")

    opcao = input("Informe a opção: ")

    if(opcao == 1):
        n1 =  int(input("Informe o valor do primeiro número: "))
        n2 = int(input("Informe o valor do segundo número: "))
        somar(n1, n2)

    elif(opcao == 2):
        n1 = int(input("Informe o valor do primeiro número: "))
        n2 = int(input("Informe o valor do segundo número: "))
        multiplicar(n1, n2)
    
    elif(opcao == 3):
        n1 = int(input("Informe o valor do primeiro número: "))
        somar(n1)
    
    elif(opcao == 4):
        n1 = int(input("Informe o valor do primeiro número: "))
        n2 = int(input("Informe o valor do segundo número: "))
        somar(n1, n2)

    elif(opcao == 5):
        n1 = int(input("Informe o valor do primeiro número: "))
        n2 = int(input("Informe o valor do segundo número: "))
        somar(n1, n2)
    
    elif(opcao == 6):
        break
    else:
        print("Valor invalido.")

    


