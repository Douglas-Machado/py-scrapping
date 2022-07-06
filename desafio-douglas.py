import requests
import re
import html2text
from bs4 import BeautifulSoup

# import das variáveis do arquivo 'desafio.ini'
from configparser import ConfigParser
file = 'desafio.ini'
config = ConfigParser()
config.read(file)

# ignorando links, imagens e quebrando em apenas uma linha
html = html2text.HTML2Text()
html.ignore_links = True
html.ignore_images = True
html.single_line_break = True

# tamanho da linha do html passa a ser o tamanho total sem quebrar a linha
html.body_width = 0

# variáveis do config
url = f'{config["dev"]["url"]}douglasclaudinomachado'
start = config["dev"]["inicio"]
end = config["dev"]["fim"]

# requisição GET para a url e 'parseando' os dados com o formato lxml
def get_page():
  res = requests.get(url)
  return BeautifulSoup(res.content, "lxml").body

# recebe uma palavra e verifica se contém os textos dos parâmetros start e end
def check_word(word):
    word = word.lower()
    return re.search(rf'^{start}.*{end}$', word)

# utilizando o html2text para converter o HTML recebido em texto
tag = get_page()
print(html.handle(str(tag)))

# criando uma lista que recebe o corpo do html e separa as palavras
arr_body = [re.split("\s", s) for s in tag.strings if s != '\n']

# cada palavra na lista de palavras do 'array_body' é passada como parâmetro 
# para 'check_word' e se retornar true a palavra é inserida no array 'result'
result = [word for array in arr_body for word in array if check_word(word)]

# lista de palavras encontradas
print(result)

# quantidade de palavras encontradas
print(len(result))