import os
from tkinter import Tk, filedialog, Label, Button, Entry, messagebox, StringVar
from PIL import Image, ImageTk

# Function to select an image file
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    if file_path:
        image_path.set(file_path)
        load_preview(file_path)

# Function to preview the image in the GUI
def load_preview(file_path):
    try:
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        preview_image = ImageTk.PhotoImage(img)
        preview_label.config(image=preview_image)
        preview_label.image = preview_image
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image preview: {e}")

# Function to resize the image
def resize_image():
    file_path = image_path.get()
    try:
        width = int(width_var.get())
        height = int(height_var.get())
    except ValueError:
        messagebox.showwarning("Invalid Input", "Width and Height must be integers.")
        return
    
    if not file_path:
        messagebox.showwarning("No Image", "Please select an image file first.")
        return

    if width <= 0 or height <= 0:
        messagebox.showwarning("Invalid Dimensions", "Width and Height must be positive integers.")
        return

    try:
        img = Image.open(file_path)
        img_resized = img.resize((width, height), Image.Resampling.LANCZOS)

        # Ask user for save location
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", ".png"), ("JPEG files", ".jpg"), ("BMP files", "*.bmp")]
        )
        if save_path:
            img_resized.save(save_path)
            messagebox.showinfo("Image Resizer", "Image has been resized and saved successfully!")
        else:
            messagebox.showinfo("Cancelled", "Save operation was cancelled.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to resize and save image: {e}")

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