from PIL import ImageGrab
from PIL import Image
from PIL import ImageFile
import sys
import autoit
import keyboard
import mouse
import time
import win32gui

def MenuAndChat():
    image2 = ImageGrab.grab(bbox = (0, 0, 1920, 1080))
    rgb_im2 = image2.convert('RGB')
    chatR, chatG, chatB = rgb_im2.getpixel((630, 400))
    escapeR, escapeG, escapeB = rgb_im2.getpixel((904, 311))

    if chatR == 77 and  chatG == 5 and chatB == 1: # checks in chat is open
        return 'chatFalse'
    elif escapeR == 152 and escapeG == 108 and escapeB == 61: # checks if escape menu is open
        return 'menuFalse'

def Potion(xCord, yCord, potSlot):
    image = ImageGrab.grab(bbox = (300, 965, 540, 1080))
    rgb_im = image.convert('RGB')
    potionR, potionG, potionB = rgb_im.getpixel((xCord, yCord))

    if potionR == 249 and potionG == 215 and potionB == 153:
        pass
    else:
        poe = win32gui.FindWindow(None, 'Path Of Exile')
        win32gui.SetForegroundWindow(poe)
        #print('sending keystroke')
        keyboard.send(str(potSlot))
        

if __name__ == '__main__':
    while True:
        if MenuAndChat() == 'chatFalse':
            print('chat is open')
        elif MenuAndChat() == 'menuFalse':
            print('escape menu is open')
        else:
            Potion(17, 108, 1)
            Potion(63, 108, 2)
            Potion(110, 108, 3)
            Potion(157, 108, 4)
            Potion(204, 108, 5)
            if keyboard.is_pressed('f11'):
                print('quitting script')
                quit()
