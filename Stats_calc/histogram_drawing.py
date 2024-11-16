import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    """
    Reads data from a file and returns it as a DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
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
    plt.hist(data[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def draw_scatter_plot(data, column1, column2):
    """
    Draws a scatter plot for the specified columns.
    """
    plt.scatter(data[column1], data[column2])
    plt.title(f'Scatter Plot of {column1} vs {column2}')
    plt.xlabel(column1)
    plt.ylabel(column2)
    plt.show()

def draw_line_plot(data, column):
    """
    Draws a line plot for the specified column.
    """
    plt.plot(data[column])
    plt.title(f'Line Plot of {column}')
    plt.xlabel('Index')
    plt.ylabel(column)
    plt.show()

def draw_bar_plot(data, column):
    """
    Draws a bar plot for the specified column.
    """
    data[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Plot of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def histogram_drawing(file_path, graph_type, column1, column2=None):
    """
    Main function to read, validate, and draw the specified graph.
    """
    data = read_data(file_path)
    if validate_data(data):
        if graph_type == 'histogram':
            draw_histogram(data, column1)
        elif graph_type == 'scatter':
            if column2 is None:
                raise ValueError("Scatter plot requires two columns")
            draw_scatter_plot(data, column1, column2)
        elif graph_type == 'line':
            draw_line_plot(data, column1)
        elif graph_type == 'bar':
            draw_bar_plot(data, column1)
        else:
            raise ValueError("Unsupported graph type")

# Example usage:
# file_path = 'path_to_your_file.csv'
# main(file_path, 'histogram', 'column_name')
# main(file_path, 'scatter', 'column1', 'column2')
# main(file_path, 'line', 'column_name')
# main(file_path, 'bar', 'column_name')