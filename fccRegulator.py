import readAudio

config = dict(language_code="en-US")

# take real time input & save to cloud
print("====STARTING FCC REGULATOR====")
    # prob take the time here and input so we know what it's called lol
mytime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
audio = ??????

# save transcript -- this part working!
readAudio.speech_to_text(config, audio, mytime)

# send transcript to arduino