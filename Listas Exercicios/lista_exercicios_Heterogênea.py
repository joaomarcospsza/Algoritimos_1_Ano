
#Exercício 01: Um telefone celular precisa ser representado em um programa de computador. Sabe-se que este telefone possui uma marca, um modelo, um ano de fabricação e um preço. Implemente uma estrutura para representar os telefones celulares. Crie três celulares, solicite os dados ao usuário para cada um e apresenteos na tela.
import time

#Criando a classe com seus campos e atributos
class telefone:
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.ano_fabricacao = 0
        self.preco = 0
    
#criando um vetor para armazenar os valores
listaTelefone = [telefone()] * 3

#cadastrando os dados dentro do vetor
for i in range(0, len(listaTelefone)):
    listaTelefone[i] = telefone()
    listaTelefone[i].marca = input("Qual a MARCA do telefone: ")
    listaTelefone[i].modelo = input("Qual o MODELO do telefone {}: ".format(listaTelefone[i].marca))
    listaTelefone[i].ano_fabricacao = int(input("Qual o ANO DE FABRIÇÃO do modelo {}: ".format(listaTelefone[i].modelo)))
    listaTelefone[i].preco = int(input("Qual o PREÇO do modelo {}, R$: ".format(listaTelefone[i].modelo)))
    time.sleep(0.10)
    print(" ")

#Listando todos os itens do vetor
for i in range(0, len (listaTelefone)):
    print("Marca: {}, Modelo: {}, Ano Fabricação: {}, R$: {} \n".format(listaTelefone[i].marca, listaTelefone[i].modelo, listaTelefone[i].ano_fabricacao, listaTelefone[i].preco,))