from pydub import AudioSegment
import os
import math
import sys

def chopAudio(mypath, index, audiofile):
#    print("audiofile: " + audiofile)
    audio = AudioSegment.from_mp3(audiofile)
    index = int(index)

    ten_seconds = 10*1000
    len = audio.duration_seconds * 1000
    segments = math.ceil(len / 10.0)

    starttime = index * ten_seconds
    endtime = starttime + ten_seconds
    if (starttime > len):
        print("DONE")
        return
    # else:
    #     print("GO")
    thisseg = audio[starttime:endtime]
    thispath = os.path.join(mypath, "%d.mp3" %index)
    thisseg.export(thispath, format = "mp3")

chopAudio(sys.argv[1], sys.argv[2], sys.argv[3])

