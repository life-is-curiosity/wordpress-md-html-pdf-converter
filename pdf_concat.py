import sys
from glob import glob
try:
    from PyPDF2 import PdfReader, PdfWriter
    from PyPDF2 import PdfMerger
except ImportError:
    from pyPdf import PdfFileReader, PdfFileWriter

def read_and_merge_from_dir_2():
    merger = PdfMerger()
    allpdfs = [a for a in glob("*.pdf")]
    [merger.append(pdf) for pdf in allpdfs]
    with open("merged_pdfs.pdf", "wb") as new_file:
        merger.write(new_file)

def read_and_merge_from_dir():
    x = [a for a in os.listdir() if a.endswith(".pdf")]
    merger = PdfMerger()
    for pdf in x:
        merger.append(open(pdf, 'rb'))
    with open("result.pdf", "wb") as fout:
        merger.write(fout)

def pdf_cat(input_files, output_stream):
    input_streams = []
    try:
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfWriter()
        for reader in map(PdfReader, input_streams):
            for n in range(len(reader.pages)):
                writer.add_page(reader.pages[n])
        writer.write(output_stream)
    finally:
        for f in input_streams:
            f.close()
        output_stream.close()

if __name__ == '__main__':
    if sys.platform == "win32":
        import os, msvcrt
        msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)
    pdf_cat(sys.argv[1:], sys.stdout)