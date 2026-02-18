definaion = '''
function name : say()
arguements : text (str)
description : This function takes a string input and uses the pyttsx3 library to convert the
'''

import os
from dotenv import load_dotenv
load_dotenv()
DEBUG:bool = os.getenv("DEBUG") == "True"



import re
import pyttsx3
import inflect
engine = pyttsx3.init() # object creation
p = inflect.engine()


# RATE
rate = engine.getProperty('rate')   # getting details of current speaking rate
if DEBUG:
    print (rate)                        # printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate

# VOLUME
volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
if DEBUG:
    print (volume)                          # printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

# VOICE
voices = engine.getProperty('voices')       # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female



def _process_text(text: str) -> str:
    """Internal helper to convert digits to words within a sentence."""
    words = []
    for word in text.split():
        # Clean the word of punctuation to check if it's a number
        clean_word = re.sub(r'[^\d]', '', word)
        if clean_word.isdigit():
            # Convert digits to words (e.g., "10" -> "ten")
            word_val = p.number_to_words(clean_word)
            words.append(word_val)
        else:
            words.append(word)
    return " ".join(words)

def say(text: str)->None:

    # Pre-process the text to convert any numbers to words
    processed_text = _process_text(text)
    
    if DEBUG:
        print(f"Original: {text}")
        print(f"Speaking: {processed_text}")

    engine.say(processed_text)
    # engine.say('My current speaking rate is ' + str(rate))
    engine.runAndWait()
    engine.stop()

    # Saving Voice to a file
    # On Linux, make sure that 'espeak-ng' is installed
    if DEBUG:
        engine.save_to_file(processed_text, 'test.mp3')
        engine.runAndWait()

if __name__ == "__main__":
    text = "The current time is 10:05 AM"
    pt = _process_text(text)
    print(f"Processed Text: {pt}")