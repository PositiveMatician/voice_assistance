import os
import rich
import speech_recognition as sr

import os
from dotenv import load_dotenv
load_dotenv()
DEBUG:bool = os.getenv("DEBUG") == "True"


def listen(OUTPUT=DEBUG) -> str:
    """Function to listen from microphone and recognize speech using Google Speech Recognition."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        rich.print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)
        
        rich.print("Say something!")
        audio = r.listen(source)
    try:
        recognized_text = r.recognize_google(audio)
        return recognized_text
    except sr.UnknownValueError:
        rich.print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        rich.print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
    
if __name__ == "__main__":
    response = listen()
    rich.print("Recognized Text:", response)