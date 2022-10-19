import random
#1 - Crie uma função para pedir um número inteiro ao usuário e retornar ele. Toda vez que você precisar de um número informado pelo usuário, utilize ela. Ela não tem parâmetro e o retorno é o valor digitado pelo usuário já com o tipo inteiro.

def NumeroInteiro():
    numInt = int(input("Informe um número inteiro: "))
    
    while(numInt < 0):
        print("Número informado {} não e valido;".format(numInt))
        numInt = int(input("Informe um novo número, dessa vez um inteiro: "))
    else:
        return(numInt)

#2 - Faça uma função para gerar números aleatórios. Esta função deve receber um número inteiro num e retornar um número aleatório entre 1 e num. Assim, toda vez que você precisar de um número qualquer pode usar a função do exercício 1 ou esta.
def NumeroAleatorio(n):
    
    numRand = random.randint(1, n)
    return numRand

