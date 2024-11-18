import pandas as pd
import tkinter as tk
from tkinter import messagebox, filedialog
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
    Validates the data to ensure it is suitable for plotting.
    """
    if data.empty:
        raise ValueError("Data is empty")
    
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data is not a DataFrame")
    
    if data.isnull().values.any():
        raise ValueError("Data contains null values")
    
    return True

def draw_histogram(data, column):
    """
    Draws a histogram for the specified column.
    """
    fig, ax = plt.subplots()
    ax.hist(data[column])
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    return fig

def draw_scatter_plot(data, column1, column2):
    """
    Draws a scatter plot for the specified columns.
    """
    fig, ax = plt.subplots()
    ax.scatter(data[column1], data[column2])
    ax.set_title(f'Scatter Plot of {column1} vs {column2}')
    ax.set_xlabel(column1)
    ax.set_ylabel(column2)
    return fig

def draw_line_plot(data, column):
    """
    Draws a line plot for the specified column.
    """
    fig, ax = plt.subplots()
    ax.plot(data[column])
    ax.set_title(f'Line Plot of {column}')
    ax.set_xlabel('Index')
    ax.set_ylabel(column)
    return fig

def draw_bar_plot(data, column):
    """
    Draws a bar plot for the specified column.
    """
    fig, ax = plt.subplots()
    data[column].value_counts().plot(kind='bar', ax=ax)
    ax.set_title(f'Bar Plot of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    return fig

def show_graph(fig):
    """
    Displays the graph in a tkinter pop-up window.
    """
    root = tk.Tk()
    root.title("Graph")

    canvas = FigureCanvasTkAgg(fig, master=root)
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

def histogram_drawing(file_path):
    """
    Opens a tkinter window to select the type of graph.
    """
    def on_button_click(graph_type):
        root.destroy()
        histogram_main(file_path, graph_type)

    root = tk.Tk()
    root.title("Select Graph Type")

    label = tk.Label(root, text="Select the type of diagram:")
    label.pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    buttons = [
        ("Histogram", "histogram"),
        ("Scatter Plot", "scatter"),
        ("Line Plot", "line"),
        ("Bar Plot", "bar")
    ]

    for text, graph_type in buttons:
        button = tk.Button(button_frame, text=text, command=lambda gt=graph_type: on_button_click(gt))
        button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

def histogram_main(file_path, graph_type):
    """
    Main function to read, validate, and draw the specified graph.
    """
    try:
        data = read_data(file_path)
        if validate_data(data):
            if graph_type == 'histogram':
                column = select_column(data, numeric_only=True)
                if column:
                    fig = draw_histogram(data, column)
                else:
                    raise ValueError("No suitable numeric column found for histogram")
            elif graph_type == 'scatter':
                if len(data.columns) < 2:
                    raise ValueError("Scatter plot requires at least two columns")
                column1 = select_column(data, numeric_only=True)
                column2 = select_column(data, numeric_only=True, exclude=[column1])
                if column1 and column2:
                    fig = draw_scatter_plot(data, column1, column2)
                else:
                    raise ValueError("No suitable numeric columns found for scatter plot")
            elif graph_type == 'line':
                column = select_column(data, numeric_only=True)
                if column:
                    fig = draw_line_plot(data, column)
                else:
                    raise ValueError("No suitable numeric column found for line plot")
            elif graph_type == 'bar':
                column = select_column(data, text_only=True)
                if column:
                    fig = draw_bar_plot(data, column)
                else:
                    raise ValueError("No suitable text column found for bar plot")
            else:
                raise ValueError("Unsupported graph type")
            show_graph(fig)
    except ValueError as e:
        show_error_message(str(e))
    except Exception as e:
        show_error_message(f"An unexpected error occurred: {e}")

def select_column(data, numeric_only=False, text_only=False, exclude=[]):
    """
    Selects a column from the DataFrame based on the specified criteria.
    """
    for column in data.columns:
        if column in exclude:
            continue
        if numeric_only and pd.api.types.is_numeric_dtype(data[column]):
            return column
        if text_only and pd.api.types.is_string_dtype(data[column]):
            return column
    return None
