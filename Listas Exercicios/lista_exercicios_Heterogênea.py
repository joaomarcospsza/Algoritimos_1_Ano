
#Exercício 01: Um telefone celular precisa ser representado em um programa de computador. Sabe-se que este telefone possui uma marca, um modelo, um ano de fabricação e um preço. Implemente uma estrutura para representar os telefones celulares. Crie três celulares, solicite os dados ao usuário para cada um e apresenteos na tela.
from mimetypes import init
import time
from tokenize import Double

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


#Exercício 02: Um programa de computador deve ser capaz de armazenar dados sobre as partes de uma casa.Como a casa possui vários cômodos e cada cômodo possui uma porta, precisa-se de uma estrutura capaz de representar as portas da casa. Sabe-se que toda porta deve ter registrado a sua largura, sua altura, seu peso e 17 o seu material (ex: madeira, alumínio, etc.). Crie três objetos que representem portas (ex: porta da sala, porta do quarto e porta da cozinha). Preencha os dados da porta solicitando-os ao usuário. Em seguida, apresente os dados das portas.
class porta:
    def __init__(self):
        self.porta_comodo = ""
        self.largura = 0
        self.altura = 0
        self.peso = 0
        self.material = ""

vetor_Porta = [porta()] * 3

for i in range(0, len(porta)):
    vetor_Porta[i] = porta()
    vetor_Porta[i].porta_comodo = input("Para qual comodo será essa porta: ")
    vetor_Porta[i].largura = float(input("Informe a largura da porta: "))
    vetor_Porta[i].altura = float(input("Informe a altura da porta: "))
    vetor_Porta[i].peso = float(input("Informe o peso da porta: "))
    vetor_Porta[i].material = input("Informe o material da porta: ")
    time.sleep(0.10)
    print(" ")

for i in range(0, len(vetor_Porta)):
    print(f"Comodo: {vetor_Porta[i].porta_comodo}, Largura: {vetor_Porta[i].largura}, Altura: {vetor_Porta[i].altura}, Peso: {vetor_Porta[i].peso}, Material: { vetor_Porta[i].material} \n")


