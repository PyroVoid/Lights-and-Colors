import time
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import cv2
import Display
import TreeSimulation as TS
from AutoMapper import Automapper
import platform

class App(tb.Window):
    def __init__(self):
        super().__init__(themename="journal")

        self.title("Project Workspace")
        self.geometry("500x600")

        self.selected_camera_index = None

        self.logo_label = tb.Label(self)
        self.logo_label.pack(pady=30)
        self.load_logo("logo.png")

        self.button_frame = tb.Frame(self)
        self.button_frame.pack(expand=True, fill=BOTH, padx=50)

        # Status Label at the very bottom
        self.status_bar = tb.Label(
            self,
            text="No camera selected",
            bootstyle=SECONDARY,
            font=("Helvetica", 9),
            anchor=W
        )
        self.status_bar.pack(side=BOTTOM, fill=X, padx=10, pady=10)

        self.create_widgets()

    def load_logo(self, path):
        try:
            img = Image.open(path)
            img = img.resize((150, 150))
            self.photo = ImageTk.PhotoImage(img)
            self.logo_label.config(image=self.photo)
        except Exception:
            self.logo_label.config(text="Lights and Colors Demo", font=("Helvetica", 18), bootstyle=INFO)

    def create_widgets(self):
        self.webcam_btn = tb.Button(
            self.button_frame,
            text="📷 Select/Open Webcam",
            bootstyle=INFO,
            command=self.webcam
        )
        self.webcam_btn.pack(fill=X, pady=10)

        self.files_btn = tb.Button(
            self.button_frame,
            text="📁 Select Files",
            bootstyle=SECONDARY,
            command=self.select_files
        )
        self.files_btn.pack(fill=X, pady=10)

        self.start_btn = tb.Button(
            self.button_frame,
            text="▶ Start Process",
            bootstyle=SUCCESS,
            command=self.start_process
        )
        self.start_btn.pack(fill=X, pady=30)

    def scan_for_cameras(self):
        available = []
        for i in range(5):
            if platform.system() == "Windows":
                cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
            else:
                cap = cv2.VideoCapture(i)
            if cap.isOpened():
                available.append(f"Camera {i}")
                cap.release()
        return available

    def webcam(self):
        self.cam_win = tb.Toplevel(self)
        self.cam_win.title("Select Camera")
        self.cam_win.geometry("300x250")
        self.cam_win.grab_set()

        tb.Label(self.cam_win, text="Scanning for devices...", font=("Helvetica", 10)).pack(pady=10)

        cameras = self.scan_for_cameras()

        if not cameras:
            tb.Label(self.cam_win, text="No cameras detected!", bootstyle=DANGER).pack(pady=10)
            return

        self.cam_choice = tb.Combobox(self.cam_win, values=cameras, state="readonly")
        if cameras:
            self.cam_choice.current(0)
        self.cam_choice.pack(pady=10, padx=20)

        tb.Button(self.cam_win, text="Connect", bootstyle=SUCCESS, command=self.confirm_camera).pack(pady=20)

    def confirm_camera(self):
        selection = self.cam_choice.get()
        self.selected_camera_index = int(selection.split()[-1])

        # Update the status bar at the bottom
        self.status_bar.config(
            text=f"Connected to: Camera {self.selected_camera_index}",
            bootstyle=SUCCESS
        )

        self.cam_win.destroy()

    def select_files(self):
        files = filedialog.askopenfilenames()
        print(f"Selected: {files}")

    def start_process(self):
        if self.selected_camera_index is None:
            # Change status bar to alert user if they forgot
            self.status_bar.config(text="Error: Please select a camera first!", bootstyle=DANGER)
            return
        print(f"Starting process with Camera {self.selected_camera_index}")
        TS.main()
        time.sleep(3)
        mapper = Automapper(self.selected_camera_index)
        coordinates = mapper.map()
        print(coordinates)

if __name__ == "__main__":
    app = App()
    app.mainloop()