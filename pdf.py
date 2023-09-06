# This program makes text unselectable on PDFs and removes any other meta-data

# Instructions

# 1. Download python

# 2. Run the command:
# pip install -r requirements.txt

# 3. Put your PDF file in the folder Input_Images

# 4. Click play in VS Code

from pdf2image import convert_from_path
from PIL import Image
from pypdf import PdfMerger
import os

# Global Directories
####################################################################################################
poppler_path = os.path.abspath(f"poppler-23.07.0\\Library\\bin")
input_pdf_dir = os.path.abspath(f"Input_Images")
pdf_dir = os.path.abspath(f"Working_dir_PDFs")
png_dir = os.path.abspath(f"Working_dir_images")
####################################################################################################

# A key function for built in python sort() function
def file_sort_key(file):
    file_num = file.split('.')[0]
    return int(file_num)
     
# Converts PDF images to PNG
def pdf_to_img(pdf_path):
    pdf_path = os.path.join(input_pdf_dir, pdf_path)

    # Uses pdf2image library to get all PDF page data into array
    pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

    i = 1
    for page in pages:
        img_name = f"{i}.png"

        # Saves page as PNG thus removing all selectable-data and meta-data
        page.save(os.path.join(png_dir, img_name), "PNG")

        i += 1

####################################################################################################

# Converts PNG images to PDF
def img_to_pdf():

    for file in os.listdir(png_dir):
        # Checks if file is an image
        if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
            # Convert image to PDF
            image = Image.open(os.path.join(png_dir, file))
            image_converted = image.convert('RGB')
            image_converted.save(os.path.join(pdf_dir, '{0}.pdf'.format(file.split('.')[-2])))

    # Sort the generated PDF images by their original order in 'pdfs' array
    pdfs = []
    for file in os.listdir(pdf_dir):
        pdfs.append(file)

    pdfs.sort(key=file_sort_key)

    merger = PdfMerger()

    # Merge sorted PDFS together
    for pdf in pdfs:
        full_path_pdf = os.path.join(pdf_dir, pdf)
        merger.append(full_path_pdf)

    merger.write("result.pdf")
    merger.close()

# Clears working directories
################################################
for file in os.listdir(png_dir):
        os.remove(os.path.join(png_dir, file))

for file in os.listdir(pdf_dir):
        os.remove(os.path.join(pdf_dir, file))
################################################

# Calls pdf conversion functions
for file in os.listdir(input_pdf_dir):

    # Checks if inputed images are truly PDF files
    if file.split('.')[-1] in ('pdf'):
        pdf_to_img(file)

img_to_pdf()

