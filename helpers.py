import os
from pdf2image import convert_from_path


def pdf_to_jpg():
    # Replace with the directory path where your PDF files are located
    file_directory = "YOUR_PATH_HERE"
    output_directory = "./static"

    pdf_files = [file for file in os.listdir(
        file_directory) if file.endswith('.pdf')]

    for file in pdf_files:
        pages = convert_from_path(file_directory + '/' + file, 500,
                                  poppler_path="BIN_PATH_HERE")
        for page in pages:
            # Change the file extension to whatever you want
            page.save(output_directory + '/' + file[:-4] + '.jpg', 'JPEG')
