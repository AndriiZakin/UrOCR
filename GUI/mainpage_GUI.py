import tkinter as tk
from tkinter import filedialog, Toplevel, Label, StringVar, OptionMenu, messagebox
from tkinter.scrolledtext import ScrolledText
from menu_functions import statistics_summary, histogram_drawing, goodness_of_fit, calculate_correlation, change_file_format_gui, show_settings, show_manual

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
        
        output_text.insert(tk.END, "Please wait while your file is processing, this may take some time.")
        root.update()

        process_image_callback(filepath)
        output_text.insert(tk.END, "File processed successfully, you can find it in this directory" + directory)

    def show_help():
        help_text = (
            "OCR (Optical Character Recognition) is a technology that converts different types of documents, "
            "such as scanned paper documents, PDF files, or images captured by a digital camera, into editable "
            "and searchable data.\n\n"
            "You can use this application to process image files and extract text from them. "
            "The types of files accepted include common image formats such as JPEG, PNG, BMP, and TIFF."
        )
        messagebox.showinfo("Help", help_text)

    def show_statistics_summary():
        filepath = file_path_entry.get()
        if not filepath:
            output_text.insert(tk.END, "Please select a file to show statistics summary.\n")
            return
        try:
            statistics_summary(filepath)
        except Exception as e:
            output_text.insert(tk.END, str(e))

    def generate_histogram():
        filepath = file_path_entry.get()
        if not filepath:
            output_text.insert(tk.END, "Please select a file to generate a histogram.\n")
            return
        try:
            histogram_drawing(filepath)
        except Exception as e:
            output_text.insert(tk.END, str(e))            

    def find_correlations():
        filepath = file_path_entry.get()
        if not filepath:
            output_text.insert(tk.END, "Please select a file to find correlations.\n")
            return
        try:
            calculate_correlation(filepath)
        except Exception as e:
            output_text.insert(tk.END, str(e))
        
    def change_file_format():
        filepath = file_path_entry.get()
        if not filepath:
            output_text.insert(tk.END, "Please select a file to change file format.\n")
            return
        try:
            change_file_format_gui(filepath)
        except Exception as e:
            output_text.insert(tk.END, str(e))

    root = tk.Tk()
    root.title("Image OCR")

    # Configure grid layout
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)

    help_label = Label(root, wraplength=400, justify="left")
    help_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="w")

    help_button = tk.Button(root, text="Help", command=show_help)
    help_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    file_path_entry = tk.Entry(root, width=50)
    file_path_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    select_file_button = tk.Button(root, text="Select File", command=select_file)
    select_file_button.grid(row=2, column=2, padx=10, pady=5, sticky="ew")

    process_button = tk.Button(root, text="Process File", command=on_process_image, width=15)
    process_button.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

    output_text = ScrolledText(root, width=70, height=20)
    output_text.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

    # Create a menu
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Show Summary Statistics", command=show_statistics_summary)
    menu.add_command(label="Generate Histogram", command=generate_histogram)
    menu.add_command(label="Find Correlations", command=find_correlations)
    menu.add_command(label="Change the file format", command=change_file_format)
    menu.add_command(label="Settings", command=show_settings)
    menu.add_command(label="Instructions/Manual", command=show_manual)
    menu.add_command(label="Save and Exit", command=root.destroy)

    # Create a button to display the menu
    dropdown_button = tk.Button(root, text="≡", font=("Arial", 14), command=lambda: menu.post(dropdown_button.winfo_rootx(), dropdown_button.winfo_rooty() + dropdown_button.winfo_height()))
    dropdown_button.grid(row=0, column=2, padx=10, pady=5, sticky="e")

    return root