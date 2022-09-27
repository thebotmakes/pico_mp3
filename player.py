from dfplayermini import Player
from machine import Pin, SPI
from time import sleep

music = Player(pin_TX=Pin(0), pin_RX=Pin(1))

print("set volume")
music.volume(10)

x = 1

while x < 11:
    print("start play")
    music.play(x)
    print('Playing track ' + str(x))
    sleep(120)                          # note this test code only plays the first two minutes of each track - this can be updated with proper track lengths
    x += 1

print('the end')
