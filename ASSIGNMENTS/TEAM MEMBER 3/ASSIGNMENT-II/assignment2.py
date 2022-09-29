import random
import time
import winsound
duration=7000
freq=600
while(1):
    temperature=random.randint(0,100)
    humidity=random.randint(0,100)
    if temperature>50:
        print("ALERT||Detected temperature:"+str(temperature)+"°C")
        winsound.Beep(freq,duration)
    else:
        print("ALERT||stop:"+str(temperature)+"°C")
        time.sleep(1)
              
