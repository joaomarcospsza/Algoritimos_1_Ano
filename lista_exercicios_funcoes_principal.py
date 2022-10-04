from Exercicios.lista_exercicios_funcoes import pedirNumero
import lista_exercicios_funcoes

class pedirNumeroINT:
    pedirnum = int(input("Informe um número inteiro: "))
    pd = pedirNumero(pedirnum)
    print("O número informado foi: {}".format(pd))

pc = lista_exercicios_funcoes.pedirNumero()

na = lista_exercicios_funcoes.numerosAleatorios()
