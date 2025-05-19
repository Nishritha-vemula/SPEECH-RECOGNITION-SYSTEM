# SPEECH-RECOGNITION-SYSTEM

"COMPANY": CODTECH IT SOLUTIONS

"NAME": NISHRITHA VEMULA

"INTERN ID": CODF274

"DOMAIN": ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE

"DURATION": 4 WEEKS

"MENTOR" : NEELA SANTOSH



Welcome to the **Speech-to-Text Converter** – a simple yet powerful web app that allows you to transcribe `.wav` audio files into readable text using two popular methods: Facebook's **Wav2Vec2** (offline deep learning model) and **Google SpeechRecognition** (online API).

This project is built with **FastAPI** and features a clean, modern, and responsive frontend. Users can upload audio, choose the transcription engine, and instantly get the text output. It's ideal for internships, demo projects, or learning how to build a full-stack ML web app.

---

##  Features

* 🎧 Upload `.wav` audio files for transcription
* 🧠 Choose between:

  * **Wav2Vec2** (offline, deep learning-based model)
  * **Google SpeechRecognition** (online, fast & accurate)
* 📄 View transcribed text directly on the page
* 📅 Option to download the transcription as a `.txt` file
* 🖥️ Clean, mobile-responsive UI with full-screen layout and larger fonts

---

##  How It Works

1. Upload a `.wav` file via the form.
2. Select your preferred transcription model.
3. The app processes the file and returns the transcription.
4. Optionally, download the transcription result.

---

##  Tech Stack

| Layer         | Tools & Frameworks                        |
| ------------- | ----------------------------------------- |
| Backend       | FastAPI, Python                           |
| Transcription | Wav2Vec2 (HuggingFace), SpeechRecognition |
| Frontend      | HTML5, CSS3 (Jinja2 templates)            |
| Audio         | Librosa for pre-processing                |
| Hosting       | Uvicorn (ASGI server)                     |

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Nishritha-vemula/SPEECH-RECOGNITION-SYSTEM.git
cd SPEECH-RECOGNITION-SYSTEM
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn speech:app --reload
```

Now open your browser and navigate to:

```
http://127.0.0.1:8000
```

---

##  Project Structure

```
├── speech.py              # Main FastAPI application
├── templates/
│   └── index.html         # UI using Jinja2
├── static/
│   └── styles.css         # Stylesheet
├── uploads/               # Uploaded audio storage
├── requirements.txt       # Dependencies
├── .gitignore             # Git ignored files
└── README.md              # Project documentation
```

---

##  Requirements

Contents of `requirements.txt`:

```
fastapi
uvicorn
transformers
torch
librosa
speechrecognition
jinja2
python-multipart
```

Install all at once with:

```bash
pip install -r requirements.txt
```

---

##  Output

![Image](https://github.com/user-attachments/assets/79137c0c-9ebe-446f-aa11-7f89861c2be3)


##  Future Ideas

* 🎤 Add real-time microphone input transcription
* 🌐 Add support for other file types (MP3, FLAC)
* 🗣️ Include multi-language model options
* 📊 Display model confidence or accuracy

---

##  Acknowledgements

* [Wav2Vec2 on Hugging Face](https://huggingface.co/facebook/wav2vec2-base-960h)
* [Google SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [Librosa Audio Library](https://librosa.org/)
* [FastAPI Documentation](https://fastapi.tiangolo.com/)

...

Made with ❤️ by \[Nishritha Vemula]
