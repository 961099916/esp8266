import neopixel
from machine import Pin

pin = Pin(5, Pin.OUT)
lenght = 60
np = neopixel.NeoPixel(pin, n=lenght)
while True:
    np.fill((255, 255, 255))
    np.write()
