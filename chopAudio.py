from pydub import AudioSegment
import os

def chopAudio(audiofile, mypath):
    audio = AudioSegment.from_mp3(audiofile)

    ten_seconds = 10*1000
    len = audio.duration_seconds
    segments = ceil(len / 10.0)
    starttime = 0

    for i in range(segments):
        endtime = starttime + ten_seconds
        if(endtime > len):
             endtime = len
        thisseg = audio[starttime:endtime]
        mypath = os.path.join(mypath, "%d.mp3" %i)
        thisseg.export(mypath, format = "mp3")
        starttime = endtime

chopAudio("./lavieboheme.mp3", "./mytime")