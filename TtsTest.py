import time
import os
from playsound import playsound

cwd = os.getcwd()

def tts(l):
    time.sleep(0)
    if l == 'A' or l == 'a':
        playsound(cwd+'/TtsLettersWav/TtsA.wav')
    if l == 'B' or l == 'b':
        playsound(cwd+'/TtsLettersWav/TtsB.wav')
    if l == 'C' or l == 'c':
        playsound(cwd+'/TtsLettersWav/TtsC.wav')
    if l == 'D' or l == 'd':
        playsound(cwd+'/TtsLettersWav/TtsD.wav')
    if l == 'E' or l == 'e':
        playsound(cwd+'/TtsLettersWav/TtsE.wav')
    if l == 'F' or l == 'f':
        playsound(cwd+'/TtsLettersWav/TtsF.wav')
    if l == 'G' or l == 'g':
        playsound(cwd+'/TtsLettersWav/TtsG.wav')
    if l == 'H' or l == 'h':
        playsound(cwd+'/TtsLettersWav/TtsH.wav')
    if l == 'I' or l == 'i':
        playsound(cwd+'/TtsLettersWav/TtsI.wav')
    if l == 'J' or l == 'j':
        playsound(cwd+'/TtsLettersWav/TtsJ.wav')
    if l == 'K' or l == 'k':
        playsound(cwd+'/TtsLettersWav/TtsK.wav')
    if l == 'L' or l == 'l':
        playsound(cwd+'/TtsLettersWav/TtsL.wav')
    if l == 'M' or l == 'm':
        playsound(cwd+'/TtsLettersWav/TtsM.wav')
    if l == 'N' or l == 'n':
        playsound(cwd+'/TtsLettersWav/TtsN.wav')
    if l == 'O' or l == 'o':
        playsound(cwd+'/TtsLettersWav/TtsO.wav')
    if l == 'P' or l == 'p':
        playsound(cwd+'/TtsLettersWav/TtsP.wav')
    if l == 'Q' or l == 'q':
        playsound(cwd+'/TtsLettersWav/TtsQ.wav')
    if l == 'R' or l == 'r':
        playsound(cwd+'/TtsLettersWav/TtsR.wav')
    if l == 'S' or l == 's':
        playsound(cwd+'/TtsLettersWav/TtsS.wav')
    if l == 'T' or l == 't':
        playsound(cwd+'/TtsLettersWav/TtsT.wav')
    if l == 'U' or l == 'u':
        playsound(cwd+'/TtsLettersWav/TtsU.wav')
    if l == 'V' or l == 'v':
        playsound(cwd+'/TtsLettersWav/TtsV.wav')
    if l == 'W' or l == 'w':
        playsound(cwd+'/TtsLettersWav/TtsW.wav')
    if l == 'X' or l == 'x':
        playsound(cwd+'/TtsLettersWav/TtsX.wav')
    if l == 'Y' or l == 'y':
        playsound(cwd+'/TtsLettersWav/TtsY.wav')
    if l == 'Z' or l == 'z':
        playsound(cwd+'/TtsLettersWav/TtsZ.wav')

mes = input()
if mes != "":
    for i in mes:
        tts(i)
