import os
from google.cloud import speech
import time
from datetime import datetime

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
speech_client = speech.SpeechClient 

def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)


def print_sentences(response):
    mytime = datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
    filename = "audio_%s.txt" % mytime
    f = open(filename, 'w+')
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        S = ''.join(transcript)
        f.write(S)
        f.write('\n')
        print(f"Confidence: {confidence:.0%}")


config = dict(language_code="en-US")
audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")
speech_to_text(config, audio)