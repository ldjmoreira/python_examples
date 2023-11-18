import sched
import time

schedule = sched.scheduler(time.time,time.sleep)

def soma():
    print(f'Tempo: {time.ctime()}')
    schedule.enter(4,1,soma)

soma()

schedule.run()