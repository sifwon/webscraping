from time import sleep
target_time=11
def up_timer(secs):
    for i in range(0,secs):
        print(i)
        sleep(1)  
        
up_timer(target_time)