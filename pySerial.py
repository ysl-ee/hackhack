import serial
import time

arduino = serial.Serial(port = "COM3", baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while True:
    word = input("Enter a word: ")
    if (word.upper() == "FUCK" or word.upper() == "FUCKING"):
        value = write_read("1")
    else:
        value = write_read("0")