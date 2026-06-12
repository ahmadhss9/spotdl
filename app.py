import os
import sys
import subprocess
import threading
from pathlib import Path
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class SpotDLGui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SpotDL Music Suite")
        self.geometry("600(x)420".replace("(x)", "x")) # Formatting fix for string geometry
        self.resizable(False, False)
        self.music_dir = str(Path.home() / "Music")

        self.title_label = ctk.CTkLabel(self, text="🎵 SpotDL Downloader", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=20)

        self.entry_link = ctk.CTkEntry(self, width=460, placeholder_text="Paste Spotify link here...")
        self.entry_link.pack(pady=10)

        self.download_btn = ctk.CTkButton(self, text="Download to Music Folder", font=ctk.CTkFont(size=14, weight="bold"), command=self.start_download_thread)
        self.download_btn.pack(pady=10)

        self.status_text = ctk.CTkTextbox(self, width=500, height=180)
        self.status_text.pack(pady=15)
        self.status_text.insert("0.0", f"Ready. Saving directly to:\n{self.music_dir}\n\n")
        self.status_text.configure(state="disabled")

    def log(self, text):
        self.status_text.configure(state="normal")
        self.status_text.insert("end", text + "\n")
        self.status_text.see("end")
        self.status_text.configure(state="disabled")

    def start_download_thread(self):
        url = self.entry_link.get().strip()
        if not url:
            self.log("❌ Please enter a Spotify link first.")
            return
        self.download_btn.configure(state="disabled", text="Processing...")
        threading.Thread(target=self.run_spotdl, args=(url,), daemon=True).start()

    def run_spotdl(self, url):
        self.log(f"⏳ Starting download process...")
        cmd = [sys.executable, "-m", "spotdl", "download", url]
        try:
            process = subprocess.Popen(cmd, cwd=self.music_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None: break
                if output:
                    clean = output.strip().replace("[0m", "").replace("[32m", "")
                    if clean: self.log(clean)
            if process.poll() == 0:
                self.log("\n🎉 Done! Check your standard Windows Music section.")
            else:
                self.log("\n❌ Process finished with warning or error code.")
        except Exception as e:
            self.log(f"\n❌ Error: {str(e)}")
        finally:
            self.download_btn.configure(state="normal", text="Download to Music Folder")

if __name__ == "__main__":
    SpotDLGui().mainloop()