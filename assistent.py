import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import datetime
from speak import speak
from get_mic import get_mic_index
from dialogflow_api import get_dialog
CONFIG = {
    "names":("семьмая","седьмая из девяти"),
    "tbr":('скажи','покажи','сколько','произнеси','повтори'),
    "cmds":{
             "ctime":("текущее время","сейчас времени"),
             "browser":("запусти браузер","открой браузер","запусти фаерфокс"),
             "test":("расскажи анекдот")

            },
    "exit_cmd":("выход","отключись","выключись","выключить","выйти") 
      }


def sorter_command(query):
    
    print(query)
    speak(get_dialog(query))
    if query.startswith(CONFIG['names']):
        cmd = query
        print(cmd)



def main():
    recog = sr.Recognizer()
    mic = sr.Microphone(device_index=get_mic_index(sr))
    print("Произнесите команду")
    while True:
        with mic as source:
            
            recog.adjust_for_ambient_noise(source)
            audio = recog.listen(source)
        try:
            query = recog.recognize_google(audio,language="ru-RU").lower()
        except sr.UnknownValueError:
            continue

        if query.startswith(CONFIG["exit_cmd"]):
            break
        sorter_command(query)
        time.sleep(0.5)

        

if __name__ == "__main__":
    main()