# Usage Guide

## Requirements

- Python
- PyMuPdf

  Change your Repository:
  
  input_folder = "Write here your path to the PDF-Files"
  output_folder = "Write here your path to the folder for the convertet PNG"
  used_pdf_folder = "Write here your path to the folder for saving your used PDF-Files"

  When you are done every time processing your Data, the used PDF-files will be deleted in your input-folder. Thats why I wrote that your PDF-Files will be saved in an other folder.
  Change the start_python.bat file with your file path to the python file. If you don't change much it should be "C:\User\...\pdf_to_png.py".

  
Install dependencies:
  ```bash
  pip install Fitz
  pip install Fitz


