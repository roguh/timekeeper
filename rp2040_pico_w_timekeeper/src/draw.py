import random
import time

import adafruit_framebuf
from Pico_ePaper_2in66 import EPD_2in66

PIXEL_FORMAT = adafruit_framebuf.MVLSB

BIRDS = [
    r"               \\                                ",
    r"       \\      (o>                               ",
    r"       (o>     //\                               ",
    r"_______(()_____V_/_______________________________",
    r"       ||      ||                                ",
    r"               ||                                ",
]

HUMM = [[
    r"                     ,_                        ",
    r"                      :`.            .--._     ",
     "                       `.`-.        /  ',-\"\"\"\"'",
     "                         `. ``~-._.'_.\"/       ",
    r"                           `~-._ .` `~;        ",
    r"                                ;.    /        ",
    r"                               /     /         ",
    r"                          ,_.-';_,.'`          ",
     '                           `"-;`/              ',
    r"                             ,'`               ",
], [
    r"                                               _'  ",
    r"                            _.--.            .`:   ",
     "                       '\"\"\"\"-,'  \\        .-`.`    ",
     "                               \\\"._'._.-~`` .`     ",
    r"                               ;~` `. _.-~`        ",
    r"                               \    .;             ",
    r"                                \     \            ",
    r"                                 `'.,_;'-._.       ",
    r'                                     \`;-"`        ',
    r"                                      `',          ",
]]


def draw(current_time):
    epd = EPD_2in66()
    image = adafruit_framebuf.FrameBuffer(epd.buffer_Landscape, epd.height, epd.width, PIXEL_FORMAT)
    image.fill(0x00)

    line_height = 10
    y = 0
    image.text("                  RPi Pico Zero", 10, y, 0xFF, font_name='./assets/font5x8.bin')
    y += line_height
    size = 2
    image.text("Felina forever <3", 10, y, 0xFF, font_name='./assets/font5x8.bin', size=size)
    y += line_height * size
    time_y = y
    for line in current_time.split():
        size = 3
        image.text(line, 10, y, 0xFF, font_name='./assets/font5x8.bin', size=size)
        y += line_height * size

    y += line_height * size
    for line in BIRDS:
        image.text(line, 7, y, 0xFF, font_name='./assets/font5x8.bin')
        y += line_height * 2 // 3

    y = time_y + line_height // 2
    for line in HUMM[1]: #random.choice(HUMM):
        image.text(line, 7, y, 0xFF, font_name='./assets/font5x8.bin')
        y += line_height

    epd.reset()
    epd.init(0)
    print("Clearing screen")
    epd.Clear(0xFF)
    time.sleep(0.2)
    print("Drawing pic")
    epd.display_Landscape(epd.buffer_Landscape)
    print("Drawing done. Putting screen to sleep")
    epd.sleep()
