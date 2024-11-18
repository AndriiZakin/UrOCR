import pandas as pd
import tkinter as tk
from tkinter import messagebox, scrolledtext
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

def validate_data(data):
    """
    Validates the data to ensure it is suitable for statistical analysis.
    """
    if data.empty:
        raise ValueError("Data is empty")
    
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data is not a DataFrame")
    
    if data.isnull().values.any():
        raise ValueError("Data contains null values")
    
    return True

def calculate_statistics(data):
    """
    Calculates and returns a statistical summary of the data.
    """
    summary = {
        'mean': data.mean(),
        'median': data.median(),
        'std_dev': data.std(),
        'variance': data.var(),
        'min': data.min(),
        'max': data.max(),
        '25%': data.quantile(0.25),
        '50%': data.quantile(0.50),
        '75%': data.quantile(0.75)
    }
    return summary

def show_statistics_results(statistics_summary):
    """
    Displays the statistical summary in a tkinter pop-up window.
    """
    root = tk.Tk()
    root.title("Statistical Summary")

    def show_help():
        help_text = (
            "This window displays the statistical summary of the data, including:\n"
            "- Mean: The average value\n"
            "- Median: The middle value\n"
            "- Standard Deviation: The measure of the amount of variation\n"
            "- Variance: The measure of the dispersion\n"
            "- Min: The minimum value\n"
            "- Max: The maximum value\n"
            "- 25%: The 25th percentile\n"
            "- 50%: The 50th percentile (median)\n"
            "- 75%: The 75th percentile"
        )
        messagebox.showinfo("Help", help_text)

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=30)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    for key, value in statistics_summary.items():
        text_area.insert(tk.END, f"{key}:\n{value}\n\n")
    text_area.configure(state='disabled')

    # Add a help button in the top-right corner
    help_button = tk.Button(root, text="Help", command=show_help)
    help_button.place(relx=1.0, rely=0.0, anchor='ne', padx=10, pady=10)

    root.mainloop()

def show_error_message(message):
    """
    Displays an error message in a tkinter pop-up window.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showerror("Error", message)
    root.destroy()

def statistics_summary(file_path):
    """
    Main function to read, validate, and calculate the statistical summary of the data.
    """
    try:
        data = read_data(file_path)
        if validate_data(data):
            summary = calculate_statistics(data)
            show_statistics_results(summary)
            return summary
    except ValueError as e:
        show_error_message(str(e))
    except Exception as e:
        show_error_message(f"An unexpected error occurred: {e}")

# Example usage:
# file_path = 'path_to_your_file.csv'
# summary = statistics_summary(file_path)
# print(summary)