import audio_to_text
import text_to_pdf
import os

os.system("cls")

print("AUDIO NOTES MAKER")
print("-------------------")

fpath = input("Enter the path to your file: ")

transcript = audio_to_text.audio_spliting_transcription(file_path=fpath)
text_to_pdf.text_to_pdf(transcript, audio_to_text.FOLDER_NAME)
