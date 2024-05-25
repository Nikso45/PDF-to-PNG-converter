import os
import shutil
import subprocess
import fitz  # PyMuPDF

def pdf_to_png(input_folder, output_folder, used_pdf_folder):
    # Check if the output folder exists, if not, create them
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    if not os.path.exists(used_pdf_folder):
        os.makedirs(used_pdf_folder)

    # Iterate through all PDF files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(input_folder, filename)
            base_filename = os.path.splitext(filename)[0]

            # Open the PDF-File
            pdf_document = fitz.open(input_path)

            # Iterate through all sites of the PDFs
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)  # Load the sites
                pix = page.get_pixmap()  # Create a Pixmap-Object
                output_path = os.path.join(output_folder, f"{base_filename}_page_{page_num + 1}.png")
                pix.save(output_path)  # Saving the Pixmap-Object as PNG

                print(f"{filename} - Page {page_num + 1} was converted {output_path} after.")

            # Close the PDF-File
            pdf_document.close()

            # Move the PDF-File to the used_pdf_folder
            used_pdf_path = os.path.join(used_pdf_folder, filename)
            shutil.move(input_path, used_pdf_path)

    # Delete all PDF-Files in the Input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.pdf'):
            os.remove(os.path.join(input_folder, filename))

if __name__ == "__main__":
    input_folder = "HERE\IS\YOUR\PATH\TO\PDF"  # Replace this path with the path of your input folder
    output_folder = "HERE\IS\YOUR\PATH\TO\OUTPUT"  # output folder
    used_pdf_folder = "HERE\IS\YOUR\PATH\FOR\USED-PDF"  # folder for used PDF-Files

    pdf_to_png(input_folder, output_folder, used_pdf_folder)
