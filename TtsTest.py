import time
import os
from playsound import playsound

cwd = os.getcwd()

def tts(l):
    letter = l.upper()
    time.sleep(0)
    if letter.isalpha() and len(letter) == 1:
        sound_file = os.path.join(
            cwd,
            "TtsLettersWav",
            f"Tts{letter}.wav"
        )
        playsound(sound_file)

mes = input()
if mes != "":
    for i in mes:
        tts(i)
