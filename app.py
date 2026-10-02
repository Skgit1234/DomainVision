import cv2
import mediapipe as mp
import pygame
import time
import os

# ==========================================
# SETTINGS
# ==========================================

CAMERA_INDEX = 0

GOJO_VIDEO = "assets/gojo_domain.mp4"
GOJO_SOUND = "assets/gojo_sound.mp3"

SUKUNA_VIDEO = "assets/sukuna_domain.mp4"
SUKUNA_SOUND = "assets/sukuna_sound.mp3"

WINDOW_NAME = "DomainVision"
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540

# ==========================================
# MEDIAPIPE
# ==========================================

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.65,
    min_tracking_confidence=0.65
)

# ==========================================
# AUDIO
# ==========================================

pygame.mixer.init()

# ==========================================
# CAMERA
# ==========================================

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("ERROR: Could not open camera.")
    exit()

# ==========================================
# CREATE NORMAL WINDOW
# ==========================================

cv2.namedWindow(
    WINDOW_NAME,
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    WINDOW_NAME,
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

# ==========================================
# FINGER DETECTION
# ==========================================

def finger_states(hand_landmarks):

    lm = hand_landmarks.landmark

    # Index finger
    index = lm[8].y < lm[6].y

    # Middle finger
    middle = lm[12].y < lm[10].y

    # Ring finger
    ring = lm[16].y < lm[14].y

    # Pinky finger
    pinky = lm[20].y < lm[18].y

    return index, middle, ring, pinky


# ==========================================
# DOMAIN SIGN DETECTION
# ==========================================

def detect_domain_signs(results):

    if not results.multi_hand_landmarks:
        return "NONE"

    hand = results.multi_hand_landmarks[0]

    index, middle, ring, pinky = finger_states(hand)

    # ======================================
    # GOJO SIGN
    # Index + Middle UP
    # Ring + Pinky DOWN
    # ======================================

    if index and middle and not ring and not pinky:
        return "GOJO"

    # ======================================
    # SUKUNA SIGN
    # OPEN PALM
    # All four fingers UP
    # ======================================

    if index and middle and ring and pinky:
        return "SUKUNA"

    return "NONE"


# ==========================================
# PLAY DOMAIN VIDEO
# ==========================================

def play_domain_video(video_path, sound_path=None):

    if not os.path.exists(video_path):

        print(
            f"ERROR: Video not found: {video_path}"
        )

        return

    video = cv2.VideoCapture(video_path)

    if not video.isOpened():

        print(
            f"ERROR: Could not open video: {video_path}"
        )

        return

    # --------------------------------------
    # KEEP NORMAL WINDOW SIZE
    # --------------------------------------

    cv2.namedWindow(
        WINDOW_NAME,
        cv2.WINDOW_NORMAL
    )

    cv2.resizeWindow(
        WINDOW_NAME,
        WINDOW_WIDTH,
        WINDOW_HEIGHT
    )

    # --------------------------------------
    # GET VIDEO FPS
    # --------------------------------------

    fps = video.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 30

    frame_delay = max(
        1,
        int(1000 / fps)
    )

    # --------------------------------------
    # PLAY EXTERNAL AUDIO
    # --------------------------------------

    if sound_path and os.path.exists(sound_path):

        pygame.mixer.music.load(
            sound_path
        )

        pygame.mixer.music.play()

    # --------------------------------------
    # PLAY VIDEO
    # --------------------------------------

    while True:

        ret, frame = video.read()

        if not ret:
            break

        # Keep video inside the normal window
        cv2.imshow(
            WINDOW_NAME,
            frame
        )

        key = cv2.waitKey(
            frame_delay
        ) & 0xFF

        if key == ord("q") or key == 27:

            video.release()

            pygame.mixer.music.stop()

            cap.release()

            cv2.destroyAllWindows()

            exit()

    # --------------------------------------
    # CLEAN VIDEO
    # --------------------------------------

    video.release()

    pygame.mixer.music.stop()

    # Restore normal window size
    cv2.namedWindow(
        WINDOW_NAME,
        cv2.WINDOW_NORMAL
    )

    cv2.resizeWindow(
        WINDOW_NAME,
        WINDOW_WIDTH,
        WINDOW_HEIGHT
    )


# ==========================================
# START
# ==========================================

print()
print("==========================================")
print("             DOMAINVISION")
print("==========================================")
print()
print("GOJO   = Index + Middle")
print("SUKUNA = Open Palm")
print()
print("Window: 960 x 540")
print("Press Q or ESC to exit.")
print()
print("Camera starting...")
print()


# ==========================================
# MAIN LOOP
# ==========================================

last_trigger = 0

cooldown = 2.0

while True:

    ret, frame = cap.read()

    if not ret:

        print(
            "ERROR: Could not read camera."
        )

        break

    # --------------------------------------
    # MIRROR CAMERA
    # --------------------------------------

    frame = cv2.flip(
        frame,
        1
    )

    # --------------------------------------
    # RGB CONVERSION
    # --------------------------------------

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # --------------------------------------
    # MEDIAPIPE
    # --------------------------------------

    results = hands.process(
        rgb_frame
    )

    # --------------------------------------
    # DRAW HAND LANDMARKS
    # --------------------------------------

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    # --------------------------------------
    # DETECT HAND SIGN
    # --------------------------------------

    sign = detect_domain_signs(
        results
    )

    # --------------------------------------
    # STATUS TEXT
    # --------------------------------------

    if sign == "GOJO":

        text = "GOJO DOMAIN"

        color = (
            255,
            200,
            50
        )

    elif sign == "SUKUNA":

        text = "SUKUNA DOMAIN"

        color = (
            50,
            50,
            255
        )

    else:

        text = "SHOW HAND SIGN"

        color = (
            255,
            255,
            255
        )

    # --------------------------------------
    # MAIN STATUS
    # --------------------------------------

    cv2.putText(
        frame,
        text,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    # --------------------------------------
    # INSTRUCTIONS
    # --------------------------------------

    cv2.putText(
        frame,
        "GOJO: Index + Middle",
        (30, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 220, 255),
        2
    )

    cv2.putText(
        frame,
        "SUKUNA: Open Palm",
        (30, 120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (80, 80, 255),
        2
    )

    cv2.putText(
        frame,
        "Q / ESC = Exit",
        (30, 155),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (200, 200, 200),
        2
    )

    # --------------------------------------
    # SHOW CAMERA
    # --------------------------------------

    cv2.imshow(
        WINDOW_NAME,
        frame
    )

    # --------------------------------------
    # DOMAIN TRIGGER
    # --------------------------------------

    current_time = time.time()

    if (
        sign != "NONE"
        and current_time - last_trigger > cooldown
    ):

        last_trigger = current_time

        # ==================================
        # GOJO
        # ==================================

        if sign == "GOJO":

            print()
            print(
                "GOJO DOMAIN EXPANSION!"
            )

            play_domain_video(
                GOJO_VIDEO,
                GOJO_SOUND
            )

        # ==================================
        # SUKUNA
        # ==================================

        elif sign == "SUKUNA":

            print()
            print(
                "SUKUNA DOMAIN EXPANSION!"
            )

            play_domain_video(
    SUKUNA_VIDEO,
    SUKUNA_SOUND
)


    # --------------------------------------
    # EXIT
    # --------------------------------------

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == 27:
        break


# ==========================================
# CLEANUP
# ==========================================

cap.release()

hands.close()

pygame.mixer.music.stop()

pygame.mixer.quit()

cv2.destroyAllWindows()

print()
print("DomainVision closed.")
