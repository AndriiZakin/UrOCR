import pandas as pd
import tkinter as tk
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
    Validates the data to ensure it is suitable for correlation calculation.
    """
    if data.empty:
        raise ValueError("Data is empty")
    
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data is not a DataFrame")
    
    if data.shape[1] < 2:
        raise ValueError("Data must have at least two columns for correlation calculation")
    
    if data.isnull().values.any():
        raise ValueError("Data contains null values")
    
    return True

def calculate_correlation_matrix(data):
    """
    Calculates the correlation matrix of the data.
    """
    correlation_matrix = data.corr()
    return correlation_matrix

def show_correlation_results(data, correlation_matrix):
    """
    Displays the correlation matrix and graph in a tkinter pop-up window.
    """
    root = tk.Tk()
    root.title("Correlation Results")

    # Create a frame for the correlation matrix
    matrix_frame = tk.Frame(root)
    matrix_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    text_area = scrolledtext.ScrolledText(matrix_frame, wrap=tk.WORD, width=50, height=30)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    text_area.insert(tk.END, correlation_matrix.to_string())
    text_area.configure(state='disabled')

    # Create a frame for the correlation graph
    graph_frame = tk.Frame(root)
    graph_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    fig, ax = plt.subplots()
    cax = ax.matshow(correlation_matrix, cmap='coolwarm')
    fig.colorbar(cax)

    ticks = range(len(data.columns))
    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_xticklabels(data.columns, rotation=90)
    ax.set_yticklabels(data.columns)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    root.mainloop()

def show_error_message(message):
    """
    Displays an error message in a tkinter pop-up window.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showerror("Error", message)
    root.destroy()

def calculate_correlation(file_path):
    """
    Main function to read, validate, and calculate correlation of the data.
    """
    try:
        data = read_data(file_path)
        if validate_data(data):
            correlation_matrix = calculate_correlation_matrix(data)
            show_correlation_results(data, correlation_matrix)
            return correlation_matrix
    except ValueError as e:
        show_error_message(str(e))
    except Exception as e:
        show_error_message(f"An unexpected error occurred: {e}")

# Example usage:
# file_path = 'C:\\Users\\AndrZ\\Desktop\\Comp.SienceProject\\UrOCR\\results\\output.xlsx'
# correlation_matrix = calculate_correlation(file_path)