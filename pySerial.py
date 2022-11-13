import serial
import time
import csv

arduino = serial.Serial(port = "COM3", baudrate=115200, timeout=.1)

wordsBad = ["shit", "asshole", "bitch", "poop", "piss"]
wordsVeryBad = ["fuck", "dick", "cock", "pussy", "tits", "cunt"]
wordsIn = []
startsIn = []
endsIn = []



def write(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.01)
    return 0

with open('test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        wordsIn.append(row['Word'].lower())
        startsIn.append(row['start_time'])
        endsIn.append(row['end_time'])

print("done")

g = 0
for h in wordsIn: 
    hStart = int(startsIn[g])
    hEnd = int(endsIn[g])
    if g == 0:
        time.sleep(hStart)
    else:
        time.sleep(hStart - endsIn[g - 1])
    for i in wordsBad:
        if i in h:
            write("1")
        else:
            write("0")
    for j in wordsVeryBad:
        if j in h:
            write("4")
        else:
            write("0")
    time.sleep(hEnd - hStart)
    g += 1