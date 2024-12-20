import os
import sys

from OCR.Table_Extract import extract_tables
from OCR.Pdf_to_Images import pdf_to_images
from OCR.Cell_Extract import extract_cells
from OCR.Image_OCR import ocr_images
from OCR.OCR_to_Format import ocr_to_csv

#from GUI import create_ocr_gui

def if_pdf(filepath):
    _, file_extension = os.path.splitext(filepath)
    return file_extension.lower() == '.pdf'

def process_image(filepath, save_path, format_file):
    image_tables = extract_tables.main([filepath])
    print(f"Running `extract_tables.main([{filepath}]).`")
    print("Extracted the following tables from the image:")
    print(image_tables)
    
    for image, tables in image_tables:
        print(f"Processing tables for {image}.")
        for table in tables:
            print(f"Processing table {table}.")
            cells = extract_cells.main(table)
            ocr = [ocr_images.main(cell, None) for cell in cells]
            print(f"Extracted {len(ocr)} cells from {table}")
            print("Cells:")
            for c, o in zip(cells[:3], ocr[:3]):
                with open(o) as ocr_file:
                    text = ocr_file.read().strip()
                    print(f"{c}: {text}")
            if len(cells) > 3:
                print("...")
            csv_file = ocr_to_csv.main(ocr, save_path, format_file)
            #print(f"Generated CSV file: {csv_file}")
            return csv_file

def main(filepath, save_path, format_file):
    if if_pdf(filepath):
        images_filenames = pdf_to_images(filepath)
        for image in images_filenames:
            process_image(image, save_path, format_file)
    else:
        process_image(filepath, save_path, format_file)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("No file path provided.")