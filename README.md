### Requirements:
 - I would like to backup my wordpress blog content as HTML/MD/PDF files

## Mandatory Installation:
#### python3 pip
 - pypandoc
 - pdfkit
#### OS Level (Windows/Mac/Linux)
 - wkhtmltox (also need to be added as env. variable, otherwise the script will throw the error related with wkhtmltox)

 ## Procedures
 0. Download XML from wordpress export
 1. Run `python3 xml2md.py` to convert the exported wordpress xml file to .md files to /training folder
 2. Run `python .\md2pdf.py -p ./training` to generate some .pdf files to /pdfs directory, and also generate some .html files on /htmls direcotory
 3. Merge .pdf files from a specific directory (or from pdfs directory) or by manually inputting by `python3 pdf_concat.py`