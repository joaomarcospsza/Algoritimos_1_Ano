
# PARTE 1
"""Criar função chamada criarVetor que recebe um número inteiro por parâmetro represetando
o tamanho de um vetor. A função deve criar o vetor, preencher com valores aleatórios
entre 1 e 200 e retornar o vetor. No algoritmo principal, solicite o tamanho
do vetor para o usuário e crie o vetor utilizando a função."""

# PARTE 2
"""Crie um procedimento chamado exibirVetor para exiba na tela o vetor recebido por parâmetro."""

# PARTE 3
"""Crie uma função chamada somaImpares que calcule e retorne a soma de todos os números
ímpares de um vetor recebido por parâmetro. No algoritmo principal, apresente a soma na tela."""

# PARTE 4
"""Implemente um procedimento chamado busca que recebe por parâmetro um número
informado pelo usuário. O procedimento deve, usando a busca sequencial, exibir
uma mensagem na tela dizendo se o número está ou não presente em um vetor
também recebido por parâmetro.
"""

# PARTE 5
"""Implemente uma função chamada ordenar que recebe dois parâmetros: um vetor de números inteiros e o nome de um algoritmo de ordenação(bolha, inserção ou seleção).
Ordene e retorne o vetor recebido de acordo com o parâmetro de ordenação.
DETALHE: um procedimento com as três implementações(que tem no moodle)"""

import random
def criarVetor(tam):
    vetor = [0] * tam
    for i in range(0, tam):
        vetor[i] = random.randint(1, 200)

    return vetor


tam = int(input("digite o tamanho do vetor: "))
vetor = criarVetor(tam)
print(vetor)


def exibirVetor(vetor):
    for i in range(0, len(vetor)):
       print(vetor[i], end = "")
    print(" ")

vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
exibirVetor(vetor)

def somaImpares(vetor):
    soma = 0
    for i in range(0, len(vetor)):
        if(vetor[i] % 2 == 1):
            soma += vetor[i]
    return soma


vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = somaImpares(vetor)
print("a soma é:", soma)

def busca(num, vetor):
    for i in range(0, len(vetor)):
        if(num == vetor[i]):
            return 
    print("O valor não está no vetor.")

    """if(x == True):
        print("Número encontrado!")
    else:
        print("O número não está no vetor.")"""


vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numero = int(input("Digite o número buscado: "))
busca(numero, vetor)

def ordenar(vetor, alg):
    if(alg == 1):
        #bolha
        for i in range(len(vetor)-1, 0, -1):
           for j in range(0, i):
               if vetor[j] > vetor[j+1]:
                   aux = vetor[j+1]
                   vetor[j+1] = vetor[j]
                   vetor[j] = aux
    elif(alg == 2):
        #inserção
        for i in range(1, len(vetor)):
            valor = vetor[i]
            j = i - 1
            while(j >= 0 and vetor[j] > valor):
                vetor[j+1] = vetor[j]
                j -= 1
                vetor[j+1] = valor
    elif(alg == 3):
        #seleção
        for i in range(0, len(vetor)-1):
            menor = vetor[i]
            pmenor = i
            for j in range(i+1, len(vetor)):
               if(menor > vetor[j]):
                   menor = vetor[j]
                   pmenor = j
            c = vetor[i]
            vetor[i] = menor
            vetor[pmenor] = c
    return vetor


opc = int(input(
    "=====escolha a ordenação=====\n 1-bolha\n 2-inserção\n 3-seleção\n Opção:"))
vetor = [9, 1, 2, 3, 4, 5, 6, 7, 8, 0]
x = ordenar(vetor, opc)
print("O vetor ordenado:", x)
