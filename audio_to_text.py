from vosk import Model, KaldiRecognizer
import wave
import os
import json
model_path = r"...vosk-model-uk-v3" #path to the model - downloaded from here https://alphacephei.com/vosk/models
model = Model(model_path)
audio_path = r"...dictaphone.audio.wav" #path to the recorded audio
output_path = r"...transcription.txt" #output folder path
with wave.open(audio_path, "rb") as wf:
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() != 16000:
        print("Audio file must be WAV format mono PCM at 16kHz.")
        exit(1)

    recognizer = KaldiRecognizer(model, wf.getframerate())

    print("Transcribing audio...")
    full_transcription = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            full_transcription.append(result.get("text", "")) #json to txt

    final_result = json.loads(recognizer.FinalResult())
    full_transcription.append(final_result.get("text", ""))

full_text = " ".join(filter(None, full_transcription))

with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Transcription saved to: {output_path}")