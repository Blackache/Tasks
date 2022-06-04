# Для приложений
import subprocess

# Для ссылок и запросов
import webbrowser
import re

# Открытие приложения
# subprocess.call(r'D:\Unity Hub\Unity Hub.exe',shell=True)

# Открытие ссылок и выполнение поисковых запросов
s = input('Введите ссылку или запрос: ')
if re.search(r'\.',s):
    webbrowser.open_new_tab('https://'+s)
    # Так-же можно использовать#format {}, а после .format('запрос')
else:
    webbrowser.open_new_tab('https://www.google.com/search?client=opera-gx&q=%s&sourceid=opera&ie=UTF-8&oe=UTF-8'%s)