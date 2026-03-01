import time
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import cv2
from Display import Display
import TreeSimulation as TS
from AutoMapper import Automapper
import platform
from TreeSimulation import Tree

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

        # Image display area (under buttons)
        self.image_label = tb.Label(self)
        self.image_label.pack(pady=20)

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
            self.logo_label.config(text="Auto Lights", font=("Helvetica", 18), bootstyle=INFO)

    def create_widgets(self):
        self.webcam_btn = tb.Button(
            self.button_frame,
            text="Select/Open Webcam",
            bootstyle=INFO,
            command=self.webcam
        )
        self.webcam_btn.pack(fill=X, pady=30)

        self.calibrate_btn = tb.Button(
            self.button_frame,
            text="Calibrate Lights",
            bootstyle=DANGER,
            command=self.calibrate_process
        )
        self.calibrate_btn.pack(fill=X, pady=30)

        self.files_btn = tb.Button(
            self.button_frame,
            text="📁 Select Files",
            bootstyle=SECONDARY,
            command=self.select_files
        )
        self.files_btn.pack(fill=X, pady=30)

        self.change_lights_btn = tb.Button(
            self.button_frame,
            text="Change Lights",
            bootstyle=SUCCESS,
            command=self.change_lights
        )
        self.change_lights_btn.pack(fill=X, pady=30)

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
        self.file = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )

        if not self.file:
            return

        try:
            self.img = Image.open(self.file)

            # Resize image to fit window nicely
            self.img.thumbnail((400, 300))

            self.selected_image = ImageTk.PhotoImage(self.img)

            # Display image
            self.image_label.config(image=self.selected_image)

            # Optional: update status bar
            self.status_bar.config(text="Image loaded successfully", bootstyle=SUCCESS)

        except Exception as e:
            self.status_bar.config(text="Error loading image", bootstyle=DANGER)

    def calibrate_process(self):
        if self.selected_camera_index is None:
            self.status_bar.config(text="Error: Please select a camera first!", bootstyle=DANGER)
            return
        if self.selected_camera_index == 0:
            self.status_bar.config(text="Error: Please select a image first!", bootstyle=SUCCESS)
            return

        print(f"Calibrating with Camera {self.selected_camera_index}")
        mapper = Automapper(self.selected_camera_index)
        self.coordinates, self.cam_frame = mapper.map()

    def change_lights(self):
        tree = Tree()
        coords = tree.get_coords()
        frame = "foo"
        Display(frame, coords, self.file)


if __name__ == "__main__":
    app = App()
    app.mainloop()