#
# Arquivo com exemplos de como trabalhar com paths
#

from os  import path
import time

def dadosArquivos():
    arquivoExiste = path.exists('NoveArquivo.txt')
    eDiretorio = path.isdir('NoveArquivo.txt')
    pathArquivo = path.realpath('NoveArquivo.txt')
    pathRelativo = path.relpath('NoveArquivo.txt')
    dataCriacao = time.ctime(path.getctime('NoveArquivo.txt'))
    dataModificacao = time.ctime(path.getmtime('NoveArquivo.txt'))
    
    print(arquivoExiste)
    print(eDiretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)
    
dadosArquivos()