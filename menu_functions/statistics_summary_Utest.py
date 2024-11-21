import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from statistics_summary import read_data, validate_data, calculate_statistics, show_statistics_results, show_error_message, statistics_summary
import tkinter as tk

class TestStatisticsSummary(unittest.TestCase):

    @patch('statistics_summary.pd.read_csv')
    def test_read_data_csv(self, mock_read_csv):
        mock_read_csv.return_value = pd.DataFrame({'A': [1, 2, 3]})
        data = read_data('Test_data/test.csv')
        mock_read_csv.assert_called_once_with('Test_data/test.csv')
        self.assertIsInstance(data, pd.DataFrame)

    @patch('statistics_summary.pd.read_excel')
    def test_read_data_excel(self, mock_read_excel):
        mock_read_excel.return_value = pd.DataFrame({'A': [1, 2, 3]})
        data = read_data('Test_data/test.xlsx')
        mock_read_excel.assert_called_once_with('Test_data/test.xlsx')
        self.assertIsInstance(data, pd.DataFrame)

    def test_validate_data(self):
        data = pd.DataFrame({'A': [1, 2, 3]})
        self.assertTrue(validate_data(data))

    def test_validate_data_empty(self):
        data = pd.DataFrame()
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_validate_data_not_dataframe(self):
        data = [1, 2, 3]
        with self.assertRaises(ValueError) as context:
            validate_data(data)
        self.assertEqual(str(context.exception), "Data is not a DataFrame")

    def test_validate_data_with_nulls(self):
        data = pd.DataFrame({'A': [1, None, 3]})
        with self.assertRaises(ValueError):
            validate_data(data)

    def test_calculate_statistics(self):
        data = pd.DataFrame({'A': [1, 2, 3, 4, 5]})
        summary = calculate_statistics(data)
        self.assertIn('mean', summary)
        self.assertIn('median', summary)
        self.assertIn('std_dev', summary)
        self.assertIn('variance', summary)
        self.assertIn('min', summary)
        self.assertIn('max', summary)
        self.assertIn('25%', summary)
        self.assertIn('50%', summary)
        self.assertIn('75%', summary)

    @patch('statistics_summary.tk.Tk')
    @patch('statistics_summary.scrolledtext.ScrolledText')
    @patch('statistics_summary.tk.Button')
    def test_show_statistics_results(self, mock_button, mock_scrolledtext, mock_tk):
        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        mock_text_area = MagicMock()
        mock_scrolledtext.return_value = mock_text_area

        statistics_summary = {
            'mean': pd.Series([1.0], index=['A']),
            'median': pd.Series([1.0], index=['A']),
            'std_dev': pd.Series([1.0], index=['A']),
            'variance': pd.Series([1.0], index=['A']),
            'min': pd.Series([1.0], index=['A']),
            'max': pd.Series([1.0], index=['A']),
            '25%': pd.Series([1.0], index=['A']),
            '50%': pd.Series([1.0], index=['A']),
            '75%': pd.Series([1.0], index=['A'])
        }

        show_statistics_results(statistics_summary)
        mock_tk.assert_called_once()
        mock_scrolledtext.assert_called_once_with(mock_root, wrap=tk.WORD, width=100, height=30)
        mock_text_area.pack.assert_called_once_with(padx=10, pady=10, fill=tk.BOTH, expand=True)
        mock_button.assert_called_once_with(mock_root, text="Help", command=unittest.mock.ANY)
        mock_root.mainloop.assert_called_once()

    @patch('statistics_summary.tk.Tk')
    @patch('statistics_summary.messagebox.showerror')
    def test_show_error_message(self, mock_showerror, mock_tk):
        mock_root = MagicMock()
        mock_tk.return_value = mock_root

        show_error_message("Test error message")
        mock_tk.assert_called_once()
        mock_showerror.assert_called_once_with("Error", "Test error message")
        mock_root.destroy.assert_called_once()

    @patch('statistics_summary.read_data')
    @patch('statistics_summary.validate_data')
    @patch('statistics_summary.calculate_statistics')
    @patch('statistics_summary.show_statistics_results')
    @patch('statistics_summary.show_error_message')
    def test_statistics_summary(self, mock_show_error_message, mock_show_statistics_results, mock_calculate_statistics, mock_validate_data, mock_read_data):
        mock_read_data.return_value = pd.DataFrame({'A': [1, 2, 3]})
        mock_validate_data.return_value = True
        mock_calculate_statistics.return_value = {'mean': pd.Series([1.0], index=['A'])}

        summary = statistics_summary('test.csv')
        mock_read_data.assert_called_once_with('test.csv')
        mock_validate_data.assert_called_once_with(mock_read_data.return_value)
        mock_calculate_statistics.assert_called_once_with(mock_read_data.return_value)
        mock_show_statistics_results.assert_called_once_with(mock_calculate_statistics.return_value)
        self.assertEqual(summary, mock_calculate_statistics.return_value)

if __name__ == '__main__':
    unittest.main()