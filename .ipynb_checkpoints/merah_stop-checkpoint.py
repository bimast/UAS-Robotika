import serial
import cv2
import numpy as np

# Inisialisasi komunikasi serial
arduino = serial.Serial('COM3', 115200, timeout=1)  # Ganti 'COM3' sesuai port Arduino

# Fungsi untuk mengirim perintah ke Arduino
def send_command(action, speed=200):
    command = f"{action},{speed}\n"
    arduino.write(command.encode())
    print(f"Kirim: {command.strip()}")

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Deteksi warna merah (rentang HSV untuk merah terang)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([180, 255, 255])

    # Gabungkan dua rentang warna merah
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # Temukan kontur objek merah
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Jika objek merah terdeteksi, robot berhenti
        send_command("STOP")
        cv2.putText(frame, "STOP: Merah Terdeteksi", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    else:
        # Jika tidak ada warna merah, robot maju
        send_command("MOVE_FORWARD", 200)
        cv2.putText(frame, "MAJU", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    # Tampilkan hasil kamera dan deteksi
    cv2.imshow("AI Controller", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
