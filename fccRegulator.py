import readAudio
import time
from datetime import datetime

config = dict(language_code="en-US")
mytime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')


# chop up audio into small chunks

# # take real time input & save to cloud
# print("====STARTING FCC REGULATOR====")
#     # prob take the time here and input so we know what it's called lol
# mytime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
# audio = ??????
#change filename things to number

# save transcript -- this part working!
readAudio.speech_to_text(config, audio, mytime)

# read text files (like every 30 sec or smth)

# detect bad words!

# send hardware output to arduino