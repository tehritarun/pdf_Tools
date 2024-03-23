from PyPDF2 import PdfWriter, PdfReader
import fnmatch
import os
from datetime import datetime

timestamp = datetime.now().strftime('%Y%m%d_%H%M')


def scan_folder() -> dict:
    pdf_dict = {}
    print(os.path.abspath("."))
    for _, _, files in os.walk("."):
        pdfs = fnmatch.filter(files, "*.pdf")
        for index, pdf in enumerate(pdfs, start=1):
            pdf_dict[index] = pdf
    return pdf_dict


def merge_pdf(pdf_list: list):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(f"merged_pdf_{timestamp}.pdf")
    merger.close()
    quit()


def decryptpdf(pdffile, passwd):
    reader = PdfReader(pdffile)
    writer = PdfWriter()
    if reader.is_encrypted:
        reader.decrypt(passwd)
    for page in reader.pages:
        writer.add_page(page)

    with open(f"unlocked_{timestamp}_{pdffile}", "wb") as f:
        writer.write(f)
    quit()
