#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil

def copiarArquivo():
    if path.exists('NoveArquivo.txt'):
        pathAtual = path.realpath('NoveArquivo.txt')
        novoPath = pathAtual + '.bkp'
        shutil.copy(pathAtual, novoPath)
        
        shutil.copystat(pathAtual, novoPath)
        
# copiarArquivo()

def renomearArquivo():
    if path.exists('NoveArquivo.txt.bkp'):
        os.rename("NoveArquivo.txt.bkp", "ArquivoAlterado2.txt")
        
renomearArquivo()