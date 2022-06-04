import time
import pyautogui as pag
import keyboard

def Pause():
    iTrue = 0
    while iTrue == 0:
        # Любой код который должен выполняться
        if keyboard.is_pressed('l'): # Кнопка на которую запускаеться пауза
            print('pause')
            time.sleep(0.2) # Задержка после нажатия паузы(что-бы сразу не снялось с паузы или наоборот)
            i=0
            while i==0:
                # Любой код который будет происходить пока стоит пауза(можно не чего не писать)
                if keyboard.is_pressed('l'): # Тоже кнопка
                    time.sleep(0.2) # Тоже задержка
                    print('not pause')
                    Pause()
Pause()