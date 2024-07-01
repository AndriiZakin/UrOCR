import sys

from STEP2_cell_extract import main

paths = main(sys.argv[1])
print("\n".join(paths))
