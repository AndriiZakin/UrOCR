import pandas as pd

# Create a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('test_data.xlsx', index=False)