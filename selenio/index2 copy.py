from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule
import time 
z=1
def launchBrowser():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("http://saudeon.giize.com/login.php")
    
    driver.find_element(By.NAME, 'email').send_keys('ldjmoreira@hotmail.com')
    driver.find_element(By.NAME, 'password').send_keys('123456')
    driver.find_element(By.CLASS_NAME, 'botao-login').click()

    driver.find_element(By.XPATH, '/html/body/aside/nav/ul/li[3]/a/div').click()
    driver.find_element(By.XPATH, '/html/body/aside/nav/ul/li[7]/a/div').click()
    driver.find_element(By.XPATH, '//*[@id="myTable"]/tbody/tr[1]/td[5]/a').click()

    driver.find_element(By.XPATH, '//*[@id="idOfForm"]/div[1]/div[2]/div[2]/div/a').click()
    driver.find_element(By.NAME, 'evolucao').send_keys("teste automatizado, envio namente após 1 minuto")
    driver.find_element(By.XPATH, '//*[@id="footer-vis"]/div[2]/button[1]').click()

    driver.find_element(By.XPATH, '/html/body/header/div/div[3]/div[3]/div/div/a/i').click()
   


schedule.every(10).seconds.do(launchBrowser)

i=0
while True:
    schedule.run_pending()
    print('Running'+str(i))
    i=i+1
    
    time.sleep(1)

