import time
import speech_recognition

sr = speech_recognition.Recognizer()


print('Please wait',end='')
s = '...'
for x in s:
    time.sleep(2)
    print(x,end='')
#region TextFromCommands
commands_dict = {
    'commands':{
        'greeting':['привет'],
        'create_task':['добавить', 'создать']
    }
}
#endregion

#region Command
def greeting():
    return 'И тебе привет'
def create_task():
    print('what?: ')
    query = listen_command()
    with open('new.txt','a') as file:
        file.write(f'{query}\n')
    return f'end'
#endregion

#region MainProgram
def listen_command():
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic)
            audio = sr.listen(source = mic)
            query = sr.recognize_google(audio_data=audio,language='ru_RU').lower()
            return query
    except speech_recognition.UnknownValueError:
        return 'Не удалось распозвать речь. Повторите попытку'
def main():
    query = listen_command()
    for k,v in commands_dict['commands'].items():
        if query in v:
            print(globals()[k]())
if __name__ == '__main__':
    main()
#endregion