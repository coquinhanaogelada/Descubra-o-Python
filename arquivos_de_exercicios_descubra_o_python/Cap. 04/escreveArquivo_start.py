#
# Escrevendo arquivos com funções do Python
#

def escreveArquivo():
    arquivo = open("NoveArquivo.txt", "w+")
    
    arquivo.write("Linha gerada com a funcao 'escreveArquivo' \r\n")
    
    arquivo.close()
    
#escreveArquivo()

def alteraArquivo():
    arquivo = open("NoveArquivo.txt", "a+")
    
    arquivo.write("Linha gerada com a funcao 'alteraArquivo' \r\n")
    
    arquivo.close()
    
alteraArquivo()