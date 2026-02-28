import tkinter as tk
from ensurepip import bootstrap

import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, SUCCESS

#Basic Setup for Window
root = ttk.Window(themename="journal")
root.geometry("800x500")

#Styles
style = ttk.Style()


#Webcam Button setup
webcam_button = ttk.Button(root, text="Webcam", bootstyle=PRIMARY)
style.configure(".TButton", font=("Helvetica", 20))

webcam_button.place(relx=0.3, rely=0.6, relwidth="0.2", relheight="0.1", anchor="center")

#Select Files Button setup

#Start Button Setup
start_button = ttk.Button(root, text="Start", bootstyle=SUCCESS)
start_button.place(relx="0.5", rely="0.75", relwidth="0.2", relheight="0.1", anchor="center")





#run
root.mainloop()