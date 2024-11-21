import unittest
import pandas as pd
from correlation_calc import read_data, validate_data, calculate_correlation_matrix, show_error_message, calculate_correlation

class TestCorrelationCalc(unittest.TestCase):

    def test_read_data_csv(self):
        data = read_data('Test_data/test_data.csv')
        self.assertIsInstance(data, pd.DataFrame)

    def test_read_data_excel(self):
        data = read_data('Test_data/test_data.xlsx')
        self.assertIsInstance(data, pd.DataFrame)

    def test_read_data_unsupported(self):
        with self.assertRaises(ValueError):
            read_data('Test_data/test_data.txt')

    def test_validate_data(self):
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        self.assertTrue(validate_data(data))

    def test_validate_data_empty(self):
        data = pd.DataFrame()
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_validate_data_not_dataframe(self):
        data = [1, 2, 3]
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_validate_data_single_column(self):
        data = pd.DataFrame({
            'A': [1, 2, 3]
        })
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_validate_data_null_values(self):
        data = pd.DataFrame({
            'A': [1, 2, None],
            'B': [4, 5, 6]
        })
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_calculate_correlation_matrix(self):
        data = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6]
        })
        correlation_matrix = calculate_correlation_matrix(data)
        self.assertIsInstance(correlation_matrix, pd.DataFrame)
        self.assertEqual(correlation_matrix.shape, (2, 2))

    def test_calculate_correlation(self):
        file_path = 'Test_data/test_data.csv'
        correlation_matrix = calculate_correlation(file_path)
        self.assertIsInstance(correlation_matrix, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()