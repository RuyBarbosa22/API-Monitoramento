import psutil
import time
import datetime
import platform
from datetime import date
import mysql.connector
from mysql.connector import errorcode
# pretty library

i = 0
while (i < 5):
    i += 1
    try:
        db_connection = mysql.connector.connect(
            host='localhost', user='root', password='#Gf47139014825', database='MIC')
        print("Conectei no banco!")
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
             print("Não encontrei o banco")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Credenciais erradas")
        else:
           print(error)


    # Tabela - computador    
    sistema_operacional = platform.system()
    disco_total = round((psutil.disk_usage('/')[0]) * (10 ** -9))
    cpu_nucleos_fisicos = psutil.cpu_count(logical=False)
    cpu_nucleos_logicos = psutil.cpu_count()
    cpu_freq_maxima = round(((psutil.cpu_freq().max) / 1000),2)
    memoria_total =  round( (psutil.virtual_memory()[0]) * (10 ** -9),1)

    # Tabela - disco_dinamico
    total = disco_total
    usado = round((psutil.disk_usage('/')[1]) * (10 ** -9))
    pct_usado = psutil.disk_usage('/')[3]
    livre = psutil.disk_usage('/')[2]

    # Tabela - cpu_dinamica
    pct_uso = psutil.cpu_percent(interval = 1, percpu = True)[0] 
    freq_uso = psutil.cpu_freq()[0]

    # Tabela - memoria_dinamica
    mem_total = psutil.virtual_memory()[0]
    mem_usando = psutil.virtual_memory()[3]
    mem_usando_pct = psutil.virtual_memory()[2]
    mem_livre = psutil.virtual_memory()[4]

    # Conversão de memórias de MB > GB
    mem_total = round((mem_total *(10**-9)),2)
    mem_usando = round((mem_usando*(10**-9)),2)
    mem_livre = round((mem_livre*(10**-9)),2)


    dataHora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # Tabela - computador  
    cursor = db_connection.cursor()
    sql = "INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total) VALUES (%s,%s,%s,%s,%s,%s)"
    values = [sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')


    # Tabela - disco_dinamico
    cursor = db_connection.cursor()
    sql = "INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total) VALUES (%s,%s,%s,%s,%s,%s)"
    values = [sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')


    # Tabela - cpu_dinamica
    cursor = db_connection.cursor()
    sql = "INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total) VALUES (%s,%s,%s,%s,%s,%s)"
    values = [sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')


    # Tabela - memoria_dinamica
    cursor = db_connection.cursor()
    sql = "INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total) VALUES (%s,%s,%s,%s,%s,%s)"
    values = [sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    print(formatted_date)
    print(cursor.rowcount, "Inseri no banco")
    db_connection.commit()
    db_connection.close()
   
    time.sleep(3) #tempo de 3 segundos para a repetição
    print("Processo finalizado!")