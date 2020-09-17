

def get_mic_index(sr):
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "USB Device" in name and int(index):
            return index

if __name__ == "__main__":
    import speech_recognition as sr
    print(get_mic_index(sr))