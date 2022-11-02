import mysql.connector

from mysql.connector import errorcode


banco = mysql.connector.connect(
		host='localhost', user='root', password='', database='algoritmos')
print("Conexão estabelecida!")
    

#Executa uma consulta precisamos de um "ponteiro" para o banco

cursor = banco.cursor()
for i in range(1, 3+1):

    #Inserindo valores no banco
    sql = "INSERT INTO disciplinas (nome, ch, professor) VALUES (%s,%s,%s)"

    #pedindo valores
    nome = input("Informe o nome da Disciplina: ")
    ch = int(input("Informe a quantidade de horas da disciplina: "))
    professor = input("Informe o professor: ")

    #valores
    valor = (nome, ch, professor)

    #execulta consulta
    cursor.execute(sql, valor)

resultado = cursor.fetchall()

for i in range(0, len(resultado)):
    print(resultado[i])

#salva a consulta feita no banco de dados
banco.commit()
#fecha o banco
banco.close()
