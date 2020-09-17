import speech_recognition as sr
from speak import speak
from dialogflow_api import get_dialog
from get_mic import get_mic_index
# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
# exit()
def bot():
    r = sr.Recognizer()

    with sr.Microphone(device_index=get_mic_index(sr)) as audio_file:
        print("Speak Please")

        r.adjust_for_ambient_noise(audio_file)
        audio = r.listen(audio_file)
        query = r.recognize_google(audio,language="ru-RU")

        print("Converting Speech to Text...")
        print("You said: " + query )
    speak(get_dialog(str(query),None))

if __name__ == "__main__":
    while True:
        bot()