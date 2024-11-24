import sys

from Cell_Extract import main

paths = main(sys.argv[1])
print("\n".join(paths))
