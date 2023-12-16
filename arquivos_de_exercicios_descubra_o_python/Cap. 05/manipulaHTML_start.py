# 
# Exemplo de processamento e parse de HTML
#
from html.parser import HTMLParser

class meuParser(HTMLParser):
    def handle_starttag(self, tag, attrs) -> None:
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:
            for a in attrs:
                print(" Valores encontrados: ", a[0], " = ", a[1])
                
    def handle_endtag(self, tag: str) -> None:
        print("Tag de fechamento encontrada!")
        
    def handle_comment(self, data: str) -> None:
        print("Comentário encontrado")
        
    def handle_data(self, data: str) -> None:
        print("Valores encontrados.")
        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)
            
def meuObjeto():
    meuparser1 = meuParser()
    arquivo = open("C:\\Users\\enuch\\Documents\\Cursos\\Descobrindo o python - LinkedIn\\Descubra-o-Python\\arquivos_de_exercicios_descubra_o_python\\Cap. 05\\exemplohtml.html", 'r')
    dados = arquivo.read()
    meuparser1.feed(dados)
    
meuObjeto()