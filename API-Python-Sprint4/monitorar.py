from pickletools import decimalnl_short
from unicodedata import decimal
import psutil
import time
import datetime
from datetime import date
import os
import math
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
        
    """ else:
    db_connection.close()
    print('connection close') """

    totalRAM =  round( (psutil.virtual_memory()[0]) * (10 ** -9),1)   
    totalVirtual =  round((psutil.virtual_memory()[1]) * (10 ** -8),1)
    totalDisco = round((psutil.disk_usage('/')[0]) * (10 ** -9))
    freqMax = round(((psutil.cpu_freq().max) / 1000),2)
    uploadPack = round((psutil.net_io_counters()[2]) * (10 ** -3))
    downloadPack = round((psutil.net_io_counters()[3]) * (10 ** -3))
    
    dataHora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    # print("\n")
    # print('--- CPU ---')
    # print("\n")

    PrcntCPU =  psutil.cpu_percent() 
    FreqCPU =  freqMax
    PortasLogicas = psutil.cpu_count()

    # print("\n")
    # print('--- Memoria RAM ---')
    # print("\n")
    
    TotalRAM = totalRAM
    PrcntRAM = psutil.virtual_memory()[2] 
    TotalVirtual = totalVirtual

    # print("\n")
    # print('--- Disco ---')
    # print("\n")

    TotalDisco = totalDisco
    PrcntDisco = psutil.disk_usage('/')[3] 

    # print("\n")
    # print('--- Rede ---')
    # print("\n")

    Upload = uploadPack
    Download = downloadPack
    DropDown = psutil.net_io_counters()[6]
    DropUp = psutil.net_io_counters()[7]

    cursor = db_connection.cursor()
    sql = "INSERT INTO leitura (DataHora,PrcntCPU,FreqCPU,PortasLogicas,TotalRAM,PrcntRAM,TotalVirtual,TotalDisco,PrcntDisco,Upload,Download,DropDown,DropUp) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = [dataHora, PrcntCPU, FreqCPU, PortasLogicas, TotalRAM, PrcntRAM, TotalVirtual, TotalDisco, PrcntDisco, Upload, Download, DropDown, DropUp]
    cursor.execute(sql, values)
    current_date = date.today()
    formatted_date = current_date.strftime('%d/%m/%Y')

    print(formatted_date)
    print(cursor.rowcount, "Inseri no banco")
    db_connection.commit()
    db_connection.close()
   
    time.sleep(3) #tempo de 3 segundos para a repetição
    print("Processo finalizado!")