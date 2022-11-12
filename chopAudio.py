from pydub import AudioSegment
import os
import math

def chopAudio(audiofile, mypath):
    audio = AudioSegment.from_mp3(audiofile)

    ten_seconds = 10*1000
    len = audio.duration_seconds * 1000
    segments = math.ceil(len / 10.0)
    starttime = 0
    endtime = starttime + ten_seconds

    # thisseg = audio[starttime:endtime]
    # thisseg.export("./test2/one.mp3", format = "mp3")

    # starttime = endtime
    # endtime = starttime + ten_seconds

    # thisseg2 = audio[starttime:endtime]
    # thisseg2.export("./test2/two.mp3", format = "mp3")
    i = 1

    while (endtime < len + ten_seconds):
        print("starttime: %d" % starttime)
        print("endtime: %d" % endtime)
        if(endtime > len):
             endtime = len
        thisseg = audio[starttime:endtime]
        newpath = os.path.join(mypath, "%d.mp3" %i)
        thisseg.export(newpath, format = "mp3")
        starttime = endtime
        endtime = starttime + ten_seconds
        i = i+1

chopAudio("./lavieboheme.mp3", "./mytime2")