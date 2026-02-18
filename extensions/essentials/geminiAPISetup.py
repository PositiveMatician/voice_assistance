import os
import webbrowser
from dotenv import set_key

def setup_gemini():
    """
    Guides the user to create a Gemini API Key and saves it to the .env file.
    """
    print("\n--- Gemini API Setup ---")
    print("Opening Google AI Studio to create your API Key...")
    
    # Direct link to the API key management page
    url = "https://aistudio.google.com/app/apikey"
    webbrowser.open(url)
    
    print(f"\n1. Go to: {url}")
    print("2. Click 'Create API key'.")
    print("3. Copy the key and paste it below.")
    
    api_key = input("\nEnter your Gemini API Key: ").strip()
    
    if api_key:
        env_path = ".env"
        # Create .env if it doesn't exist
        if not os.path.exists(env_path):
            with open(env_path, "w") as f:
                f.write("")
        
        # set_key from python-dotenv handles updating or adding the key
        set_key(env_path, "GEMINI_API_KEY", api_key)
        print(f"\nSuccess! GEMINI_API_KEY has been saved to {env_path}")
    else:
        print("\nSetup cancelled. No key was provided.")

if __name__ == "__main__":
    setup_gemini()