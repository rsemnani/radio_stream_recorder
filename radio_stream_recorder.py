
#!/usr/bin/env python3

"""Record, transcribe, and search for keywords in a radio stream."""

import argparse
import subprocess
import datetime
import io
from google.cloud import speech_v1 as speech

def record_stream(stream_url, duration, output_filename):
    """Record the audio stream for a specified duration."""
    # The command below uses ffmpeg to record the stream. The user needs to have ffmpeg installed.
    command = f"ffmpeg -i {stream_url} -t {duration} -acodec copy {output_filename}"
    subprocess.call(command, shell=True)

def transcribe_audio(file_path):
    """Transcribe the recorded audio file using Google Cloud Speech-to-Text API."""
    # The user needs to set up authentication for Google Cloud Speech API before using this function.
    client = speech.SpeechClient()
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    return " ".join([result.alternatives[0].transcript for result in response.results])

def search_keywords(transcribed_text, keywords):
    """Search for specific keywords in the transcribed text."""
    # This function returns a dictionary with keywords and a boolean indicating if they were found.
    return {keyword: keyword in transcribed_text for keyword in keywords}

def main():
    """Main function to parse arguments and call other functions."""
    parser = argparse.ArgumentParser(description="Record, transcribe, and search keywords in a radio stream.")
    parser.add_argument("--stream-url", type=str, required=True, help="URL of the radio stream.")
    parser.add_argument("--duration", type=int, default=3600, help="Duration to record in seconds (default: 3600).")
    parser.add_argument("--start-time", type=str, default=None, help="Start time in UTC (HHMM).")
    parser.add_argument("--date", type=str, default=datetime.datetime.now().strftime("%y%m%d"), help="Date in YYMMDD format (default: today).")
    parser.add_argument("--keywords", type=str, help="Comma-separated list of keywords to search.")

    args = parser.parse_args()

    # Output filename generation based on date and time
    output_filename = f"radio_recording_{args.date}_{args.start_time}.mp3"

    # Record the stream
    record_stream(args.stream_url, args.duration, output_filename)

    # Transcribe the audio
    transcribed_text = transcribe_audio(output_filename)

    # Search for keywords
    if args.keywords:
        keywords = args.keywords.split(",")
        found_keywords = search_keywords(transcribed_text, keywords)
        print(found_keywords)

if __name__ == "__main__":
    main()
