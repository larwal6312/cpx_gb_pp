from time import sleep
from random import seed
#from random import shuffle
from random import randint
from random import choice
from adafruit_circuitplayground.express import cpx

### NeoPixel Colors ###
white = (30, 30, 30)
red = (90, 0, 0)
yellow = (45, 45, 0)
green = (0, 90, 0)
aqua = (0, 45, 45)
blue = (0, 0, 90)
purple = (45, 0, 45)
off = (0, 0, 0)

### Color Groups ###
fade_colors = (red, green, blue)
random_colors = (white, red, yellow, green, aqua, blue, purple)

### NeoPixel Brightness Levels ###
low_light = 0.1
high_light = 0.5

### Auto_write on/off ###
autoWrite_on = True
autoWrite_off = False

def start_sound(autoWrite, brightness):
    cpx.pixels.brightness = brightness
    cpx.pixels.auto_write = autoWrite
    cpx.play_file("protonpack_start.wav")
    #cpx.play_file("Ghostbusters.mid")
    for pixel in range(10):
        cpx.pixels[pixel] = (green)
        sleep(0.4)
    cpx.pixels.fill((off))

def color_fade(autoWrite, brightness):
    cpx.pixels.auto_write = autoWrite
    cpx.pixels.brightness = brightness
    for color in fade_colors:
        cpx.pixels.fill((color))
        for level in range(1,51):
            brightness = (level * 0.01)
            cpx.pixels.brightness = brightness
            cpx.pixels.show()
        sleep(1)
        for level in range(50):
            brightness = (0.5 - (level * 0.01))
            cpx.pixels.brightness = brightness
            cpx.pixels.show()
        sleep(1)
        cpx.pixels.fill((off))
        cpx.pixels.show()

def random_lights(autoWrite, brightness):
    cpx.pixels.autoWrite = autoWrite
    cpx.pixels.brightness = brightness
    pixel_list = [0,1,2,3,4,5,6,7,8,9]
    for _ in range(15):
        rand_pixel = choice(pixel_list)
        rand_color = choice(random_colors)
        cpx.pixels[rand_pixel] = rand_color
        cpx.pixels.show()
        last_color = rand_color
        last_pixel = rand_pixel
        sleep(.5)
        cpx.pixels[rand_pixel] = off

def spinning_lights(autoWrite_off, brightness):
    cpx.pixels.auto_write = autoWrite_off
    cpx.pixels.brightness = brightness
    for _ in range(5):
        cpx.pixels[0] = white
        cpx.pixels[5] = white
        cpx.pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        cpx.pixels[1] = red
        cpx.pixels[6] = red
        cpx.pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        cpx.pixels[2] = yellow
        cpx.pixels[7] = yellow
        cpx.pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        cpx.pixels[3] = aqua
        cpx.pixels[8] = aqua
        cpx.pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        cpx.pixels[4] = purple
        cpx.pixels[9] = purple
        cpx.pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        cpx.pixels.show()

#for _ in range(1):
while True:
    if cpx.switch:
        print("loop started")
        #cpx.play_file("protonpack_start.wav")
        start_sound(autoWrite_on, high_light)
        sleep(1)
        color_fade(autoWrite_off, low_light)
        sleep(1)
        random_lights(autoWrite_on, high_light)
        sleep(1)
        spinning_lights(autoWrite_off, high_light)
