import argparse
from STEP1a_table_extract import main

parsing = argparse.ArgumentParser()

parsing.add_argument("files", nargs="+")
args = parsing.parse_args()
files = args.files
results = main(files)

for image, tables in results:
    print("\n".join(tables))
