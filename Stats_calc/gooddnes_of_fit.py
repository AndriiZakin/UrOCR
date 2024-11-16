import pandas as pd
from scipy.stats import chisquare, kstest, normaltest

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
    Validates the data to ensure it is suitable for goodness of fit tests.
    """
    if data.empty:
        raise ValueError("Data is empty")
    
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Data is not a DataFrame")
    
    if data.isnull().values.any():
        raise ValueError("Data contains null values")
    
    return True

def chi_square_test(data, expected_freqs):
    """
    Performs the Chi-Square goodness of fit test.
    """
    observed_freqs = data.value_counts()
    chi2, p = chisquare(f_obs=observed_freqs, f_exp=expected_freqs)
    return chi2, p

def kolmogorov_smirnov_test(data, cdf):
    """
    Performs the Kolmogorov-Smirnov goodness of fit test.
    """
    ks_stat, p = kstest(data, cdf)
    return ks_stat, p

def normality_test(data):
    """
    Performs the normality test.
    """
    stat, p = normaltest(data)
    return stat, p

def goodness_of_fit(file_path, test_type, column, **kwargs):
    """
    Main function to read, validate, and perform the specified goodness of fit test.
    """
    data = read_data(file_path)
    if validate_data(data):
        data_column = data[column]
        if test_type == 'chi_square':
            expected_freqs = kwargs.get('expected_freqs')
            if expected_freqs is None:
                raise ValueError("Expected frequencies must be provided for Chi-Square test")
            result = chi_square_test(data_column, expected_freqs)
        elif test_type == 'kolmogorov_smirnov':
            cdf = kwargs.get('cdf')
            if cdf is None:
                raise ValueError("CDF must be provided for Kolmogorov-Smirnov test")
            result = kolmogorov_smirnov_test(data_column, cdf)
        elif test_type == 'normality':
            result = normality_test(data_column)
        else:
            raise ValueError("Unsupported test type")
        return result

# Example usage:
# file_path = 'path_to_your_file.csv'
# result = main(file_path, 'chi_square', 'column_name', expected_freqs=[10, 20, 30])
# print(result)
# result = main(file_path, 'kolmogorov_smirnov', 'column_name', cdf='norm')
# print(result)
# result = main(file_path, 'normality', 'column_name')
# print(result)