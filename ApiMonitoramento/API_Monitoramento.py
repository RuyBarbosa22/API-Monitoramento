#para rodar "Cntl+F5"

import psutil
import time
import mysql.connector
import datetime
from datetime import date
# from mysql.connector import errorcode
i = 0

while i<200:
    try:
      con = mysql.connector.connect(
          host='localhost', 
          user='root', 
          password='HugoBossH22@', 
          database='DadosMaquina')
          
      print("Conexão ao banco estabelecida!")
    except mysql.connector.Error as error:
      if error.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
          print("Erro: Database não encontrado")
      elif error.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
          print("Erro: Nome e/ou senha incorretos")
      else:
          print(error)
    dataHora = datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S')
    


#tabela dados
#freqAtual;
    freqAtual = psutil.cpu_freq()[0]

    
#percentualCpu decimal(4,1),
    percentualCpu = psutil.cpu_percent(interval = 1, percpu = True)[0] 

#discoAtual; discoUsado; discoLivre decimal(5,2),
    total = psutil.disk_usage('C:\\')[0]
    usado = psutil.disk_usage('C:\\')[1]
    livre= psutil.disk_usage('C:\\')[2]
    percentualDisco = psutil.disk_usage('C:\\')[3]

    discoTotal = round((total*(10**-9)),2) #convertendo de Kb para Gb
    discoUsado = round((usado*(10**-9)),2) #convertendo de Kb para Gb
    discoLivre = round((livre*(10**-9)),2)#convertendo de Kb para Gb


#memoriaTotal; memoriaUsada; memoriaLivre decimal(3,2),
    totalMem = psutil.virtual_memory()[0]
    disponívelMem =psutil.virtual_memory()[1]
    percentualMem = psutil.virtual_memory()[2]
    usadaMem = psutil.virtual_memory()[3]
    livreMem =psutil.virtual_memory()[4]

    memoriaTotal = round((totalMem *(10**-9)),2)
    memoriaUsada = round((usadaMem*(10**-9)),2)
    memoriaLivre = round((livreMem*(10**-9)),2)


    #método que permite fazer interação por elementos de uma tabela lendo individualmente cada um
    cursor = con.cursor() 
    #comando para inserir os dados das variaveis no banco
    sql = "INSERT INTO dados(dataHora,freqAtual,percentualCpu,discoTotal,discoUsado,discoLivre,memoriaTotal,memoriaUsada, memoriaLivre) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=[dataHora, freqAtual,percentualCpu,discoTotal,discoUsado,discoLivre,memoriaTotal,memoriaUsada,memoriaLivre]
    cursor.execute(sql,values)
    current_date = date.today()
    formatted_date = current_date.strftime('%y/%m/%d')

    print(formatted_date)

    print(cursor.rowcount,"record inserted")
    print("\n")
    con.commit()
    i+=1
    #con.close() #esse método serve para encerrar a captura de dados e envio ao banco

    time.sleep(0.1)
    
