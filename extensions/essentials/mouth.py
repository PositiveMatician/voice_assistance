import os
import asyncio
import edge_tts
import inflect
from just_playback import Playback
import time
import re
from dotenv import load_dotenv

load_dotenv()
DEBUG: bool = os.getenv("DEBUG") == "True"

VOICE = "en-US-ChristopherNeural" 
OUTPUT_FILE = "test.mp3"
p = inflect.engine()

def _process_text(text: str) -> str:
    """Internal helper to convert digits to words."""
    words = []
    for word in text.split():
        # Strip punctuation to check if it is a number
        clean_word = re.sub(r'[^\d]', '', word)
        
        if clean_word.isdigit():
            # Convert "10" -> "ten"
            word_val = p.number_to_words(clean_word)
            words.append(word_val)
        else:
            # Keep the original word (preserves punctuation for non-numbers)
            words.append(word)
            
    return " ".join(words)

async def speak(text):
    # Generate the audio file
    communicate = edge_tts.Communicate(text, VOICE, volume="+0%", rate="+0%")
    await communicate.save(OUTPUT_FILE)
    
    # Play the audio file
    playback = Playback()
    playback.load_file(OUTPUT_FILE)
    playback.play()
    
    # Wait for playback to finish
    # We use a small sleep to prevent CPU hogging while waiting
    while playback.active:
        time.sleep(0.1)

def say(text: str) -> None:
    """Synchronous wrapper for the async speak function."""
    pt = _process_text(text)
    
    if DEBUG:
        print(f"[say] Speaking: {pt}")
        
    try:
        # asyncio.run() automatically manages the event loop lifecycle.
        # It creates a new loop, runs the task, and closes it.
        asyncio.run(speak(pt))
    except Exception as e:
        print(f"Error in speech generation: {e}")

if __name__ == "__main__":
    say("Hello! This is a test.")
    say("I can now speak multiple sentences without crashing.")
    say("The event loop is now managed correctly.")