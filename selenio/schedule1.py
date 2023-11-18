import schedule
import time 

def roda_minha_funcao():
    print('olha estou rodando esse funcao')

schedule.every(5).seconds.do(roda_minha_funcao)

while True:
    schedule.run_pending()
    print('Running')
    time.sleep(1)