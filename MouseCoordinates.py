import time
import keyboard
import pyautogui
import pyautogui as pag


print("Press (L) to quit and (CTRL-C) to quit")
try:
    iTrue = 0
    while iTrue == 0:
        # получение текущих координат
        x, y = pyautogui.position()
        # метод str(x) превращает число в строку а rjust(4) сдвигает его на четыре позиции вправоc
        positionStr = 'X:'+ str(x).rjust(4) +'  Y:'+ str(y).rjust(4)
        # end предотвращает добавление символа новой строки,  без  этого старые координаты удалить не получится
        print(positionStr, end = '')
        
        # escape-символ \ b стирает конец строки и чтобы удалить всю строку умножаем его на длину строки
        print('\b'*len(positionStr), end = '', flush = True)
        
        # для предотвращения мигания при выполнении цикла используем засыпание
        time.sleep(0.01)
        if keyboard.is_pressed('l'):
            time.sleep(0.5)
            print('X:'+ str(x).rjust(4) +'  Y:'+ str(y).rjust(4))


# Когда пользователь нажимает CTRL-C, выполнение программы переходит к разделу except и # Done будет напечатан с новой строки

except KeyboardInterrupt:
    print('\nDone')