import rpi_lcd as lcd
from time import sleep
screen=lcd.LCD()


def scroll(text: str):
    global screen
    res=text
    for i in range(0, len(text)):
        screen.text("", 1)
        screen.text(res, 2)
        res=res[1:]
        sleep(0.03125)
    screen.clear()



try:
    while True:
        ask=input("What Would You Like To Scroll?\n>>")
        scroll(ask)
except KeyboardInterrupt:
    print("\nClearing LCD...")
    screen.clear()

