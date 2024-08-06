import tkinter as tk
from tkinter import filedialog, Toplevel, Label
from tkinter.scrolledtext import ScrolledText

directory = r'C:\Users\AndrZ\Desktop\Comp.SienceProject\UrOCR\OCR\results'

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
        
        output_text.insert(tk.END, "Please wait while your file is processed, this may take some time.")
        process_image_callback(filepath)
        output_text.insert(tk.END, "File processed successfully, you can find it in this directory" + directory)

    def show_help():
        help_window = Toplevel(root)
        help_window.title("Help")
        help_text = (
            "OCR (Optical Character Recognition) is a technology that converts different types of documents, "
            "such as scanned paper documents, PDF files, or images captured by a digital camera, into editable "
            "and searchable data.\n\n"
            "You can use this application to process image files and extract text from them. "
            "The types of files accepted include common image formats such as JPEG, PNG, BMP, and TIFF."
        )
        help_label = Label(help_window, text=help_text, wraplength=400, justify="left")
        help_label.pack(padx=10, pady=10)

    root = tk.Tk()
    root.title("Image OCR")

    help_button = tk.Button(root, text="Help", command=show_help)
    help_button.place(x=10, y=10)

    file_path_entry = tk.Entry(root, width=50)
    file_path_entry.pack(padx=10, pady=5)

    select_file_button = tk.Button(root, text="Select File", command=select_file)
    select_file_button.pack(pady=5)

    process_button = tk.Button(root, text="Process File", command=on_process_image)
    process_button.pack(pady=5)

    output_text = ScrolledText(root, width=70, height=20)
    output_text.pack(padx=10, pady=5)

    return root