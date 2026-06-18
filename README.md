🎙️ Filler Word Detection System
An AI-powered tool that listens to speech audio, transcribes it, and automatically detects hesitation filler words — giving you structured JSON output with detailed counts.
- What Is This?
When people speak, they often use filler words like "um", "uh", "like", or "you know" without realizing it. This project helps identify and count those fillers automatically.

- It works in two steps:

* Speech → Text using OpenAI Whisper (AI-based transcription)\
* Text → Filler Analysis using regex-based pattern matching
* The result is a clean JSON report showing exactly how many fillers were detected and which ones.

- Why Use This?
- Coaches and teachers can analyze student or speaker fluency
- Public speakers can self-review their recordings
- Researchers can study hesitation patterns in speech
- Developers can integrate it into speech analysis pipelines

Features

- AI transcription via OpenAI Whisper (no internet required after install)
- Detects four common filler words: um, uh, like, you know Processes multiple audio files in one run
- Context-aware detection to reduce false positives (e.g., "I like it" vs filler "like")
- Outputs structured JSON for easy parsing or storage
- Includes error handling for invalid or unreadable audio files
- Tech Stack
Tool	Purpose:

- Python	Core language
- OpenAI Whisper	Speech-to-text transcription
- Regex (re module)	Filler word pattern matching
- FFmpeg	Audio decoding (required by Whisper)
- Project Structure:
- filler_word_detect or/
- │
- ├── app.py               ← Main script (run this)
- ├── requirements.txt     ← Python dependencies
- ├── README.md            ← Project documentation
- └── audios/              ← Put your audio files here
     -  ├── audio1.wav
      - ├── audio2.wav
      - └── audio3.wav
- Installation:

Step 1 — Clone or Download the Project
git clone https://github.com/your-username/filler-word-detector.git
cd filler-word-detector
Step 2 — Install Python Dependencies
pip install -r requirements.txt
This installs Whisper and all required libraries.

Step 3 — Install FFmpeg
Whisper uses FFmpeg to decode audio files. Install it based on your OS:

- Windows:

Download from https://www.gyan.dev/ffmpeg/builds/
- Extract the ZIP file
Add the bin folder path to your system's Environment Variables → PATH
macOS:

brew install ffmpeg
Linux:

sudo apt install ffmpeg
- How to Run
Place your .wav audio files inside the audios/ folder
Run the script:
python app.py
That's it! The system will process each file and print JSON output to the console.

- How It Works:
┌─────────────┐
│  Audio File │  (.wav)
└──────┬──────┘
       │
       ▼
┌──────────────────────┐
│  Whisper Transcription│  Converts speech → text
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  Transcript (Text)   │  Raw spoken words as a string
└──────────┬───────────┘
           │
           ▼
┌───────────────────────────┐
│  Regex Filler Detection   │  Scans for um, uh, like, you know
└──────────┬────────────────┘
           │
           ▼
┌──────────────────────┐
│     JSON Output      │  Counts per filler + total
└──────────────────────┘
_- visual selection
Sample Output:
For an audio file where the speaker said:

"Um, I think, uh, the project is going well, you know, and I like, uh, the results."

The output would be:

{
    "file": "audio1.wav",
    "filler_count": 4,
    "details": {
        "um": 1,
        "uh": 2,
        "you know": 1,
        "like": 0
    }
}
Screenshot 2026-06-14 201903
- Supported Audio Formats
Whisper + FFmpeg support a wide range of formats:

.wav
.mp3 
.m4a 
.flac 
.ogg 
Known Limitations:

"like" false positives — The word "like" is common in non-filler contexts ("I like this"). The contextual filter reduces but may not eliminate all false positives.
Accent sensitivity — Whisper handles most accents well, but very strong accents may reduce transcription accuracy.
Background noise — Heavy background noise can affect transcription quality. Use clean audio for best results.
Roadmap / Future Ideas:

 - Add support for more filler words (so, basically, right)
 - Generate a per-sentence filler breakdown
 - Add a confidence score per detection
 - Build a simple web UI with Flask or Streamlit
 - Export results to CSV alongside JSON
 -  Conclusion:
    This project demonstrates how AI-based speech transcription (Whisper) combined with lightweight NLP (regex) can produce a practical, useful tool — without         needing complex ML models for the analysis step. It's simple, extensible, and easy to integrate into larger speech analysis workflows.

- filler_word_detector:
    AI-powered tool that transcribes speech audio using Whisper and detects hesitation filler words (um, uh, like, you know) with regex-based NLP. Outputs             structured JSON with filler counts.
