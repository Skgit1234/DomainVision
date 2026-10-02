⚡ DomainVision

A real-time Jujutsu Kaisen-inspired Domain Expansion project using Python, OpenCV, and MediaPipe.

DomainVision detects hand signs through your webcam and triggers different Domain Expansion videos.

✨ Features

🎥 Real-time webcam hand tracking

🌀 Gojo Domain Expansion

🔥 Sukuna Domain Expansion

🖐️ Simple hand-sign controls

🔊 Domain-specific audio

⚡ Real-time detection using MediaPipe

🖥️ Normal 960×540 playback window

🎬 Videos play at their original FPS

🖐️ Hand Signs
Character Hand Sign
🌀 Gojo Index + Middle fingers up
🔥 Sukuna Open palm

🛠️ Technologies
🐍 Python
   └── Core programming language

👁️ OpenCV
   └── Webcam capture and video processing

✋ MediaPipe
   └── Real-time hand landmark detection

🔢 NumPy
   └── Numerical and image-data processing

🔊 Pygame
   └── Domain audio playback

🎬 MoviePy
   └── Audio extraction from domain videos


📁 Project Structure
DomainVision/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── assets/
    ├── gojo_domain.mp4
    ├── gojo_sound.mp3
    ├── sukuna_domain.mp4
    └── sukuna_sound.mp3

🚀 Setup

1. Create a virtual environment
   python -m venv venv

2. Activate the virtual environment

Windows:

venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run the project
   python app.py

🎮 Controls

🌀 Gojo: Show index + middle fingers

🔥 Sukuna: Show an open palm

❌ Q / ESC: Exit the application

🔒 Privacy

DomainVision processes the webcam feed locally through OpenCV and MediaPipe. The application does not contain code that uploads the webcam feed to a remote server.

⚠️ Disclaimer

This is a fan-made educational project inspired by Jujutsu Kaisen. Character names, concepts, and media belong to their respective rights holders.
