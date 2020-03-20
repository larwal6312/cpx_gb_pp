import board
import digitalio
import neopixel
from time import sleep
from random import seed
from random import randint
from random import choice
from adafruit_circuitplayground.express import cpx

### Strip Pixels ###
pixel_pin = board.D6
pixel_count = 30
pixels = neopixel.NeoPixel(pixel_pin, pixel_count)

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
blake_colors = (red, blue, red, blue)
random_colors = (white, red, yellow, green, aqua, blue, purple)

### NeoPixel Brightness Levels ###
low_light = 0.1
high_light = 0.3

### Auto_write on/off ###
autoWrite_on = True
autoWrite_off = False

sound_count = 0

def start_sound(autoWrite, brightness, play_sound):
    pixels.brightness = high_light
    pixels.auto_write = autoWrite
    for number in range(30):
        if number <= 14:
            pixels[number] = (blue)
        elif number >= 15:
            pixels[number] = (red)
    pixels.show()
    if play_sound:
        cpx.play_file('protonpack_start.wav')
    else:
        sleep(1)
    pixels.fill((off))
    pixels.show()
    sleep(0.1)
    for _ in range(5):
        pixels.fill((blue))
        pixels.show()
        sleep(0.2)
        pixels.fill((off))
        pixels.show()
        sleep(0.1)
        pixels.fill((red))
        pixels.show()
        sleep(0.2)
        pixels.fill((off))
        pixels.show()

def start_lights(autoWrite, brightness):
    cpx.pixels.brightness = brightness
    cpx.pixels.auto_write = autoWrite
    pixels.brightness = brightness
    pixels.auto_write = autoWrite
    for color in blake_colors:
        count = 0
        for pixel in range(10):
            for _ in range(3):
                pixels[count] = (color)
                count += 1
            cpx.pixels[pixel] = (color)
            cpx.pixels.show()
            pixels.show()
            sleep(0.4)
        cpx.pixels.fill((off))
        cpx.pixels.show()
        pixels.fill((off))
        pixels.show()

def color_fade(autoWrite, brightness):
    cpx.pixels.auto_write = autoWrite
    cpx.pixels.brightness = brightness
    pixels.autoWrite = autoWrite
    pixels.brightness = brightness
    for color in blake_colors:
        cpx.pixels.fill((color))
        pixels.fill((color))
        for level in range(1,51):
            brightness = (level * 0.01)
            cpx.pixels.brightness = brightness
            pixels.brightness = brightness
            cpx.pixels.show()
            pixels.show()
        sleep(1)
        for level in range(50):
            brightness = (0.5 - (level * 0.01))
            cpx.pixels.brightness = brightness
            pixels.brightness = brightness
            cpx.pixels.show()
            pixels.show()
        sleep(1)
        cpx.pixels.fill((off))
        pixels.fill((off))
        cpx.pixels.show()
        pixels.show()

def color_grow(autoWrite, brightness):
    cpx.pixels.auto_write = autoWrite
    cpx.pixels.brightness = brightness
    pixels.auto_write = autoWrite
    pixels.brightness = brightness
    for color in blake_colors:
        pixels.fill((color))
        pixels.show()
        cpx_pixel1 = 4
        cpx_pixel2 = 5
        for _ in range(5):
            cpx.pixels[cpx_pixel1] = color
            cpx.pixels[cpx_pixel2] = color
            cpx.pixels.show()
            sleep(0.5)
            cpx_pixel1 -= 1
            cpx_pixel2 += 1
        cpx_pixel1 = 0
        cpx_pixel2 = 9
        for _ in range(5):
            cpx.pixels[cpx_pixel1] = off
            cpx.pixels[cpx_pixel2] = off
            cpx.pixels.show()
            sleep(0.5)
            cpx_pixel1 += 1
            cpx_pixel2 -= 1
    cpx.pixels.fill((off))
    cpx.pixels.show()
    pixels.fill((off))
    pixels.show()

