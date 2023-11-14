# Radio Stream Recorder and Transcriber

This Python script is designed to record a segment of an online radio stream, transcribe the recorded audio to text, and search for specific keywords within the transcribed text. It's particularly useful for verifying the presence of specific ads or content in a radio broadcast.

## Features

- **Recording**: Captures live audio from a specified online radio stream.
- **Transcription**: Utilizes Google Cloud Speech-to-Text API to transcribe the recorded audio.
- **Keyword Search**: Searches the transcribed text for pre-defined keywords.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3**: The script is written for Python 3.
- **ffmpeg**: Required for recording the audio stream.
- **Google Cloud Speech-to-Text API**: Necessary for transcribing the audio.
  - Set up a Google Cloud account and create a project.
  - Enable the Speech-to-Text API for your project.
  - Create a service account and download its JSON key file.
  - Install the Google Cloud Speech client library: `pip install google-cloud-speech`

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/rsemnani/radio_stream_recorder
cd radio-stream-recorder
```

## Usage

Run the script from the command line, providing the necessary arguments:

```bash
python3 radio_stream_recorder.py --stream-url "<stream_url>" --duration <duration_in_seconds> --start-time <HHMM> --date <YYMMDD> --keywords "keyword1,keyword2"
```

- `--stream-url`: URL of the radio stream.
- `--duration`: Duration to record in seconds (default is 3600 seconds).
- `--start-time`: Start time of the recording in UTC (format: HHMM).
- `--date`: Date of the recording in YYMMDD format (default is today's date).
- `--keywords`: Comma-separated list of keywords to search in the transcribed text.

Example:

```bash
python3 radio_stream_recorder.py --stream-url "https://kuer.streamguys1.com/high_icy" --duration 1200 --start-time 1500 --date 221113 --keywords "news,weather"
```

## Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -am 'Add some feature'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## License

