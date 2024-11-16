'''import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Resizer")
        self.root.geometry("600x500")
        self.root.config(bg="#e0e0e0")

        self.image = None
        self.image_display = None

        # Header Label
        header_label = tk.Label(self.root, text="Image Resizer", font=("Arial", 20, "bold"), bg="#5a5a5a", fg="white")
        header_label.pack(fill="x", pady=10)

        # Frame for image selection and display
        frame = tk.Frame(self.root, bg="#e0e0e0")
        frame.pack(pady=20)

        # Load Image Button
        load_button = tk.Button(frame, text="Load Image", command=self.load_image, font=("Arial", 12), bg="#4CAF50", fg="white")
        load_button.grid(row=0, column=0, padx=10)

        # Resize Width and Height Entry Fields
        self.width_entry = tk.Entry(frame, width=10, font=("Arial", 12))
        self.width_entry.grid(row=0, column=1, padx=10)
        self.width_entry.insert(0, "Width")

        self.height_entry = tk.Entry(frame, width=10, font=("Arial", 12))
        self.height_entry.grid(row=0, column=2, padx=10)
        self.height_entry.insert(0, "Height")

        # Resize Button
        resize_button = tk.Button(frame, text="Resize", command=self.resize_image, font=("Arial", 12), bg="#2196F3", fg="white")
        resize_button.grid(row=0, column=3, padx=10)

        # Save Image Button
        save_button = tk.Button(frame, text="Save Image", command=self.save_image, font=("Arial", 12), bg="#FF9800", fg="white")
        save_button.grid(row=0, column=4, padx=10)

        # Label for displaying the image
        self.image_label = tk.Label(self.root, bg="#e0e0e0")
        self.image_label.pack(pady=20)

    def load_image(self):
        # Open file dialog to select an image file
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def resize_image(self):
        # Resize the image based on user input for width and height
        if self.image:
            try:
                width = int(self.width_entry.get())
                height = int(self.height_entry.get())
                resized_image = self.image.resize((width, height))
                self.display_image(resized_image)
                self.image_display = resized_image
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid integers for width and height.")
        else:
            messagebox.showwarning("No Image", "Please load an image first.")

    def save_image(self):
        # Save the resized image
        if self.image_display:
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("BMP", "*.bmp")])
            if save_path:
                self.image_display.save(save_path)
                messagebox.showinfo("Image Saved", "Your resized image has been saved successfully.")
        else:
            messagebox.showwarning("No Resized Image", "Please resize the image before saving.")

    def display_image(self, img):
        # Display the image in the GUI
        img.thumbnail((300, 300))  # Adjust preview size
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageResizerApp(root)
    root.mainloop()'''
    
import os
from tkinter import Tk, filedialog, Label, Button, Entry, messagebox, StringVar
from PIL import Image, ImageTk, ImageFont, ImageDraw

# Function to select an image file
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        image_path.set(file_path)
        load_preview(file_path)

# Function to preview the image in the GUI
def load_preview(file_path):
    img = Image.open(file_path)
    img.thumbnail((200, 200))
    preview_image = ImageTk.PhotoImage(img)
    preview_label.config(image=preview_image)
    preview_label.image = preview_image

# Function to resize the image
def resize_image():
    file_path = image_path.get()
    width = int(width_var.get())
    height = int(height_var.get())
    
    if file_path and width > 0 and height > 0:
        img = Image.open(file_path)
        img_resized = img.resize((width, height), Image.ANTIALIAS)
        
        # Ask user for save location
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if save_path:
            img_resized.save(save_path)
            messagebox.showinfo("Image Resizer", "Image has been resized and saved successfully!")
    else:
        messagebox.showwarning("Invalid Input", "Please make sure all fields are filled correctly.")

# Set up the main window
root = Tk()
root.title("Image Resizer")
root.geometry("400x500")
root.config(bg="#f3e8e8")

# Font settings
label_font = ("Helvetica", 12, "bold")
entry_font = ("Helvetica", 11)

# Image path variable
image_path = StringVar()

# Header
header_label = Label(root, text="Image Resizer", font=("Helvetica", 18, "bold"), bg="#f3e8e8", fg="#6a6a6a")
header_label.pack(pady=10)

# Image selection
select_button = Button(root, text="Select Image", command=select_image, bg="#add8e6", fg="#6a6a6a", font=label_font)
select_button.pack(pady=10)

# Image preview
preview_label = Label(root, bg="#f3e8e8")
preview_label.pack(pady=10)

# Width entry
width_label = Label(root, text="Width:", font=label_font, bg="#f3e8e8", fg="#6a6a6a")
width_label.pack(pady=5)
width_var = StringVar()
width_entry = Entry(root, textvariable=width_var, font=entry_font, bg="#ffffff", fg="#6a6a6a", width=10)
width_entry.pack(pady=5)

# Height entry
height_label = Label(root, text="Height:", font=label_font, bg="#f3e8e8", fg="#6a6a6a")
height_label.pack(pady=5)
height_var = StringVar()
height_entry = Entry(root, textvariable=height_var, font=entry_font, bg="#ffffff", fg="#6a6a6a", width=10)
height_entry.pack(pady=5)

# Resize button
resize_button = Button(root, text="Resize & Save Image", command=resize_image, bg="#add8e6", fg="#6a6a6a", font=label_font)
resize_button.pack(pady=20)

# Main loop
root.mainloop()