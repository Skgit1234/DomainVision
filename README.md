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
Character	Hand Sign
🌀 Gojo	Index + Middle fingers up
🔥 Sukuna	Open palm
🛠️ Technologies

Python

OpenCV

MediaPipe

NumPy

Pygame

MoviePy

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

Create and activate a virtual environment:

python -m venv venv


Windows:

venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run the project:

python app.py

🎮 Controls

Gojo: Show index + middle fingers

Sukuna: Show an open palm

Q / ESC: Exit the application

🔒 Privacy

DomainVision processes the webcam feed locally through OpenCV and MediaPipe. The application does not contain code that uploads the webcam feed to a remote server.

⚠️ Disclaimer

This is a fan-made educational project inspired by Jujutsu Kaisen. Character names, concepts, and media belong to their respective rights holders.

👨‍💻 Author

Sarvesh Kundale

Built with Python, OpenCV and MediaPipe.