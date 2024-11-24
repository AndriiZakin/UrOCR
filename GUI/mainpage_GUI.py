import tkinter as tk
from tkinter import filedialog, Toplevel, Label, StringVar, OptionMenu, messagebox, Frame
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
import os
from menu_functions import statistics_summary, histogram_drawing, goodness_of_fit, calculate_correlation, change_file_format_gui, show_settings, show_manual

def create_ocr_gui(process_image_callback):
    root = tk.Tk()
    root.title("Main Page")

    save_path = ""
    format_file = "CSV"

    def select_file():
        filepath = filedialog.askopenfilename()
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(0, filepath)

    def select_save_location():
        save_directory = filedialog.askdirectory()
        return save_directory

    def on_process_image():
        filepath = file_path_entry.get()
        if not filepath:
            output_text.insert(tk.END, "Please select an image file.\n")
            return

        if not save_path:
            output_text.insert(tk.END, "Please select a location to save the processed file.\n To do it click on the 'Settings' button.\n")
            return

        save_file_path = os.path.join(save_path, f"processed_file.{format_file.lower()}")  # Use selected format

        output_text.insert(tk.END, "Please wait while your file is processing, this may take some time.\n")
        root.update()

        process_image_callback(filepath, save_file_path, format_file)
        output_text.insert(tk.END, f"File processed successfully, you can find it here: {save_file_path}\n")

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

    def show_settings_menu(root):
        settings_window = Toplevel(root)
        settings_window.title("Settings")

        def save_settings():
            nonlocal save_path, format_file
            save_path = save_path_entry.get()
            format_file = format_var.get()
            settings_window.destroy()

        def cancel_settings():
            if messagebox.askokcancel("Cancel", "Are you sure you want to cancel? Your changes will not be saved."):
                settings_window.destroy()

        def on_closing():
            cancel_settings()

        settings_window.protocol("WM_DELETE_WINDOW", on_closing)

        Label(settings_window, text="Save Path:").grid(row=0, column=0, padx=10, pady=10)
        save_path_entry = tk.Entry(settings_window, width=50)
        save_path_entry.grid(row=0, column=1, padx=10, pady=10)
        save_path_entry.insert(0, save_path)

        select_save_path_button = ttk.Button(settings_window, text="Browse", command=lambda: save_path_entry.insert(0, select_save_location()))
        select_save_path_button.grid(row=0, column=2, padx=10, pady=10)

        Label(settings_window, text="File Format:").grid(row=1, column=0, padx=10, pady=10)
        format_var = StringVar(settings_window, value=format_file)
        format_menu = ttk.Combobox(settings_window, textvariable=format_var, values=["CSV", "XLSX"])
        format_menu.grid(row=1, column=1, padx=10, pady=10)

        button_frame = Frame(settings_window)
        button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        save_button = ttk.Button(button_frame, text="Save", command=save_settings)
        save_button.grid(row=0, column=0, padx=10)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=cancel_settings)
        cancel_button.grid(row=0, column=1, padx=10)

    # Configure grid layout
    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(3):
        root.grid_columnconfigure(i, weight=1)

    # Create frames for better organization
    top_frame = Frame(root, padx=10, pady=10)
    top_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

    middle_frame = Frame(root, padx=10, pady=10)
    middle_frame.grid(row=1, column=0, columnspan=3, sticky="ew")

    bottom_frame = Frame(root, padx=10, pady=10)
    bottom_frame.grid(row=2, column=0, columnspan=3, sticky="nsew")

    # Define button style
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=6, relief="flat", background="#4CAF50", foreground="white")
    style.map("TButton", background=[("active", "#45a049")])

    # Top frame widgets
    help_button = ttk.Button(top_frame, text="Help", command=show_help, width=10)
    help_button.pack(side="left", padx=5)

    dropdown_button = ttk.Button(top_frame, text="Menu", command=lambda: menu.post(dropdown_button.winfo_rootx(), dropdown_button.winfo_rooty() + dropdown_button.winfo_height()), width=10)
    dropdown_button.pack(side="right", padx=5)

    # Middle frame widgets
    settings_button = ttk.Button(middle_frame, text="Settings", command=lambda: show_settings_menu(root), width=10)
    settings_button.pack(side="left", padx=5)

    file_path_entry = tk.Entry(middle_frame, width=50)
    file_path_entry.pack(side="left", fill="x", expand=True, padx=5)

    select_file_button = ttk.Button(middle_frame, text="Select File", command=select_file)
    select_file_button.pack(side="left", padx=5)

    process_button = ttk.Button(middle_frame, text="Process File", command=on_process_image, width=15)
    process_button.pack(side="left", padx=5)

    # Bottom frame widgets
    output_text = ScrolledText(bottom_frame, width=70, height=20)
    output_text.pack(fill="both", expand=True, padx=5, pady=5)

    # Create a menu
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Show Summary Statistics", command=show_statistics_summary)
    menu.add_command(label="Generate Histogram", command=generate_histogram)
    menu.add_command(label="Find Correlations", command=find_correlations)
    menu.add_command(label="Change the file format", command=change_file_format)
    menu.add_command(label="Settings", command=show_settings)
    menu.add_command(label="Instructions/Manual", command=show_manual)
    menu.add_command(label="Save and Exit", command=root.destroy)

    return root