def random_lights(autoWrite, brightness):
    cpx.pixels.autoWrite = autoWrite
    cpx.pixels.brightness = brightness
    pixels.autoWrite = autoWrite
    pixels.brightness = brightness
    cpx_pixel_list = [0,1,2,3,4,5,6,7,8,9]
    pixel_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    for _ in range(15):
        rand_cpx_pixel = choice(cpx_pixel_list)
        rand_cpx_color = choice(random_colors)
        cpx.pixels[rand_cpx_pixel] = rand_cpx_color
        #for _ in range(2):
        rand_pixel1 = choice(pixel_list)
        rand_pixel_color1 = choice(random_colors)
        rand_pixel2 = choice(pixel_list)
        rand_pixel_color2 = choice(random_colors)
        rand_pixel3 = choice(pixel_list)
        rand_pixel_color3 = choice(random_colors)
        rand_pixel4 = choice(pixel_list)
        rand_pixel_color4 = choice(random_colors)
        rand_pixel5 = choice(pixel_list)
        rand_pixel_color5 = choice(random_colors)
        rand_pixel6 = choice(pixel_list)
        rand_pixel_color6 = choice(random_colors)
        pixels[rand_pixel1] = rand_pixel_color1
        pixels[rand_pixel2] = rand_pixel_color2
        pixels[rand_pixel3] = rand_pixel_color3
        pixels[rand_pixel4] = rand_pixel_color4
        pixels[rand_pixel5] = rand_pixel_color5
        pixels[rand_pixel6] = rand_pixel_color6
        cpx.pixels.show()
        pixels.show()
        sleep(.5)
        cpx.pixels[rand_cpx_pixel] = off
        cpx.pixels.show()
        pixels[rand_pixel1] = off
        pixels[rand_pixel2] = off
        pixels[rand_pixel3] = off
        pixels[rand_pixel4] = off
        pixels[rand_pixel5] = off
        pixels[rand_pixel6] = off
        pixels.show()

def spinning_lights(autoWrite, brightness):
    cpx.pixels.auto_write = autoWrite
    cpx.pixels.brightness = brightness
    for _ in range(5):
        cpx.pixels[0] = white
        cpx.pixels[5] = white
        pixels.fill((white))
        cpx.pixels.show()
        pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        pixels.fill((off))
        cpx.pixels.show()
        pixels.show()
        cpx.pixels[1] = red
        cpx.pixels[6] = red
        pixels.fill((red))
        cpx.pixels.show()
        pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        pixels.fill((off))
        cpx.pixels.show()
        pixels.show()
        cpx.pixels[2] = yellow
        cpx.pixels[7] = yellow
        pixels.fill((yellow))
        cpx.pixels.show()
        pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        pixels.fill((off))
        cpx.pixels.show()
        pixels.show()
        cpx.pixels[3] = aqua
        cpx.pixels[8] = aqua
        pixels.fill((aqua))
        cpx.pixels.show()
        pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        pixels.fill((off))
        cpx.pixels.show()
        pixels.show()
        cpx.pixels[4] = purple
        cpx.pixels[9] = purple
        pixels.fill((purple))
        cpx.pixels.show()
        pixels.show()
        sleep(0.2)
        cpx.pixels.fill((off))
        pixels.fill((off))
        cpx.pixels.show()
        pixels.show()

while True:
    cpx.pixels.fill((off))
    pixels.fill((off))
    if cpx.switch:
        print("loop started")
        if sound_count == 0:
            play_sound = True
            sound_count += 1
        elif sound_count <= 5:
            play_sound = False
            sound_count +=1
        elif sound_count > 5:
            play_sound = True
            sound_count = 1
        start_sound(autoWrite_off, high_light, play_sound)
        start_lights(autoWrite_off, high_light)
        sleep(1)
        color_fade(autoWrite_off, low_light)
        sleep(1)
        color_grow(autoWrite_off, low_light)
        sleep(1)
        random_lights(autoWrite_on, high_light)
        sleep(1)
        spinning_lights(autoWrite_off, high_light)
