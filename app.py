import cv2
import numpy as np
import time
import pyautogui

# Başlangıç değerleri
width, height = 640, 480
center_x = width // 2
center_y = height // 2
radius = 50
motion_detected = False
last_motion_time = 0
motion_pause_duration = 3  # 3 saniye boyunca algılama duracak
motion_threshold = 500  # Piksel farkı eşik değeri (başlangıç)

def nothing(x):
    pass

# Telefon kamerası yayını (IP adresinizi girin)
stream_url = "http://192.168.250.56:8080/video"
cap = cv2.VideoCapture(stream_url)

cv2.namedWindow("IP Kamera Yayını")
cv2.createTrackbar("X Merkezi", "IP Kamera Yayını", center_x, width, nothing)
cv2.createTrackbar("Y Merkezi", "IP Kamera Yayını", center_y, height, nothing)
cv2.createTrackbar("Yarıçap", "IP Kamera Yayını", radius, 200, nothing)
cv2.createTrackbar("Hassasiyet", "IP Kamera Yayını", motion_threshold, 2000, nothing)

prev_frame = None
motion_detection_active = True

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kameraya bağlanılamadı.")
        break

    # Trackbar değerlerini al
    center_x = cv2.getTrackbarPos("X Merkezi", "IP Kamera Yayını")
    center_y = cv2.getTrackbarPos("Y Merkezi", "IP Kamera Yayını")
    radius = cv2.getTrackbarPos("Yarıçap", "IP Kamera Yayını")
    motion_threshold = cv2.getTrackbarPos("Hassasiyet", "IP Kamera Yayını")

    # Daire alanını belirle
    mask = np.zeros(frame.shape[:2], dtype="uint8")
    cv2.circle(mask, (center_x, center_y), radius, 255, -1)

    # Daire içindeki pikselleri alın
    masked_frame = cv2.bitwise_and(frame, frame, mask=mask)
    gray_frame = cv2.cvtColor(masked_frame, cv2.COLOR_BGR2GRAY)

    if prev_frame is not None and motion_detection_active:
        # Piksel farkını hesapla
        frame_diff = cv2.absdiff(prev_frame, gray_frame)
        _, thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)
        non_zero_count = cv2.countNonZero(thresh)

        # Hareket algılama
        if non_zero_count > motion_threshold:  # Piksel farkı eşik değeri
            current_time = time.time()
            if current_time - last_motion_time > motion_pause_duration:
                print("Hareket algılandı!")
                pyautogui.press('right')  # Sağ ok tuşuna bas
                last_motion_time = current_time

    # Daireyi çiz
    cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)

    # Hareket algılamayı kapatma için mesaj
    if not motion_detection_active:
        cv2.putText(frame, "Hareket Algilama Kapali", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Görüntüyü göster
    cv2.imshow("IP Kamera Yayını", frame)

    # Çıkış ve hareket algılamayı durdurma
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('d'):
        motion_detection_active = not motion_detection_active

    # Önceki kareyi güncelle
    prev_frame = gray_frame

cap.release()
cv2.destroyAllWindows()
