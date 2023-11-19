from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import csv
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) != 3:
    print("Uso: python selen.py <correo> <contraseña>")
    sys.exit(1)

correo = sys.argv[1]
pas = sys.argv[2]


# Crear una lista vacía para almacenar los enlaces
enlaces = []

# Abrir el archivo 'links.txt' en modo de lectura
with open('links.txt', 'r') as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        # Añadir la línea (enlace) a la lista, eliminando espacios en blanco y saltos de línea
        enlaces.append(linea.strip())

# Configuración del WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# URL de la página que deseas visitar
url = "https://www.linkedin.com"
driver.get(url)

# Esperar a que se cargue la página y que el botón esté presente
time.sleep(5)  # Ajusta este tiempo según la necesidad


# Buscar el elemento y hacer clic
try:
    
    #Introduce Correo y Contraseña
    campo_texto = driver.find_element(By.XPATH, '//*[@id="session_key"]')
    campo_texto.send_keys(correo)
    campo_texto = driver.find_element(By.XPATH, '//*[@id="session_password"]')
    campo_texto.send_keys(pas)
    
    button = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
    button.click()
    
except Exception as e:
    print("Error ", e)

time.sleep(2)

driver.get(enlaces[0])

try:   

    button = driver.find_element(By.XPATH, '//*[@id="top-card-text-details-contact-info"]')
    button.click()
    time.sleep(10)
    
    # Espera a que el modal sea visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div[data-test-modal]'))
    )
    
    enlace_email = driver.find_element(By.CSS_SELECTOR, 'a[href^="mailto:"]')
    href_email = enlace_email.get_attribute('href')
    email = href_email.replace("mailto:", "")
    
    print(email)
    
    
except Exception as e:
    print("Error ", e)
    
time.sleep(500)
