🌀 JJK Domain Expansion — MediaPipe

A real-time computer vision project that uses Python, OpenCV, and MediaPipe to detect hand signs through a webcam and trigger a Jujutsu Kaisen-inspired Domain Expansion effect.

✨ Features

🎥 Real-time webcam input

✋ MediaPipe hand tracking

🤞 Gojo-style hand-sign detection

🌀 Unlimited Void domain video effect

🔊 Domain activation sound

🔁 Domain video automatically loops

⚡ Real-time OpenCV processing

🎮 Press Q or ESC to exit

🛠️ Technologies

Python 3.12

OpenCV

MediaPipe

NumPy

Pygame

📁 Project Structure
Dr Strange/
│
├── assets/
│   ├── gojo_domain.mp4
│   └── gojo_sound.mp3
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md

🚀 Installation
1. Create a virtual environment
python -m venv venv

2. Activate the virtual environment

Windows:

venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the project
python app.py

🎮 How To Use

Start the application.

Allow camera access if Windows asks.

Show the configured Gojo hand sign.

The Domain Expansion video will activate.

The domain sound will play.

Remove the hand sign to return to the normal camera.

Press Q or ESC to exit.

⚙️ Camera Configuration

The project currently uses:

CAMERA_INDEX = 0


If your webcam doesn't open, try:

CAMERA_INDEX = 1


or:

CAMERA_INDEX = 2

🔒 Privacy

Camera frames are processed locally by the application.

This project does not contain code that uploads the webcam feed to a remote server.

📌 Roadmap

 Webcam hand tracking

 Gojo hand-sign detection

 Unlimited Void video effect

 Domain activation sound

 Sukuna hand-sign detection

 Malevolent Shrine domain

 Better hand-sign recognition

 Cinematic transition effects

 Portal/ring visual effects

 Improved performance and FPS

 More JJK-inspired effects

⚠️ Assets & Copyright

The video and audio files inside assets/ should only be redistributed if you have the necessary rights or permission to use them.

If publishing this project publicly, consider replacing copyrighted assets with original or properly licensed assets.

⭐ Future Goal

The goal is to turn this into a real-time AR-style Domain Expansion experience using computer vision and visual effects.