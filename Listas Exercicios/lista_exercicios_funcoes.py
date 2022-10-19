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

#3 - Faça uma função que receba um número inteiro por parâmetro e retorne o mês correspondente ao número. Por exemplo, 2 corresponde a "Fevereiro". Se o número informado não corresponder a um mês (1 a 12), retorne a mensagem “Mês inválido”.
def RetornaMes(r):

    if(r == 1):
        print("Mês de Janeiro")
    elif(r == 2):
        print("Mês de Fevereiro")
    elif(r == 3):
        print("Mês de Março")
    elif(r == 4):
        print("Mês de Abril")
    elif(r == 5):
        print("Mês de Maio")
    elif(r == 6):
        print("Mês de Junho")
    elif(r == 7):
        print("Mês de Julho")
    elif(r == 8):
        print("Mês de Agosto")
    elif(r == 9):
        print("Mês de Setembro")
    elif(r == 10):
        print("Mês de Outubro")
    elif(r == 11):
        print("Mês de Novembro")
    elif(r == 12):
        print("Mês de Dezembro")
    else:
        print("Mês invalido")
