import pyautogui
import keyboard
import ctypes
from PIL import Image
import pystyle
from pystyle import *
from pathlib import Path
import subprocess
import time

def firstlaunchings():
    print(Colorate.Horizontal(Colors.blue_to_red, Box.DoubleCube(''
                                                                 'We notice'
                                                                 ' this is the first time you launch the program')))
    print(Colorate.Horizontal(Colors.green_to_yellow, Box.DoubleCube('''What do you prefer ? : ''')))
    print(Colorate.Horizontal(Colors.green_to_yellow, 'Color One [1]'))
    print(Colorate.Horizontal(Colors.blue_to_red, 'Color Two [2]'))
    print(Colorate.Horizontal(Colors.green_to_black, 'Color Three (Hard to see sometimes [3]'))
    choose = input('Choose : ')
    if choose == '1':
        with open('data.txt', 'w', encoding="utf-8") as e:
            e.write('Colors')

    elif choose == '2':
        with open('data.txt', 'w') as e:
            e.write('Colorss')

    elif choose == '3':
        with open('data.txt', 'w') as e:
            e.write('Colorsss')

    else:
        print('Wrong Number')
        firstlaunchings()


if Path('data.txt').is_file():
    print("")
else:
    open('data.txt', 'w')
    firstlaunchings()

Keybinding = ''' 
    Autoclicker | H | Enabled
    Autoclicker | J | Disabled  
    TriggerBot  | F | Enabled
    TriggerBot  | G | Disabled'''

with open("data.txt", mode='r', encoding="utf-8") as z:
    TextColor = z.readline()
    if TextColor == 'Colors':
        TextColor = Colors.green_to_yellow
    elif TextColor == 'Colorss':
        TextColor = Colors.blue_to_red
    elif TextColor == 'Colorsss':
        TextColor = Colors.green_to_black
    else:
        print('Nope')

print('\n' * 100)

color = (255, 0, 0)
color2 = (0, 0, 0)
x = 0
y = 0

i = 1
n = 1000

autoclicker = 0
start = 0
module = 0

triggerbot = 0
pyautogui.PAUSE = 0.05
ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Is Good | Launched | https://github.com/TheCuteOwl")

Banner5 = '''
+-----------------------------------------+ 
|Autoclicker  | Working     + Update Soon | 
|             |             |             |
|TriggerBot   | Working     |             |
|             |             |             |
|Aimbot       | Working On  |             | 
|             |             |             | 
|             +             +             | 
+-----------------------------------------+ 
PRESS N FOR Help
FOR THE TRIGGERBOT YOU NEED TO USE LUNAR AND MAKE THE CROSSHAIR RED WHILE LOOKING TO A ENNEMY'''

print(Colorate.Diagonal(TextColor, Center.XCenter(Banner5 + '\n\n')))
while i < n:

    if keyboard.is_pressed('N'):
        print(Colorate.Diagonal(TextColor, Center.XCenter(Keybinding + '\n\n')))
        time.sleep(1)

    if keyboard.is_pressed('h'):
        var = autoclicker = 1
        print(Colorate.Diagonal(TextColor, 'Autoclicker Enabled'))
        module = 1
        ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Is Good | Autoclicker Enabled | https://github.com/TheCuteOwl")
        while autoclicker == 1:
            pyautogui.click()

            if keyboard.is_pressed('j'):
                while True:
                    module = 0
                    ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Is Good | Autoclicker Disabled | https://github.com/TheCuteOwl")
                    var2 = autoclicker = 0
                    print(Colorate.Diagonal(TextColor, 'Autoclicker Disabled'))
                    i = 2
                    break
    elif keyboard.is_pressed('f'):
        var3 = triggerbot = 1
        print(Colorate.Diagonal(TextColor, 'Triggerbot Enabled'))
        module = 1
        ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Is Good | Triggerbot Enabled | https://github.com/TheCuteOwl")
        while triggerbot == 1:

            x, y = pyautogui.position()
            rgb = pyautogui.pixel(x, y)
            if rgb == color:
                pyautogui.click()

            elif keyboard.is_pressed('g'):
                while True:
                    module = 0
                    ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Is Good | Triggerbot Disabled | https://github.com/TheCuteOwl")
                    var4 = triggerbot = 0
                    print(Colorate.Diagonal(TextColor, 'Triggerbot Disabled'))
                    break
