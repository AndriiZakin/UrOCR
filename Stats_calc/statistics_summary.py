import pandas as pd

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

def statistics_summary(file_path):
    """
    Main function to read, validate, and calculate the statistical summary of the data.
    """
    data = read_data(file_path)
    if validate_data(data):
        statistics_summary = calculate_statistics(data)
        return statistics_summary

# Example usage:
# file_path = 'path_to_your_file.csv'
# summary = main(file_path)
# print(summary)