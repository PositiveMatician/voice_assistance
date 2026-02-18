defination='''
function tell_time() -> None
arguements : None
description : This function retrieves the current system time, formats it into a natural language sentence, and uses the say() function to vocalize the time. It handles both hours and minutes, converting them into words for a more human-like output   
'''

import os
from dotenv import load_dotenv
load_dotenv()
DEBUG:bool = os.getenv("DEBUG") == "True"


from datetime import datetime
from extensions.essentials.mouth import say

def tell_time() -> None:
    now = datetime.now()
    
    # Get components as integers
    hour = now.hour
    minute = now.minute
    period = now.strftime("%p") # AM or PM

    # Convert 24h to 12h for the word converter
    hour_12 = hour % 12
    if hour_12 == 0: hour_12 = 12
        
    if minute == 0:
        minute_word = "o'clock"
    elif minute < 10:
        # Makes "10:05" sound like "Ten oh five" instead of "Ten five"
        minute_word = f"o {(minute)}"
    else:
        minute_word = (minute)

    # Construct the natural sentence
    time_message = f"It is currently {hour_12}, {minute_word}, {period}."
    
    say(time_message)

if __name__ == "__main__":
    tell_time()