#Importar librerias y solucionar el error que da el from machine simulando un pin que funciona SOLO PARA TEST.
import time
try:
    from machine import Pin
except ImportError:
    class Pin:
        OUT = "OUT"
        def __init__(self, numero, modo=None):
            self.numero = numero
        def on(self):
            print(f"[SIMULACIÓN] LED en pin {self.numero}: ENCENDIDO")
        def off(self):
            print(f"[SIMULACIÓN] LED en pin {self.numero}: APAGADO")
            
#Configurar el pin como salida y el sensor
led_iluminacion = Pin(2, Pin.OUT)

#El usuario introduce un valor de luz
luz = int(input("Introduce el nivel de luz actual: "))

#Filtra los valores incompatibles y muestra mensaje de error
if luz < 0 or luz > 100:
    print("Nivel erróneo en la medición de luz")
    led_iluminacion.off()

#Si el nivel es menor a 30, enciende el led
elif luz < 30: 
    print("Está oscuro. Encendiendo LED") 
    led_iluminacion.on()
#Si el nivel está entre 30-70 parpadea el led
elif luz < 70:
    print("El nivel de luz está entre 30-70, el LED parpadea")
    led_iluminacion.on()
    time.sleep(2)
    led_iluminacion.off()
#Cuando el nivel es mayor a 70, apaga el led
else: 
    print("Hay suficiente luz. Apagando LED.") 
    led_iluminacion.off()
    