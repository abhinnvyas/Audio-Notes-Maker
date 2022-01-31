import speech_recognition as sr  # for converting our audio to text
from pydub import AudioSegment  # for opening our audio files
# for splitting our audio file at silence points
from pydub.silence import split_on_silence
import os

FOLDER_NAME = ""


speech_recognizer = sr.Recognizer()


def audio_transcription(file):
    with sr.AudioFile(file) as source:
        data = speech_recognizer.record(source)

        try:
            text = speech_recognizer.recognize_google(data)
        except sr.UnknownValueError as err:
            return " "
        else:
            return text


def audio_spliting_transcription(file_path):

    global FOLDER_NAME

    # split the audio file into small chunks based on silence

    # audio = AudioSegment.from_file(file_path, ftype)

    print(f"[*] Opening your File: {file_path}")

    audio = AudioSegment.from_wav(file_path)

    print(f"[*] Splitting your Audio where ever there is Silence")
    audio_chunks = split_on_silence(audio,
                                    min_silence_len=500,
                                    silence_thresh=audio.dBFS-14,
                                    keep_silence=500)

    FOLDER_NAME = file_path.split(".")[0]

    if not os.path.isdir(FOLDER_NAME):
        print(f"[*] Created Folder: {FOLDER_NAME}")
        os.mkdir(FOLDER_NAME)

    transcript = ""

    print(f"[*] Total number of Chunks created: {len(audio_chunks)}")

    for i, chunk in enumerate(audio_chunks, start=1):

        chunk_filename = os.path.join(FOLDER_NAME, f"chunk{i}.wav")
        chunk.export(chunk_filename, format="wav")
        print(f"[*] Saved Chunk: {chunk_filename}")

        # save each chunk and then transcript each chunk individually
        print(f"[*] Transcribing : {chunk_filename}")
        tmp_text = audio_transcription(chunk_filename)
        transcript += tmp_text

    return transcript


# print(audio_spliting_transcription("TestAudio/test_audio.wav"))
# print(audio_transcription("TestAudio/test_audio.wav"))
