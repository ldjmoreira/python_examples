##IMPORTS BIBLIOTECAS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import schedule
import time 
## global variables
z=1
i=0
estado='first'

## functions
def launchBrowser():
    global estado
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://saudeon.giize.com/login.php")
        
        driver.find_element(By.NAME, 'email').send_keys('ldjmoreira@hotmail.com')
        driver.find_element(By.NAME, 'password').send_keys('123456')
        driver.find_element(By.CLASS_NAME, 'botao-login').click()

        driver.find_element(By.XPATH, '/html/body/aside/nav/ul/li[3]/a/div').click()
        driver.find_element(By.XPATH, '/html/body/aside/nav/ul/li[7]/a/div').click()
        driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[1]/td[5]/a').click()

        driver.find_element(By.XPATH, '//*[@id="idOfForm"]/div[1]/div[2]/div[2]/div/a').click()
        driver.find_element(By.NAME, 'evolucao').send_keys("teste automatizado, envio namente após 1 minuto1")
        driver.find_element(By.XPATH, '//*[@id="footer-vis"]/div[2]/button[1]').click()

        driver.find_element(By.XPATH, '/html/body/header/div/div[3]/div[3]/div/div/a/i').click()
        estado='first'
    except:
        print("Erro inesperado, tentaremos novamente em algum tempo1")
        schedule.cancel_job(scheduler1)
        estado='emErro'

def launchBrowserEmErro():
    global estado
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("http://saudeon.giize.com/login.php")
        
        driver.find_element(By.NAME, 'email').send_keys('ldjmoreira@hotmail.com')
        driver.find_element(By.NAME, 'password').send_keys('123456')
        driver.find_element(By.CLASS_NAME, 'botao-login').click()

        driver.find_element(By.XPATH, '/html/body/aside/nav/ul/li[3]/a/div').click()
        driver.find_element(By.XPATH, '/html/body/aside/nav/ul/li[7]/a/div').click()
        driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[1]/td[5]/a').click()

        driver.find_element(By.XPATH, '//*[@id="idOfForm"]/div[1]/div[2]/div[2]/div/a').click()
        driver.find_element(By.NAME, 'evolucao').send_keys("teste automatizado, envio namente após 1 minuto2")
        driver.find_element(By.XPATH, '//*[@id="footer-vis"]/div[2]/button[1]').click()

        driver.find_element(By.XPATH, '/html/body/header/div/div[3]/div[3]/div/div/a/i').click()
        estado='first'
    except:
        print("Erro inesperado, tentaremos novamente em algum tempo2")
        estado='emErro'


# Create a new scheduler (OBJETOS)
scheduler1 = schedule.Scheduler()
scheduler1.every(60).seconds.do(launchBrowser)

scheduler2 = schedule.Scheduler()
scheduler2.every(10).seconds.do(launchBrowserEmErro)

## MAIN ENTRY POINT
## paradigma de programação. Procedural, usando estados da aplicação
while True:

    if estado == 'first': 
        scheduler1.run_pending()
        print('Running'+str(z))
        print(datetime.now())
        time.sleep(1)
        print(estado)
        print(i)
        print(z)
        z=z+1
    if estado == 'emErro': 
        scheduler2.run_pending()
        print('Running'+str(z))
        print('Running'+str(i))
        i=i+1
        z=z+1
        print(datetime.now())
        print(estado)
        print(i)
        print(z)
        time.sleep(1)
        if i == 55:
            i=0
            estado='first'
            print('Não foi possivel bater o ponto')


    


