def fatorial(num):
    global x #mostra que esta e uma variavel global
    fat = 1 
    i = 2
    while(i <= num):
        fat = fat * i
        i+= 1
    print("O valor de {} e o resultado é: {} ".format(num, fat))

x = int(input("Informe um número: "))

fatorial(x)

"""def fatorial2(fat):
    resultado = 1
    for i in range(fat, 0, -1):
        resultado = resultado * i
    print("Fatorial: {}".format(resultado))


fatorial2()"""

"""
Variavel Global: todo o codigo ve

Variavel Local: apenas vista dentro do subalgoritimo
"""