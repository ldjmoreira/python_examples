from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pandas import DataFrame
from datetime import datetime
from selenium.webdriver.chrome.service import Service
import sched
import threading
from datetime import datetime
import time
from webdriver_manager.chrome import ChromeDriverManager

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from io import StringIO
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import smtplib

#https://pje.tjba.jus.br/pje/Painel/painel_usuario/advogado.seam

contador = 0

def obter_tentativa():
    global contador
    contador += 1
    return contador
 
def tarefa():  
    # Abrir navegador
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    serv = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options ,service=serv)


    driver.delete_all_cookies()
    driver.maximize_window()

    driver.get('https://pje.tjba.jus.br')
    cpf = driver.find_element(By.ID,"username") 
    cpf.send_keys('00363401547') 

    password = driver.find_element(By.ID,"password") 
    password.send_keys('DPEb@2019')    

    button = driver.find_elements(By.ID,'btnEntrar')
    button[0].click()

    time.sleep(20)
    WebDriverWait(driver, 3600).until(
        EC.presence_of_element_located((By.CLASS_NAME,'dropdown-toggle'))
    )
    logado=1
    while(logado):
        try:
            navegacao(driver)
        except:
            driver.get('https://pje.tjba.jus.br/pje/QuadroAviso/listViewQuadroAvisoMensagem.seam')
            navegacao(driver)
        print("Execução terminada.")

def navegacao(driver):
    print(datetime.now())
    menu = driver.find_elements(By.CLASS_NAME,'botao-menu')
    menu[0].click()

    time.sleep(60)

    opt_painel = driver.find_element(By.LINK_TEXT,'Painel')
    opt_painel.click()

    time.sleep(60)

    opt_representante = driver.find_elements(By.LINK_TEXT,'Painel do representante processual') 
    opt_representante[0].click()

    time.sleep(60)

    opt1 = driver.find_elements(By.CLASS_NAME,'nomeTarefa')
    opt1[0].click()

    time.sleep(60)
    
    opt2 = driver.find_elements(By.CLASS_NAME,'nomeTarefa')
    for i in range(len(opt2)):
        if (opt2[i].text == 'SALVADOR - REGIÃO METROPOLITANA'):
            value = i

    time.sleep(60)
    opt2[value].click()
    time.sleep(60)

    print("Aguardando carregamento dos processos.")

    time.sleep(60)

    text_qtd_result = driver.find_elements(By.CLASS_NAME,'text-muted')
    quantidade_de_results = text_qtd_result[3].text

    time.sleep(60)

    varinha_mgc = driver.find_elements(By.ID,'formExpedientes:distribuirExpedientes')
    varinha_mgc[0].click()

    time.sleep(360)

    WebDriverWait(driver, 3600).until(EC.element_to_be_clickable((By.CLASS_NAME, 'rich-messages')))

    msgs_entregues = driver.find_elements(By.CLASS_NAME, 'rich-messages')
    text_distribuidos = msgs_entregues[0].text
    
    

    if text_distribuidos == 'Nenhum expediente distribuído. Não há expedientes que se encaixam nos filtros das caixas, a caixa está em um período de inativação ou não há filtro configurado.':
        time.sleep(360)
        print("Nenhum processo para distribuir")
    else:
        enviar(quantidade_de_results, text_distribuidos)

    time.sleep(30)
    WebDriverWait(driver, 3600).until(EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Fechar')]"))).click()

    time.sleep(30)
    msgs_entregues = driver.find_elements(By.ID,'j_id131:atualizarPagina')
    msgs_entregues[0].click()

    time.sleep(150)
    print("Aguardando carregamento")

    #navegacao(driver)
    logado = 1


def enviar(quantidade_de_results, text_distribuidos):    
    msg = MIMEMultipart()
                    
    message = '[NÚCLEO DE CONTESTAÇÃO]\n\nOlá, aqui é o bot de distribuição de processos do PJE.\n\nEu acabei de distribuir {}.\n\nAqui estão os expedientes distribuidos:\n\n{} \n\nTchau, até mais!! \n\n'.format(quantidade_de_results, text_distribuidos)
    
    password = "Facil!!"
    msg['From'] = "ia@defensoria.ba.def.br"
    msg['To'] = "clovis.filho@defensoria.ba.def.br"
    msg['To2'] = "daniele.souza@defensoria.ba.def.br"
    msg['To3'] = "andre.souza@defensoria.ba.def.br"
    #msg['To4'] = "thales.almeida@defensoria.ba.def.br"
    #msg['To5'] = "gil.braga@defensoria.ba.def.br"

    msg['Subject'] = "[NÚCLEO DE CONTESTAÇÃO] - Nova distribuição de processos realizada"

    msg.attach(MIMEText(message, 'plain'))
        
    server = smtplib.SMTP('smtp.gmail.com: 587')
        
    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.sendmail(msg['From'], msg['To2'], msg.as_string())
    server.sendmail(msg['From'], msg['To3'], msg.as_string())
    #server.sendmail(msg['From'], msg['To4'], msg.as_string())
    #server.sendmail(msg['From'], msg['To5'], msg.as_string()) 
    server.quit()

def repeat_at_interval(scheduler, event, interval=7200, add_n=20, start_t=None):   
    #"""Adiciona 'add_n' mais chamadas ao "evento" a cada "intervalo" segundos"""
    if start_t is None:
        t = time.time()
        t = t - (t % interval) + interval
    else:
        t = start_t

    for i in range(add_n):
        scheduler.enterabs(t, 0, event)
        t += interval

    scheduler.enterabs(t - interval, 0, repeat_at_interval, kwargs={
        "scheduler": scheduler,
        "event": event,
        "interval": interval,
        "add_n": add_n,
        "start_t": t
        })


def test():
    print(datetime.now())

def main():
    scheduler  = sched.scheduler(time.time, time.sleep)
    repeat_at_interval(scheduler, test, interval=3600)
    thread = threading.Thread(target=scheduler.run)
    thread.start()
    while True:
        test()
        try:
            tarefa()
        except:
            print("Erro inesperado, tentaremos novamente em algum tempo")
        print("Execução terminada.")


if _name_ == "_main_":
    main()