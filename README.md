# 🎵 SpotDL Music Downloader GUI

A modern, sleek, and premium desktop interface for **spotDL**, built using Python and CustomTkinter. This application allows you to download your favorite Spotify tracks, albums, or playlists directly into your system's native **Music** folder with just a single click.

---

## ✨ Features
* **Modern Dark UI:** Clean, distraction-free aesthetic designed with a native Spotify-inspired green accent palette.
* **Smart Path Resolution:** Automatically detects the logged-in system user and seamlessly targets the standard `Users/YourName/Music` section without any manual path typing.
* **Asynchronous Background Processing:** Uses multi-threading to ensure the interface never freezes or says "Not Responding" while downloads are active.
* **Live Status Log:** Streams output directly from the terminal backend straight into your view so you can track download progress in real time.

---

## 🛠️ Requirements & Setup

Before running or building the application, ensure you have **Python 3.x** and **FFmpeg** configured on your operating system.

### 1. Install Python Dependencies
Open your terminal or command prompt inside the project directory and install the required modules:
```bash
pip install spotdl customtkinter pyinstaller
