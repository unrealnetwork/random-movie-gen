#gnu license, everyone can use it as their own, by @unreal_shoushuke
#if you are using arch-linux based system, better use a virtual environment. 
#to create a vrtiual envriontments, follow these commands in your terminal
'''
cd YOUR-PATH
python -m venv NAME_YOUR_VENV
python -m venv NAME_OF_YOUR_VENV
source name_of_your_venv/bin/activate
'''
#to deactivate venv, use command "deactivate".

import cv2 #pip install open-cv python (you can use pacman or apt too)
import tkinter as tk #pip install tkinter (you can use sudo pacman -S tk or apt install tkinter too)
from datetime import datetime #this is pre-installed pythn module, you dont have to install it externally
from PIL import Image, ImageTk #pillow can be installed using pip or any package manager you have

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera App")
        self.root.geometry("600x400")

        self.camera = cv2.VideoCapture(0)
        self.is_recording = False
        self.start_time = None

        self.canvas = tk.Canvas(self.root, width=600, height=350)
        self.canvas.pack()

        # design a photo click button (capture button)
        self.btn_capture = tk.Canvas(self.root, width=60, height=60, bd=0, highlightthickness=0)
        self.btn_capture.create_oval(5, 5, 55, 55, outline="white", width=2)
        self.btn_capture.pack()
        self.btn_capture.bind("<Button-1>", self.start_recording)
        self.btn_capture.bind("<ButtonRelease-1>", self.stop_recording)

        self.recording_square = None

        self.update()
        self.root.mainloop()

    def capture_photo(self):
        ret, frame = self.camera.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_name = f"photo_{timestamp}.png"
            file_path = os.path.join("/home/aneek/Pictures/cam", file_name)
            cv2.imwrite(file_path, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    def start_recording(self, event):
        self.is_recording = True
        self.start_time = datetime.now()
        self.recording_square = self.canvas.create_rectangle(10, 10, 30, 30, outline="red", width=2)

    def stop_recording(self, event):
        if self.is_recording:
            self.is_recording = False
            self.canvas.delete(self.recording_square)

    def update(self):
        ret, frame = self.camera.read()
        if ret:
            if self.is_recording:
                duration = datetime.now() - self.start_time
                self.canvas.create_text(300, 370, text=str(duration), fill="white")
            self.photo = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.after(10, self.update)
        
#use these lines instead of the logic above if your camera/webcam is capturing horizontally
    
    ''' 
        def update(self):
        ret, frame = self.camera.read()
        if ret:
            frame = cv2.flip(frame, 1)

            if self.is_recording:
                duration = datetime.now() - self.start_time
                self.canvas.create_text(300, 370, text=str(duration), fill="white")
            self.photo = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.root.after(10, self.update)
        
        '''

    def __del__(self):
        self.camera.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = CameraApp(root)
