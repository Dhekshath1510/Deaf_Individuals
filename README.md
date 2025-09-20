IoT-Based Assistive Speech-to-Text System for Deaf People
📌 Project Overview

This project is designed to help deaf and hard-of-hearing individuals by converting spoken language into readable text in real-time. It uses an ESP32-S3 with an I2S MEMS microphone to capture spoken audio, which is then transmitted to a cloud-based Python server for speech-to-text processing. The recognized text is sent back to the ESP32 and displayed on a Waveshare OLED screen.

🎯 Features

Real-time speech-to-text conversion.

Cloud-based Python backend using Flask + SpeechRecognition.

ESP32-S3 captures audio and communicates over Wi-Fi.

Portable and low-power IoT design.

OLED display shows recognized speech clearly.

🛠️ Components Used

ESP32-S3 (Wi-Fi enabled microcontroller)

I2S MEMS Microphone (for audio input)

Waveshare OLED Display (for text output)

Cloud Service (Render/Deta/AWS to host Python API)

⚙️ Workflow

ESP32-S3 records audio via I2S MEMS microphone.

Audio is saved in .wav format and uploaded to the cloud server.

The cloud server runs Python SpeechRecognition to convert speech into text.

Text is sent back to ESP32-S3 over Wi-Fi.

ESP32-S3 displays text on OLED for the user to read.

🚀 Applications

Assistive device for deaf and hard-of-hearing individuals.

Real-time classroom/meeting communication aid.

Smart IoT-based accessibility tool.
