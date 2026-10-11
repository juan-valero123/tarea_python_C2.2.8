#Importar librerias necesarias
import RPi.GPIO as GPIO
import time

#Configuracion del pin 2 como salida 
GPIO.setup(2,GPIO.OUT) 

#Encender el led del pin 2
GPIO.output(2, GPIO.HIGH)
#Espera 2 segundos
time.sleep(2)
#Apagar el led
GPIO.output(2, GPIO.LOW)

