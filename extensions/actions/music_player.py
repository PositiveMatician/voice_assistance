import os
import random
import pygame

# Initialize mixer
pygame.mixer.init()

# Path to your music folder
MUSIC_FOLDER = os.path.join(os.getcwd(), "music")

current_song = None


def play_random_music():
    global current_song

    try:
        songs = [file for file in os.listdir(MUSIC_FOLDER)
                 if file.endswith((".mp3", ".wav"))]

        if not songs:
            return "No songs found in music folder."

        current_song = random.choice(songs)
        song_path = os.path.join(MUSIC_FOLDER, current_song)

        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

        return f"Playing {current_song}"

    except Exception as e:
        return f"Error playing music: {str(e)}"
