import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def read_data(file_path):
    """
    Reads data from a file and returns it as a DataFrame.
    """
    try:
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.csv':
            data = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            data = pd.read_excel(file_path)
        elif file_extension == '.json':
            data = pd.read_json(file_path)
        elif file_extension == '.parquet':
            data = pd.read_parquet(file_path)
        elif file_extension in ['.h5', '.hdf5']:
            data = pd.read_hdf(file_path)
        elif file_extension == '.feather':
            data = pd.read_feather(file_path)
        elif file_extension == '.dta':
            data = pd.read_stata(file_path)
        elif file_extension in ['.sas7bdat', '.xpt']:
            data = pd.read_sas(file_path)
        elif file_extension in ['.sav', '.zsav']:
            data = pd.read_spss(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
        return data
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")

def convert_file_format(file_path, target_format):
    try:
        # Read the file into a DataFrame
        data = read_data(file_path)

        # Determine the new file path
        base, ext = os.path.splitext(file_path)
        new_file_path = f"{base}_modified.{target_format}"

        # Save the DataFrame in the new format
        if target_format == 'csv':
            data.to_csv(new_file_path, index=False)
        elif target_format == 'xlsx':
            data.to_excel(new_file_path, index=False)
        elif target_format == 'json':
            data.to_json(new_file_path, orient='records', lines=True)
        elif target_format == 'parquet':
            data.to_parquet(new_file_path)
        elif target_format == 'hdf5':
            data.to_hdf(new_file_path, key='df', mode='w')
        elif target_format == 'feather':
            data.to_feather(new_file_path)
        elif target_format == 'stata':
            data.to_stata(new_file_path)
        elif target_format == 'sas':
            data.to_sas(new_file_path)
        elif target_format == 'spss':
            data.to_spss(new_file_path)
        else:
            raise ValueError(f"Unsupported target format: {target_format}")

        messagebox.showinfo("Success", f"File converted and saved as {new_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert file: {e}")

def change_file_format_gui(file_path):
    def on_convert_button_click():
        target_format = format_var.get()
        if target_format:
            convert_file_format(file_path, target_format)
            root.destroy()
        else:
            messagebox.showwarning("Warning", "Please select a target format")

    root = tk.Tk()
    root.title("Convert File Format")

    label = tk.Label(root, text="Select the target format:")
    label.pack(pady=10)

    format_var = tk.StringVar(value="")

    formats = ['csv', 'xlsx', 'json', 'parquet', 'hdf5', 'feather', 'stata', 'sas', 'spss']
    for fmt in formats:
        radio_button = tk.Radiobutton(root, text=fmt.upper(), variable=format_var, value=fmt)
        radio_button.pack(anchor=tk.W)

    convert_button = tk.Button(root, text="Convert", command=on_convert_button_click)
    convert_button.pack(pady=10)

    root.mainloop()