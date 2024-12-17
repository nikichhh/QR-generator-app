import qrcode
import os
import platform

def generate_qr_code(data, save_path):
    qr = qrcode.make(data)
    qr.save(save_path)

def print_image(file_path):
    if platform.system() == "Windows":
        os.startfile(file_path, "print")
    else:
        raise NotImplementedError("Printing is only supported on Windows.")
