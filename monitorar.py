import psutil
import time
import datetime
import platform
from datetime import date
import mysql.connector
from mysql.connector import errorcode
# pretty library

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'kotlin-na-azure.database.windows.net' 
database = 'Kotlin' 
username = 'Admin-Kotlin' 
password = '1sis@grupo5' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

i = 0
while (i < 5):
    i += 1
    # Tabela - computador    
    sistema_operacional = platform.system()
    print(sistema_operacional)
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

    count = cursor.execute(f"""
    INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total) 
    VALUES ('{sistema_operacional}', {disco_total}, {cpu_nucleos_logicos}, {cpu_nucleos_fisicos}, {cpu_freq_maxima}, {memoria_total})""",
    cnxn.commit())

    count = cursor.execute(f"""
    INSERT INTO disco_dimamico (total, usado, pct_usado, livre, datahora) 
    VALUES ({total}, {usado}, {pct_usado}, {livre}, '{dataHora}')""",
    cnxn.commit())

    count = cursor.execute(f"""
    INSERT INTO cpu_dinamica (pct_uso, freq_uso, livre, dataHora) 
    VALUES ({pct_uso}, {freq_uso}, '{dataHora}')""",
    cnxn.commit())

    count = cursor.execute(f"""
    INSERT INTO memoria_dinamica (mem_total, mem_usando, mem_usando_pct, mem_livre, dataHora) 
    VALUES ({mem_total}, {mem_usando}, {mem_usando_pct}, {mem_livre}, '{dataHora}')""",
    cnxn.commit())

    # # Tabela - computador  
    # sql = "INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total) VALUES (%s,%s,%s,%s,%s,%s)"
    # values = [sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total]
    # cursor.execute(sql, values)
    # current_date = date.today()
    # formatted_date = current_date.strftime('%d/%m/%Y')


    # # Tabela - disco_dinamico
    # sql = "INSERT INTO disco_dinamico (total, usado, pct_usado, livre, datahora) VALUES (%s,%s,%s,%s,%s)"
    # values = [total, usado, pct_usado, livre, dataHora]
    # cursor.execute(sql, values)
    # current_date = date.today()
    # formatted_date = current_date.strftime('%d/%m/%Y')


    # # Tabela - cpu_dinamica
    # sql = "INSERT INTO cpu_dinamica (pct_uso, freq_uso, livre, dataHora) VALUES (%s,%s,%s)"
    # values = [pct_uso, freq_uso, dataHora]
    # cursor.execute(sql, values)
    # current_date = date.today()
    # formatted_date = current_date.strftime('%d/%m/%Y')


    # # Tabela - memoria_dinamica
    # sql = "INSERT INTO memoria_dinamica (mem_total, mem_usando, mem_usando_pct, mem_livre, dataHora) VALUES (%s,%s,%s,%s,%s)"
    # values = [mem_total, mem_usando, mem_usando_pct, mem_livre, dataHora]
    # cursor.execute(sql, values)
    # current_date = date.today()
    # formatted_date = current_date.strftime('%d/%m/%Y')

    # print(formatted_date)
    # print(cursor.rowcount, "Inseri no banco")
   
    time.sleep(3) #tempo de 3 segundos para a repetição
    print("Processo finalizado!")