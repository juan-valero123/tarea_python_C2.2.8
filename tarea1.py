#libreria
from machine import Pin, ADC

#Configurar el pin como salida y el sensor
led_iluminacion = Pin(2, Pin.OUT)
sensor_LDR = ADC(Pin(34))

#Leer el valor de luz que capta el LDR
luz = sensor_LDR.read()
print("El nivel de luz es: ", luz)

#Filtro los valores incompatibles y muestro mensaje de error
if luz < 0 or luz > 100:
    print("Nivel erróneo en la medición de luz")
    led_iluminacion.off()
#Si el nivel es menor a 50, enciende el led
elif luz < 50: 
    print("Está oscuro. Encendiendo LED") 
    led_iluminacion.on()
#Cuando el nivel es mayor, apaga el led
else: 
    print("Hay suficiente luz. Apagando LED.") 
    led_iluminacion.off()