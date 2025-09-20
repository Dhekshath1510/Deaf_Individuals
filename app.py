from flask import Flask, request, jsonify
import speech_recognition as sr
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder to temporarily store uploaded audio
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Deaf Individuals Speech-to-Text API is running on Render!"

@app.route("/upload", methods=["POST"])
def upload_wav():
    """
    Accepts audio file (WAV) via POST, converts to text, returns JSON.
    """
    file_path = None

    # 1️⃣ Multipart file upload (ESP32 can send like this)
    if "file" in request.files:
        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "No selected file"}), 400
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

    # 2️⃣ Raw audio data sent in POST body
    elif request.data:
        filename = "audio.wav"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        with open(file_path, "wb") as f:
            f.write(request.data)

    else:
        return jsonify({"error": "No audio data received"}), 400

    # 3️⃣ Convert audio to text
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    except sr.UnknownValueError:
        text = "Could not understand audio"
    except sr.RequestError:
        text = "Speech API unavailable"
    except Exception as e:
        text = f"Error: {str(e)}"

    # 4️⃣ Delete temporary file
    if file_path and os.path.exists(file_path):
        os.remove(file_path)

    return jsonify({"text": text})


if __name__ == "__main__":
    # Render automatically sets PORT, fallback to 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
