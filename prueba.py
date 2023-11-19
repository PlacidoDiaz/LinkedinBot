from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Configura el driver de Selenium (por ejemplo, Chrome)
driver = webdriver.Chrome('/path/to/chromedriver')

# Abre la página web
driver.get('https://www.ejemplo.com')

# Espera a que se cargue la página y se ejecute JavaScript
time.sleep(5)

# Obtén el HTML después de la ejecución de JavaScript
html = driver.page_source

# Cierra el navegador
driver.quit()

# Analiza el HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Ahora puedes trabajar con 'soup' o guardarlo en un archivo
with open('soup_output.txt', 'w', encoding='utf-8') as file:
    file.write(str(soup))
