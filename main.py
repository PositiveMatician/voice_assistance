import extensions.essentials.ears as ears
import extensions.essentials.mouth as mouth
import extensions.essentials.brain as brain


def main():    
        thoughts = ears.listen()
        words = brain.think(thoughts)
        mouth.say(words)

if __name__ == "__main__":
    main()