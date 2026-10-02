import cv2
import mediapipe as mp
import os
import pygame


# ==========================================
# SETTINGS
# ==========================================

VIDEO_PATH = "assets/gojo_domain.mp4"
SOUND_PATH = "assets/gojo_sound.mp3"

CAMERA_INDEX = 0


# ==========================================
# MEDIAPIPE SETUP
# ==========================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)


# ==========================================
# CAMERA SETUP
# ==========================================

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("ERROR: Camera could not be opened.")
    exit()


# ==========================================
# GOJO VIDEO SETUP
# ==========================================

if not os.path.exists(VIDEO_PATH):
    print("ERROR: Gojo video not found:")
    print(VIDEO_PATH)
    cap.release()
    exit()

gojo_video = cv2.VideoCapture(VIDEO_PATH)

if not gojo_video.isOpened():
    print("ERROR: Could not open Gojo video.")
    cap.release()
    exit()


# ==========================================
# SOUND SETUP
# ==========================================

if not os.path.exists(SOUND_PATH):
    print("ERROR: Sound file not found:")
    print(SOUND_PATH)
    cap.release()
    gojo_video.release()
    exit()

pygame.mixer.init()

pygame.mixer.music.load(SOUND_PATH)


# ==========================================
# VARIABLES
# ==========================================

domain_active = False
previous_domain_state = False


# ==========================================
# GOJO HAND SIGN
# ==========================================

def is_gojo_sign(hand):
    """
    Gojo hand sign:

    Index finger  -> UP
    Middle finger -> UP
    Ring finger   -> DOWN
    Pinky         -> DOWN
    """

    index_up = hand[8][1] < hand[6][1]

    middle_up = hand[12][1] < hand[10][1]

    ring_down = hand[16][1] > hand[14][1]

    pinky_down = hand[20][1] > hand[18][1]

    return (
        index_up
        and middle_up
        and ring_down
        and pinky_down
    )


# ==========================================
# MAIN LOOP
# ==========================================

while True:

    # --------------------------------------
    # Read camera
    # --------------------------------------

    success, camera_frame = cap.read()

    if not success:
        print("Camera frame could not be read.")
        break


    # Mirror camera
    camera_frame = cv2.flip(camera_frame, 1)

    height, width, _ = camera_frame.shape


    # --------------------------------------
    # Convert BGR -> RGB
    # --------------------------------------

    rgb = cv2.cvtColor(
        camera_frame,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------------
    # Detect hands
    # --------------------------------------

    results = hands.process(rgb)

    gojo_sign_detected = False


    # ======================================
    # PROCESS HANDS
    # ======================================

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            points = []

            for landmark in hand_landmarks.landmark:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                points.append((x, y))


            # Draw hand skeleton
            mp_draw.draw_landmarks(
                camera_frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )


            # Check Gojo sign
            if is_gojo_sign(points):

                gojo_sign_detected = True


    # ======================================
    # DOMAIN STATE
    # ======================================

    if gojo_sign_detected:

        domain_active = True

    else:

        domain_active = False


    # ======================================
    # SOUND CONTROL
    # ======================================

    # Domain just activated
    if domain_active and not previous_domain_state:

        pygame.mixer.music.play()


    # Domain just deactivated
    if not domain_active and previous_domain_state:

        pygame.mixer.music.stop()


    # Remember state
    previous_domain_state = domain_active


    # ======================================
    # GOJO DOMAIN
    # ======================================

    if domain_active:

        # Read next video frame
        video_success, domain_frame = gojo_video.read()


        # Restart video when it ends
        if not video_success:

            gojo_video.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )

            video_success, domain_frame = gojo_video.read()


        if video_success:

            # Resize video
            domain_frame = cv2.resize(
                domain_frame,
                (width, height)
            )


            # ----------------------------------
            # Blend domain video + camera
            # ----------------------------------

            output = cv2.addWeighted(
                domain_frame,
                0.75,
                camera_frame,
                0.25,
                0
            )


            # ----------------------------------
            # Purple cinematic overlay
            # ----------------------------------

            overlay = output.copy()

            cv2.rectangle(
                overlay,
                (0, 0),
                (width, height),
                (100, 0, 180),
                -1
            )

            output = cv2.addWeighted(
                overlay,
                0.15,
                output,
                0.85,
                0
            )


            # ----------------------------------
            # Domain Expansion text
            # ----------------------------------

            cv2.putText(
                output,
                "DOMAIN EXPANSION",
                (
                    width // 2 - 250,
                    70
                ),
                cv2.FONT_HERSHEY_DUPLEX,
                1.2,
                (255, 255, 255),
                3
            )


            cv2.putText(
                output,
                "UNLIMITED VOID",
                (
                    width // 2 - 210,
                    115
                ),
                cv2.FONT_HERSHEY_DUPLEX,
                1.0,
                (180, 100, 255),
                2
            )


        else:

            output = camera_frame


    # ======================================
    # NORMAL CAMERA
    # ======================================

    else:

        output = camera_frame


        cv2.putText(
            output,
            "Show Gojo Hand Sign",
            (30, 45),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )


        cv2.putText(
            output,
            "Index + Middle UP",
            (30, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (180, 180, 180),
            2
        )


    # ======================================
    # DISPLAY
    # ======================================

    cv2.imshow(
        "JJK Domain Expansion",
        output
    )


    # ======================================
    # KEYBOARD
    # ======================================

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q") or key == 27:

        break


# ==========================================
# CLEANUP
# ==========================================

cap.release()

gojo_video.release()

pygame.mixer.music.stop()

pygame.mixer.quit()

cv2.destroyAllWindows()

hands.close()
