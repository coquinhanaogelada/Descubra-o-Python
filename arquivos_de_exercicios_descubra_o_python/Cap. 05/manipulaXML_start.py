# 
# Arquivo com exemplo de tratamento de XML
#

import xml.dom.minidom

def manipulaXML():
    doc = xml.dom.minidom.parse('C:\\Users\\enuch\\Documents\\Cursos\Descobrindo o python - LinkedIn\\Descubra-o-Python\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemploXML.xml')
    
    print("Nome da primeira tag: ", str(doc.firstChild.tagName))
    primeiroNome = doc.getElementsByTagName("firstname")
    print(primeiroNome[0].firstChild.nodeValue)
    
    for skill in doc.getElementsByTagName("skill"):
        print("Skill encontrado: ", skill.getAttribute("name"))
        
manipulaXML()