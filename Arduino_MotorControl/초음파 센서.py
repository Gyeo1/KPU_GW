import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
print "Measuing Distance"
print "Press ctrl +c to stop me"
GPIO.setup(23,GPIO.OUT)#16~18번 핀을 사용한다.
GPIO.setup(24,GPIO.IN)
time.sleep(0.02)
GPIO.output(23,False)
print "Setting Trigger pin to zero by default"
time.sleep(1)
while True:
        GPIO.output(23,True)
        time.sleep(0.00001)
        GPIO.output(23,False)
        while GPIO.input(24)==0:
                start_time=time.time()
        while GPIO.input(24)==1:
                end_time=time.time()
        time=end_time-start_time
        distance=17150*time
        print "Measured Distance is:", distance ,"cms."