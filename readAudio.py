import csv
import os
import sys

def transcribe_gcs_with_word_time_offsets(mypath, index):
    index = int(index)
    csvpath = "%s/transcribed.csv" % mypath
    speechfile = "%s/%d.mp3" %(mypath, index)
    f = open(csvpath, 'a')
    writer = csv.writer(f)

    """Transcribe the given audio file asynchronously and output the word time
    offsets."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with open(speechfile, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_word_time_offsets=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    result = operation.result(timeout=90)

    for result in result.results:
        alternative = result.alternatives[0]
        print("Transcript: {}".format(alternative.transcript))
        print("Confidence: {}".format(alternative.confidence))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time

            # print(
            #     f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
            # )
            #print("Word: %s, start_time: %s, end_time: %s" %(word, start_time.total_seconds(), end_time.total_seconds()))
            writer.writerow([word, start_time.total_seconds(), end_time.total_seconds()])

transcribe_gcs_with_word_time_offsets(sys.argv[1], sys.argv[2])