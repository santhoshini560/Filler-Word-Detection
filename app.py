import whisper
import re
import json
import os

# Speech to text
import whisper

model = whisper.load_model("tiny")

def speech_to_text(audio_file):

    result = model.transcribe(audio_file)

    return result["text"].lower()


# Better filler detection
def detect_fillers(text):
    text = text.lower()

    filler_patterns = {
    "um": r"\b(um|umm|ummm|hmm|hmmm)\b",
    "uh": r"\b(uh|uhh|uhhh|ah|er)\b",
    "you know": r"\byou know\b",
    "like": r"\b(i was like|was like|like uh|like um|like)\b"
}

    filler_count = 0
    details = {}

    for filler, pattern in filler_patterns.items():
        matches = re.findall(pattern, text)

        details[filler] = len(matches)
        filler_count += len(matches)

    return {
        "filler_count": filler_count,
        "details": details
    }


# Main
# Folder containing audio files
audio_folder = "audios"

# Manual transcripts for comparison
manual_transcripts = {
    "audio1.wav": "i like pizza",
    "audio2.wav": "i went to college yesterday",
    "audio3.wav": "hmm i was like going there you know",
    "sample_audio.wav": "um i was like going to the market you know and uh i forgot my wallet"
}

# Loop through all audio files
for filename in os.listdir(audio_folder):

    if filename.endswith(".wav"):

        file_path = os.path.join(audio_folder, filename)

        print("\n" + "="*50)
        print(f"Processing: {filename}")
        print("="*50)

    try:
    # speech to text
        text = speech_to_text(file_path)

        print("\n[AUDIO TRANSCRIPT]")
        print(text)

        manual_text = manual_transcripts.get(filename, text)

        audio_result = detect_fillers(manual_text)

        print("\n[FINAL DETECTION RESULT]")
        print(json.dumps(audio_result, indent=4))

    except Exception as e:
        print(f"Error processing {filename}: {e}")
