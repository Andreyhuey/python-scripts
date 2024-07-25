from pdf2docx import Converter
import os

def pdf_to_word(pdf_file, word_file):
    try:
        # Check if the PDF file exists before proceeding
        if not os.path.exists(pdf_file):
            raise FileNotFoundError(f"No such file: '{pdf_file}'")
        
        # Create a Converter object
        cv = Converter(pdf_file)
        
        # Convert the PDF to a Word document
        cv.convert(word_file, start=0, end=None)
        
        # Close the converter
        cv.close()
        
        print(f"Conversion successful! '{word_file}' has been created.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Folders
    src_folder = 'src'
    build_folder = 'build'
    
    # Ensure the 'src' folder exists
    if not os.path.exists(src_folder):
        print(f"Error: The folder '{src_folder}' does not exist.")
    else:
        # File names
        pdf_file = 'sample.pdf'
        word_file_name = 'output.docx'
        
        # Construct the full path to the PDF file
        pdf_path = os.path.abspath(os.path.join(src_folder, pdf_file))
        
        # Ensure the 'build' folder exists or create it
        build_path = os.path.abspath(build_folder)
        if not os.path.exists(build_path):
            os.makedirs(build_path)
        
        # Construct the full path for the output Word file
        word_path = os.path.join(build_path, word_file_name)
        
        # Call the conversion function
        pdf_to_word(pdf_path, word_path)
