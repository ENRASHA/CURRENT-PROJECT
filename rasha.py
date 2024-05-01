import os
import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code(data, directory, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save QR code as image file (in jpg format)
    qr_path = os.path.join(directory, f"{filename}.jpg")
    qr_img.save(qr_path)

    return qr_path

def choose_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    directory = filedialog.askdirectory(title="Select Directory to Save QR Code")
    return directory

if __name__ == "__main__":
    # Prompt the user to enter the data to be encoded in the QR code
    qr_data = input("Enter the data to encode in the QR code: ")

    # Prompt the user to choose the directory to save the QR code image using GUI
    save_directory = choose_directory()

    # Ensure the directory exists or create it if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Prompt the user to enter the filename for the QR code image
    qr_filename = input("Enter the filename for the QR code image (without extension): ")

    # Generate QR code and get the path of the saved image
    qr_image_path = generate_qr_code(qr_data, save_directory, qr_filename)

    print(f"QR code generated and saved as {qr_image_path}")

