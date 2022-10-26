#para rodar "Cntl+F5"

import psutil
import time
import datetime
from datetime import date
# from mysql.connector import errorcode
i = 0


    


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


time.sleep(0.1)
    
