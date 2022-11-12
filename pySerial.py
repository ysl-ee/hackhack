import serial
import time

arduino = serial.Serial(port = "COM3", baudrate=115200, timeout=.1)

wordsBad = ["shit", "asshole", "bitch", "poop", "piss"]
wordsVeryBad = ["fuck", "dick", "cock", "pussy", "tits", "cunt"]

def write(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.01)
    return 0

while True:
    inputWord = input("Enter a word: ").lower()
    for i in wordsBad:
        if i in inputWord:
            write("1")
        else:
            write("0")
    for j in wordsVeryBad:
        if j in inputWord:
            write("4")
        else:
            write("0")