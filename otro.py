import os 
import time
a=0
while a <= 9:
    a=a+1
    m=1
    time.sleep(5)
    os.system("cls")
    while m <= 10:
        print (f"{m} * {a} = {a*a}")
        m=m+1
    
