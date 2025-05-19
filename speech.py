from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch, librosa, uuid, os


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/transcribe")
async def transcribe(request: Request, file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    filepath = os.path.join(UPLOAD_DIR, f"{file_id}.wav")

    with open(filepath, "wb") as buffer:
        buffer.write(await file.read())

    try:
        audio, rate = librosa.load(filepath, sr=16000)
        inputs = processor(audio, sampling_rate=rate, return_tensors="pt", padding=True)
        with torch.no_grad():
            logits = model(inputs.input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)[0]
    except Exception as e:
        transcription = f"Error: {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "transcription": transcription,
        "filename": file.filename,
        "audio_url": f"/audio/{file_id}"
    })

@app.get("/audio/{file_id}")
async def get_audio(file_id: str):
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.wav")
    return FileResponse(file_path, media_type="audio/wav")
