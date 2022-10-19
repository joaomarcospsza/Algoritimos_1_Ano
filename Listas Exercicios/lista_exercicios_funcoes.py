from itertools import count
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
        return ("Mês de Janeiro")
    elif(r == 2):
        return ("Mês de Fevereiro")
    elif(r == 3):
        return ("Mês de Março")
    elif(r == 4):
        return ("Mês de Abril")
    elif(r == 5):
       return ("Mês de Maio")
    elif(r == 6):
        return ("Mês de Junho")
    elif(r == 7):
        return ("Mês de Julho")
    elif(r == 8):
        return ("Mês de Agosto")
    elif(r == 9):
        return ("Mês de Setembro")
    elif(r == 10):
       return ("Mês de Outubro")
    elif(r == 11):
        return ("Mês de Novembro")
    elif(r == 12):
        return ("Mês de Dezembro")
    else:
        return ("Mês invalido")

#4 - Faça funções para resolver as equações de área: do quadrado = x²  do retângulo = b . h 	(base x altura) do triângulo= (b . h)2 do trapézio = (B + b) . h2
def quadrado(x):
    qua = x * x
    return qua

def retangulo(b, a):
    ret = b * a
    return ret

def tringulo(b, a):
    tri = (b * a) /2
    return tri

def trapezio(B, b, h):
    tra = ((B + b) * h) /2
    return tra

#5 - Faça um programa para calcular o Fatorial de um número. Para o cálculo do fatorial, sabemos que n! depende de (n-1)!; este por sua vez depende de (n-2)!; e, assim por diante, até que n seja 1, quando então tem-se que fatorial de 1 é igual a 1 mesmo. Utilize uma função que recebe como parâmetro de entrada o número a ser calculado o fatorial, do tipo inteiro, e retorna o fatorial deste número, também do tipo inteiro
def fatorial(x):
    cont = 1
    fat = 1
    while(x > cont):
        fat *= cont
        cont-=1
    return fat

#6 - Crie uma função para calcular o fatorial, mas não utilize laço de repetição.
def fatNoRepeat(n):
    if (n == 1 or n == 0):
        return (1)
    else:
        return (n * fatNoRepeat(n-1))
