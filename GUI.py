import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk


class App(tb.Window):
    def __init__(self):
        # Initialize the window with the Journal theme
        super().__init__(themename="journal")

        self.title("Project Workspace")
        self.geometry("500x600")

        # 1. Logo Section
        self.logo_label = tb.Label(self)
        self.logo_label.pack(pady=30)
        self.load_logo("logo.png")  # Replace with your actual filename

        # 2. Container for Buttons
        self.button_frame = tb.Frame(self)
        self.button_frame.pack(expand=True, fill=BOTH, padx=50)

        # 3. Create Buttons
        self.create_widgets()

    def load_logo(self, path):
        try:
            # Load and resize your logo
            img = Image.open(path)
            img = img.resize((150, 150), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            self.logo_label.config(image=self.photo)
        except Exception:
            # Fallback if the logo file isn't found
            self.logo_label.config(text="[ LOGO PLACEHOLDER ]", font=("Helvetica", 18))

    def create_widgets(self):
        # Webcam Button
        self.webcam_btn = tb.Button(
            self.button_frame,
            text="📷 Open Webcam",
            bootstyle=INFO,
            command=self.open_webcam
        )
        self.webcam_btn.pack(fill=X, pady=10)

        # Select Files Button
        self.files_btn = tb.Button(
            self.button_frame,
            text="📁 Select Files",
            bootstyle=SECONDARY,
            command=self.select_files
        )
        self.files_btn.pack(fill=X, pady=10)

        # Start Button (Primary action)
        self.start_btn = tb.Button(
            self.button_frame,
            text="▶ Start Process",
            bootstyle=SUCCESS,
            command=self.start_process
        )
        self.start_btn.pack(fill=X, pady=30)

    # --- Logic Placeholders ---
    def open_webcam(self):

        print("Webcam button clicked!")

    def select_files(self):
        files = filedialog.askopenfilenames()
        print(f"Selected: {files}")

    def start_process(self):
        print("Process started!")


if __name__ == "__main__":
    app = App()
    app.mainloop()