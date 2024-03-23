from PyPDF2 import PdfWriter
import fnmatch
import os


def scan_folder() -> dict:
    pdf_dict = {}
    print(os.path.abspath("."))
    for _, _, files in os.walk("."):
        pdfs = fnmatch.filter(files, "*.pdf")
        for index, pdf in enumerate(pdfs, start=1):
            print(f"{index}. -> {pdf}")
            pdf_dict[index] = pdf
    return pdf_dict


def get_and_validate_input(pdf_dict: dict) -> list:
    valid_input = False
    while not valid_input:
        try:
            choice = input("please enter index in order:[eg. 1,3,2]:")
            listpdf = []
            for pdf_index in choice.split(","):
                listpdf.append(pdf_dict[int(pdf_index.strip())])
            valid_input = True
        except:
            print("invalid input. try again")
    return listpdf


def merge_pdf(pdf_list: list):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged_pdf.pdf")
    merger.close()


def main():
    file_dict = scan_folder()
    if len(file_dict.keys()) != 0:
        pdf_list = get_and_validate_input(file_dict)
        merge_pdf(pdf_list)
    else:
        print("No pdf found!")


if __name__ == "__main__":
    main()
