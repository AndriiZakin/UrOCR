import os
import re
import subprocess
from PIL import Image
from contextlib import contextmanager
from OCR.util import get_logger

logger = get_logger(__name__)

@contextmanager
def working_dir(path):
    """
    A context manager to temporarily change the working directory.
    """
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(old_dir)

def pdf_to_images(pdf_filepath):
    """
    Turn a PDF into images.
    Returns the filenames of the created images sorted lexicographically.
    """
    directory, filename = os.path.split(pdf_filepath)
    image_filenames = pdf_images(pdf_filepath)

    return sorted([os.path.join(directory, f) for f in image_filenames])

def pdf_images(pdf_filepath):
    """
    Uses the `pdfimages` utility from Poppler to create images out of each page.
    Images are prefixed by their name sans extension and suffixed by their page number.
    After creation, images are rotated 90 degrees to the left to correct their orientation.
    """
    directory, filename = os.path.split(pdf_filepath)
    if not os.path.isabs(directory):
        directory = os.path.abspath(directory)
    filename_sans_ext = os.path.splitext(filename)[0]

    with working_dir(directory):
        result = subprocess.run(["pdfimages", "-png", filename, filename_sans_ext], capture_output=True)
        if result.returncode != 0:
            logger.error(f"Error running pdfimages: {result.stderr.decode().strip()}")
            return []

    image_filenames = find_matching_files_in_dir(filename_sans_ext, directory)
    
    # Rotate images to correct their orientation
    for image_filename in image_filenames:
        image_path = os.path.join(directory, image_filename)
        with Image.open(image_path) as img:
            rotated_img = img.rotate(90, expand=True)  # Rotate 90 degrees to the left
            rotated_img.save(image_path)

    logger.debug(f"Converted and rotated {pdf_filepath} into files:\n" + "\n".join(image_filenames))
    return image_filenames

def find_matching_files_in_dir(file_prefix, directory):
    pattern = re.compile(rf"{re.escape(file_prefix)}-\d{{3}}.*\.png")
    files = [filename for filename in os.listdir(directory) if pattern.match(filename)]
    return files