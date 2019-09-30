import time
from random import seed, shuffle, randint
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
            sleep(0.5)
        for level in range(50):
            brightness = (0.5 - (level * 0.01))
            cpx.pixels.brightness = brightness
            cpx.pixels.show()
            sleep(0.5)
        cpx.pixels.fill((off))
        cpx.pixels.show()
        sleep(0.5)

def random_lights(autoWrite, brightness):
    cpx.pixels.autoWrite = autoWrite
    for loop in range(5):
        seed(loop)
        sequence = [i for i in range(10)]
        shuffle(sequence)
        cpx.pixels.brightness = brightness
        for num in range(10):
            pixel_num = sequence
            seed(num)
            color = randinit(0,7)
            cpx.pixels[pixel_num] = (color)
            cpx.pixels.show()
            sleep(0.5)

while true:
    start_sound(autoWrite_on, high_light)
    sleep(2)
    color_fade(autoWrite_off, low_light)
    sleep(2)
    random_lights(autoWrite_off, low_light)
