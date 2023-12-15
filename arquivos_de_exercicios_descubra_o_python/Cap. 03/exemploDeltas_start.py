#
# Arquivo de exemplo para uso da classe timedeltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def quantosDiasFaltam(ano, mes, dia):
    hoje = date.today()
    dataProcurada = date(ano, mes, dia)
    
    qtosDias = dataProcurada - hoje
    
    mensagemRetorno = "Faltam " + str(qtosDias).replace("days, 0:00:00", "") + " dias para a data " + dataProcurada.strftime("%d/%m/%y")
    
    print(mensagemRetorno)
    
quantosDiasFaltam(2024, 1, 1)
    