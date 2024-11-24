import csv
import io
from io import BytesIO
import os
from openpyxl import Workbook # type: ignore

def text_files_to_XLSX(files, output_filename):
    wb = Workbook()
    ws = wb.active

    for f in files:
        directory, filename = os.path.split(f)
        with open(f) as of:
            txt = of.read().strip()
        row, column = map(int, filename.split(".")[0].split("-"))
        # Openpyxl uses 1-based indexing, so we adjust row and column
        ws.cell(row=row + 1, column=column + 1, value=txt)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    wb.save(output_filename)
    virtual_workbook = BytesIO()
    wb.save(virtual_workbook)
    virtual_workbook.seek(0)  

    return virtual_workbook.getvalue()

def text_files_to_csv(files, output_filename):
    """Files must be sorted lexicographically
    Filenames must be <row>-<column>.txt.
    000-000.txt
    000-001.txt
    001-000.txt
    etc...
    """
    rows = []
    for f in files:
        directory, filename = os.path.split(f)
        with open(f) as of:
            txt = of.read().strip()
        row, column = map(int, filename.split(".")[0].split("-"))
        while row >= len(rows):
            rows.append([])
        rows[row].append((column, txt))

    # Sort each row by column number and replace each tuple with just the text
    for row in rows:
        row.sort(key=lambda x: x[0])
        for i in range(len(row)):
            row[i] = row[i][1]

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)

    # Write the CSV file and save it
    with open(output_filename, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

    # Create a StringIO object to return the CSV content
    csv_content = io.StringIO()
    writer = csv.writer(csv_content)
    writer.writerows(rows)
    csv_content.seek(0)  # Rewind the StringIO object to the beginning
    return csv_content.getvalue()

def main(files, save_path, format_file):
    if format_file == 'CSV':
        return text_files_to_csv(files, save_path)
    else:
        return text_files_to_XLSX(files, save_path)