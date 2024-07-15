import os
import random
import tkinter as tk
from tkinter import Toplevel
from PIL import Image, ImageTk
import numpy as np
import subprocess
import shutil
import sys
import pytesseract  # Import pytesseract
import pyperclip  # Import pyperclip to handle clipboard operations
import webbrowser  # Import webbrowser module for opening URLs

class ImageGallery:
    def __init__(self, root, image_folder):
        self.root = root
        self.root.title("Photoreviewer")
        self.image_folder = image_folder
        self.cleared_folder = os.path.join(image_folder, "cleared")
        self.reviewed_folder = os.path.join(image_folder, "reviewed")
        self.image_files = self.get_all_images(image_folder)
        self.liked_images = []
        self.image_probabilities = np.ones(len(self.image_files))  # Initialize equal probabilities
        self.history = []
        self.history_index = -1  # Tracks the position in the history
        self.current_image_index = -1

        # Set the initial canvas size to be larger
        self.canvas_width = 1200
        self.canvas_height = 900
        self.canvas = tk.Canvas(root, bg='white', width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.next_button = tk.Button(self.button_frame, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.previous_button = tk.Button(self.button_frame, text="Previous", command=self.show_previous_image)
        self.previous_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.like_button = tk.Button(self.button_frame, text="Like", command=self.like_current_image)
        self.like_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_current_image)
        self.clear_button.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        self.root.bind("<Right>", lambda event: self.show_next_image())
        self.root.bind("<Left>", lambda event: self.show_previous_image())
        self.root.bind("<Up>", lambda event: self.like_current_image())
        self.root.bind("<Down>", lambda event: self.clear_current_image())
        self.root.bind("<Delete>", lambda event: self.delete_current_image())
        self.root.bind("<Return>", lambda event: self.open_in_explorer())
        self.root.bind("o", lambda event: self.recognize_text())  # Bind 'o' key to recognize_text function
        self.root.bind("<Home>", lambda event: self.open_webpage())  # Bind Home key to open webpage
        self.root.bind("<End>", lambda event: self.rename_and_exit())  # Bind End key to rename and exit
        
        # Show first photo on startup
        if self.image_files:
            self.current_image_index = 0
            self.history.append(self.current_image_index)
            self.history_index = 0
            self.root.after(100, lambda: self.show_image(self.image_files[self.current_image_index]))
        else:
            self.show_temp_message("No images found in the folder.")

    def get_all_images(self, folder):
        image_files = []
        for root, _, files in os.walk(folder):
            if os.path.abspath(root) == os.path.abspath(self.cleared_folder):
                continue
            for file in files:
                if file.lower().endswith(('png', 'jpg', 'jpeg', 'gif')):
                    image_files.append(os.path.join(root, file))
        return image_files

    def show_temp_message(self, message):
        temp_window = Toplevel(self.root)
        temp_window.title("Message")
        temp_window.geometry("200x100")
        temp_label = tk.Label(temp_window, text=message)
        temp_label.pack(expand=True)
        self.root.after(1000, temp_window.destroy)  # Destroy the window after 1 second

    def show_image(self, image_path):
        img = Image.open(image_path)
        img_width, img_height = img.size
        canvas_width, canvas_height = self.canvas.winfo_width(), self.canvas.winfo_height()
        max_width = min(canvas_width, img_width * 1.5)
        max_height = min(canvas_height, img_height * 1.5)
        img.thumbnail((max_width, max_height), Image.LANCZOS)
        self.photo_img = ImageTk.PhotoImage(img)
        
        # Center the image on the canvas
        self.canvas.delete("all")
        x = (canvas_width - img.width) // 2
        y = (canvas_height - img.height) // 2
        self.canvas.create_image(x, y, anchor=tk.NW, image=self.photo_img)

    def show_next_image(self):
        if not self.image_files:
            self.show_temp_message("No images left in the folder.")
            return
        
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.current_image_index = self.history[self.history_index]
        else:
            # Ensure the next image is not the same as the current one
            if len(self.image_files) > 1:
                remaining_probs = self.image_probabilities.copy()
                remaining_probs[self.current_image_index] = 0  # Set probability of current image to 0
                self.current_image_index = np.random.choice(len(self.image_files), p=remaining_probs/remaining_probs.sum())
            else:
                self.current_image_index = 0
            self.history.append(self.current_image_index)
            self.history_index = len(self.history) - 1
        
        self.show_image(self.image_files[self.current_image_index])

    def show_previous_image(self):
        if not self.image_files:
            self.show_temp_message("No images left in the folder.")
            return

        if self.history_index > 0:
            self.history_index -= 1
            self.current_image_index = self.history[self.history_index]
            self.show_image(self.image_files[self.current_image_index])

    def like_current_image(self):
        if self.current_image_index == -1:
            return
        current_image = self.image_files[self.current_image_index]
        if current_image not in self.liked_images:
            self.liked_images.append(current_image)
        
        # Increase the probability density of the liked image
        self.image_probabilities[self.current_image_index] *= 1.5
        self.show_temp_message("Liked")

    def delete_current_image(self):
        if self.current_image_index == -1 or not self.image_files:
            return
        
        current_image = self.image_files[self.current_image_index]
        os.remove(current_image)
        self.image_files.pop(self.current_image_index)
        self.image_probabilities = np.delete(self.image_probabilities, self.current_image_index)
        
        # Remove the deleted image from history and adjust indices
        self.history = [i if i < self.current_image_index else i - 1 for i in self.history if i != self.current_image_index]
        
        self.show_temp_message("Deleted")
        
        if self.image_files:
            # Ensure current_image_index is within bounds
            self.history_index = min(self.history_index, len(self.history) - 1)
            self.current_image_index = self.history[self.history_index]
            self.show_image(self.image_files[self.current_image_index])
        else:
            self.current_image_index = -1
            self.canvas.delete("all")

    def clear_current_image(self):
        if self.current_image_index == -1 or not self.image_files:
            return
        
        current_image = self.image_files[self.current_image_index]
        
        # Create the "cleared" folder if it doesn't exist
        if not os.path.exists(self.cleared_folder):
            os.makedirs(self.cleared_folder)
        
        # Move the current image to the "cleared" folder
        destination = os.path.join(self.cleared_folder, os.path.basename(current_image))
        shutil.move(current_image, destination)
        
        # Remove the image from the list and update probabilities
        self.image_files.pop(self.current_image_index)
        self.image_probabilities = np.delete(self.image_probabilities, self.current_image_index)
        
        # Remove the cleared image from history and adjust indices
        self.history = [i if i < self.current_image_index else i - 1 for i in self.history if i != self.current_image_index]
        
        self.show_temp_message("Cleared")
        
        if self.image_files:
            # Ensure current_image_index is within bounds
            self.history_index = min(self.history_index, len(self.history) - 1)
            self.current_image_index = self.history[self.history_index]
            self.show_image(self.image_files[self.current_image_index])
        else:
            self.current_image_index = -1
            self.canvas.delete("all")

    def open_in_explorer(self):
        if self.current_image_index == -1:
            return
        
        current_image = self.image_files[self.current_image_index]
        folder_path = os.path.dirname(current_image)
        file_name = os.path.basename(current_image)
        
        if os.name == 'nt':  # For Windows
            subprocess.run(['explorer', '/select,', current_image])
        elif os.name == 'posix':  # For macOS and Linux
            if sys.platform == 'darwin':  # macOS
                subprocess.run(['open', '-R', current_image])
            else:  # Linux
                subprocess.run(['xdg-open', folder_path])
        
        self.show_temp_message(f"Opened folder: {folder_path}")

    def recognize_text(self):
        if self.current_image_index == -1:
            return
        
        current_image = self.image_files[self.current_image_index]
        img = Image.open(current_image)

        # Perform OCR using pytesseract
        recognized_text = pytesseract.image_to_string(img, lang='eng+jpn+vie')

        # Show the recognized text in a temporary message box
        self.show_temp_message(recognized_text)
        
        # Copy the recognized text to clipboard
        pyperclip.copy(recognized_text)
         
    def open_webpage(self):
        # Open a webpage when Home key is pressed
        url = "https://smk-toyama.notion.site/Photoreviewer-67f701d33a0d4eb18fccb6a5871c56db"  # Replace with your desired URL
        webbrowser.open(url)

    def rename_and_exit(self):
        if os.path.exists(self.cleared_folder):
            os.rename(self.cleared_folder, self.reviewed_folder)
            self.show_temp_message("Renamed 'cleared' folder to 'reviewed'")
        self.root.quit()  # Exit the application
        
if __name__ == "__main__":
    root = tk.Tk()
    
    # Check if a file path is provided via command line argument
    if len(sys.argv) > 1:
        image_folder = os.path.dirname(sys.argv[1])  # Use the parent folder of the provided file path
    else:
        # Get the default "Pictures" folder for the current user
        image_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    
    app = ImageGallery(root, image_folder)
    root.mainloop()