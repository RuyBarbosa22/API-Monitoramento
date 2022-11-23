import psutil
import time
import datetime
import platform
from datetime import datetime
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
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE=' +
                      database+';ENCRYPT=yes;UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

conn = mysql.connector.connect(
            host='172.17.0.2',
            database='BancoPi',
            user='root',
            password='senha123'
            port=3306
        )
print("Consegui! Conexão com o Banco de Dados MySQL efetuada com sucesso.")
cursorMySQL = conn.cursor()

i = 0
while (i < 5):
    i += 1
    # Tabela - computador
    print("Processo iniciado!")
    sistema_operacional = platform.system()
    disco_total = round((psutil.disk_usage('/')[0]) * (10 ** -9))
    cpu_nucleos_fisicos = psutil.cpu_count(logical=False)
    cpu_nucleos_logicos = psutil.cpu_count()
    cpu_freq_maxima = round(((psutil.cpu_freq().max) / 1000), 2)
    memoria_total = round((psutil.virtual_memory()[0]) * (10 ** -9), 1)

    # Tabela - disco_dinamico
    total = disco_total
    usado = round((psutil.disk_usage('/')[1]) * (10 ** -9))
    pct_usado = psutil.disk_usage('/')[3]
    livre = psutil.disk_usage('/')[2]

    # Tabela - cpu_dinamica
    pct_uso = psutil.cpu_percent(interval=1, percpu=True)[0]
    freq_uso = psutil.cpu_freq()[0]

    # Tabela - memoria_dinamica
    mem_total = psutil.virtual_memory()[0]
    mem_usando = psutil.virtual_memory()[3]
    mem_usando_pct = psutil.virtual_memory()[2]
    mem_livre = psutil.virtual_memory()[4]
    
    # Conversão de memórias de MB > GB
    mem_total = round((mem_total * (10**-9)), 2)
    mem_usando = round((mem_usando*(10**-9)), 2)
    mem_livre = round((mem_livre*(10**-9)), 2)

    dataHora = datetime.now()
    dataHora = dataHora.strftime("%d-%m-%Y %H:%M:%S")
    time.sleep(1.5)

    print("Executando...")
    
    cursor.execute("""
    INSERT INTO dbo.computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total,codEmpresa,fk_empresa)
    VALUES (?,?,?,?,?,?,?,?);""",
                    (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total,'12345', 7,))
    cnxn.commit()

    cursorMySQL.execute("""
    INSERT INTO computador (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total, codEmpresa, fk_empresa)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""",
                    (sistema_operacional, disco_total, cpu_nucleos_logicos, cpu_nucleos_fisicos, cpu_freq_maxima, memoria_total,'12345', 1,))
    conn.commit()

    cursor.execute("""
    INSERT INTO dbo.disco_dinamico (total, usado, pct_usado, livre, dataHora, fk_computador)
    VALUES (?,?,?,?,?,?);""", 
        (total, usado, pct_usado, livre, dataHora, 203,))
    cnxn.commit()

    cursorMySQL.execute("""
    INSERT INTO disco_dinamico (total, usado, pct_usado, livre, dataHora, fk_computador)
    VALUES (%s,%s,%s,%s, current_timestamp(),%s);""", 
        (total, usado, pct_usado, livre, 201,))
    conn.commit()

    cursor.execute("""
    INSERT INTO dbo.cpu_dinamica (pct_uso, freq_uso, dataHora,fk_computador)
    VALUES (?,?,?,?);""", 
        (pct_uso, freq_uso, dataHora, 203,))
    cnxn.commit()

    cursorMySQL.execute("""
    INSERT INTO cpu_dinamica (pct_uso, freq_uso, dataHora,fk_computador)
    VALUES (%s,%s,current_timestamp(),%s);""", 
        (pct_uso, freq_uso, 201,))
    conn.commit()

    cursor.execute("""
    INSERT INTO dbo.memoria_dinamica (mem_total, mem_usando, mem_usando_pct, mem_livre, dataHora,fk_computador)
    VALUES (?,?,?,?,?,?);""", 
        (mem_total, mem_usando, mem_usando_pct, mem_livre, dataHora, 203,))
    cnxn.commit()

    cursorMySQL.execute("""
    INSERT INTO memoria_dinamica (mem_total, mem_usando, mem_usando_pct, mem_livre, dataHora,fk_computador)
    VALUES (%s,%s,%s,%s, current_timestamp(),%s);""", 
        (mem_total, mem_usando, mem_usando_pct, mem_livre, 201,))
    conn.commit()

    time.sleep(1.5)
    print("Processo finalizado!")
    time.sleep(3)  

    # conn.commit()
    