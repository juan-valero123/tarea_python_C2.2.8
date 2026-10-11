#libreria
from machine import Pin

#Configurar el pin como salida y el sensor
led_iluminacion = Pin(2, Pin.OUT)

#El usuario introduce un valor de luz
luz = int(input("Introduce el nivel de luz actual: "))

#Filtra los valores incompatibles y muestra mensaje de error
if luz < 0 or luz > 100:
    print("Nivel erróneo en la medición de luz")
    led_iluminacion.off()
#Si el nivel es menor a 40, enciende el led
elif luz < 40: 
    print("Está oscuro. Encendiendo LED") 
    led_iluminacion.on()
#Cuando el nivel es mayor, apaga el led
else: 
    print("Hay suficiente luz. Apagando LED.") 
    led_iluminacion.off()