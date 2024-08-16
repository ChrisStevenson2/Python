import tkinter as tk

from tkinter import filedialog, messagebox

from PIL import Image, ImageTk, ImageDraw, ImageFont

import os



class WatermarkApp:

    def __init__(self, root):

        self.root = root

        self.root.title("Image Watermark Application")

        self.image = None

       

        # Create UI components

        self.create_widgets()



    def create_widgets(self):

        # Upload Button

        self.upload_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)

        self.upload_button.pack(pady=10)



        # Watermark Text Entry

        self.watermark_label = tk.Label(self.root, text="Enter Watermark Text:")

        self.watermark_label.pack(pady=5)

       

        self.watermark_entry = tk.Entry(self.root)

        self.watermark_entry.pack(pady=5)

       

        # Add Watermark Button

        self.add_watermark_button = tk.Button(self.root, text="Add Watermark", command=self.add_watermark)

        self.add_watermark_button.pack(pady=10)



        # Display Image

        self.image_label = tk.Label(self.root)

        self.image_label.pack(pady=10)



    def upload_image(self):

        """Handle image upload and display."""

        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

        if file_path:

            self.image = Image.open(file_path)

            self.display_image(self.image)



    def display_image(self, image):

        """Display the uploaded image in the Tkinter window."""

        image.thumbnail((400, 400))  # Resize for display

        self.tk_image = ImageTk.PhotoImage(image)

        self.image_label.config(image=self.tk_image)



    def add_watermark(self):

        """Add a watermark to the uploaded image."""

        if self.image is None:

            messagebox.showerror("Error", "No image uploaded.")

            return



        watermark_text = self.watermark_entry.get()

        if not watermark_text:

            messagebox.showerror("Error", "Watermark text cannot be empty.")

            return



        # Add watermark

        watermark_image = self.image.copy()

        draw = ImageDraw.Draw(watermark_image)

        try:

            font = ImageFont.load_default()  # Load a default font

            text_width, text_height = draw.textsize(watermark_text, font)

            width, height = watermark_image.size

            x = width - text_width - 10

            y = height - text_height - 10

            draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))  # White text with some transparency

        except Exception as e:

            messagebox.showerror("Error", f"An error occurred: {e}")

            return



        # Save and display the watermarked image

        output_path = "watermarked_image.png"

        watermark_image.save(output_path)

        self.display_image(watermark_image)

        messagebox.showinfo("Success", f"Watermark added. Image saved as {output_path}")



if __name__ == "__main__":

    root = tk.Tk()

    app = WatermarkApp(root)

    root.mainloop()

