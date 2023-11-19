from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

correo = "correo"
pas = "contraseña"


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

driver.get("https://www.linkedin.com")


time.sleep(500)
