from gpiozero import MCP3008
from gpiozero import LED
import time
pump0 = LED(17)
pump1 = LED(21)
pump2 = LED(27)
pump3 = LED(22)

from tkinter import *

root=Tk()

def run():
   while(1):
    adc0=MCP3008(channel=0,device=0)
    adc1=MCP3008(channel=1,device=0)
    adc2=MCP3008(channel=2,device=0)
    adc3=MCP3008(channel=3,device=0)
    
    
    
    sensor0=int(adc0.value*1023)
    sensor1=int(adc1.value*1023)
    sensor2=int(adc2.value*1023)
    sensor3=int(adc3.value*1023)
  
    
    def percent(x):
        return ((1023-x)/603)*100
    
    
    
    if(percent(sensor0) >=0 and percent(sensor0)<40):
        print("Pump is running",int(percent(sensor0)))
        pump0.on()
        
    else:
        print("Pump is closed",int(percent(sensor0)))
        pump0.off()
        
        
    
    if(percent(sensor1) >=0 and percent(sensor1)<40):
        print("Pump is running",int(percent(sensor1)))
        pump1.on()
        
    else:
        print("Pump is closed",int(percent(sensor1)))
        pump1.off()    
    
    
    if(percent(sensor2) >=0 and percent(sensor2)<40):
        print("Pump is running",int(percent(sensor2)))
        pump2.on()
        
    else:
        print("Pump is closed",int(percent(sensor2)))
        pump2.off()
        
    
    if(percent(sensor3) >=0 and percent(sensor3)<40):
        print("Pump is running",int(percent(sensor3)))
        pump3.on()
        
    else:
        print("Pump is closed",int(percent(sensor3)))
        pump3.off()    
     
    time.sleep(1)


def stop():
   pump0.off()
   pump1.off()
   pump2.off()
   pump3.off()
Button(text="run",command=run).pack()
Button(text="stop",command=stop).pack()
root.mainloop()
