
import random

class pedirNumero:
    def pedirNumero(a):
    
        while(pedirnum < 0):
            print("Número invalido")
            pedirnum = int(input("informe um número inteiro dessa vez: "))   
        else:
            print("Número valido")
            return pedirnum

class numerosAleatorios:
    def numeroAle(b):
        numAle = random.randint(1, pedirNumero())

        return numAle

pedirnum = int(input("informe um número inteiro: "))

