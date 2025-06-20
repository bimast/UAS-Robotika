# 🤖 Robot Beroda dengan AI Deteksi Warna Merah

Proyek UAS Mata Kuliah **Robotika**  
Dibuat oleh mahasiswa Teknik Informatika sebagai implementasi robot cerdas berbasis **ESP32** dan **Python OpenCV** untuk mendeteksi objek berwarna merah dan bergerak sesuai perintah.

---

## 🎥 Dokumentasi Video

tonton dokumentasi demo lengkap di:  
🔗 [https://youtu.be/YOUTUBE_VIDEO_ID](https://youtu.be/jXUisu6m404)

---

## 🧠 Deskripsi Proyek

Robot ini mampu:
- Mendeteksi objek berwarna merah menggunakan **kamera dan OpenCV**
- Mengirim sinyal ke **ESP32** melalui komunikasi serial UART
- Mengontrol motor untuk berhenti secara otomatis
- Dapat dikembangkan lebih lanjut untuk pengenalan warna lain atau navigasi cerdas

---

## 🛠️ Teknologi & Tools

- 🐍 Python 3 (OpenCV, NumPy, PySerial)
- ⚙️ Arduino IDE + ESP32 board support
- 🎥 Kamera USB / webcam
- 🔌 Komunikasi Serial (UART via USB)

---

## 🚀 Cara Menjalankan

### 1. Setup Arduino
- Buka folder `arduino_code/`
- Upload sketch ke ESP32 via Arduino IDE
- Pastikan pin motor sesuai dengan wiring kamu

### 2. Jalankan Python
- Buka `python_ai/main.py`
- Pastikan dependensi terinstal:
  ```bash
  pip install opencv-python pyserial numpy
Sambungkan kamera dan ESP32 ke komputer

Jalankan script:

bash
Copy
Edit
python main.py
