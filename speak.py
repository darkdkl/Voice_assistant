import speechd

def speak(text):
    engine = speechd.SSIPClient('rhvoice')
    engine.set_output_module('rhvoice')
    engine.set_language('ru')
    engine.set_synthesis_voice('Elena')
    # engine.set_rate(9)
    engine.set_punctuation(speechd.PunctuationMode.SOME)

    engine.speak(str(text))
    engine.close()

if __name__ == "__main__":
    speak("Приветствую тебя,человек")