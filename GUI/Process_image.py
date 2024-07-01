import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

def create_ocr_gui(process_image_callback):
    def select_file():
        filepath = filedialog.askopenfilename()
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, filepath)

    def on_process_image():
        filepath = file_path_entry.get()
        if not filepath:
            output_text.insert(tk.END, "Please select an image file.\n")
            return
        
        process_image_callback(filepath)

    root = tk.Tk()
    root.title("Image OCR")

    file_path_entry = tk.Entry(root, width=50)
    file_path_entry.pack(padx=10, pady=5)

    select_file_button = tk.Button(root, text="Select Image", command=select_file)
    select_file_button.pack(pady=5)

    process_button = tk.Button(root, text="Process Image", command=on_process_image)
    process_button.pack(pady=5)

    output_text = ScrolledText(root, width=70, height=20)
    output_text.pack(padx=10, pady=5)

    return root