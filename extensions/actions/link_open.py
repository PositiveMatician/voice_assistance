
defination = '''
function link_open(url: str) -> None:

arguments:
- url: The URL to open.

Example usage:
link_open("https://www.example.com")
'''
import os
from dotenv import load_dotenv
load_dotenv()
DEBUG:bool = os.getenv("DEBUG") == "True"




import webbrowser

def link_open(url: str) -> None:
    if DEBUG:
        print(f"Opening URL: {url}")
    webbrowser.open(url)

if __name__ == "__main__":
    # Example usage
    link_open("https://www.example.com")