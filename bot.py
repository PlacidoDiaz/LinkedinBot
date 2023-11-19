import requests
import re
from bs4 import BeautifulSoup
import urllib.request


# URL de la página web
url = 'https://www.linkedin.com/in/davidferreraber/'

url = url + 'overlay/contact-info/'


fp = urllib.request.urlopen('https://www.linkedin.com/in/davidferreraber/overlay/contact-info/')
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

print(mystr)

"""
# Abrir un archivo en modo de escritura y guardar el contenido de soup
with open('soup_output.txt', 'w', encoding='utf-8') as file:
    file.write(str(soup))


# Expresión regular para buscar correos electrónicos
expresion_regular = '/([a-zA-Z0-9]+)([\_\.\-{1}])?([a-zA-Z0-9]+)\@([a-zA-Z0-9]+)([\.])([a-zA-Z\.]+)/g'

# Buscar correos electrónicos en el texto de la página
emails_found = re.findall(expresion_regular, mystr)

# Imprimir los correos electrónicos encontrados
for email in emails_found:
    print(email)
"""
