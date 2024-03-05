from PyPDF2 import PdfWriter, PdfReader
import fnmatch
import os


def scan_folder() -> dict:
    pdf_dict = {}
    print(os.path.abspath("."))
    for _, _, files in os.walk("."):
        pdfs = fnmatch.filter(files, "*.pdf")
        # print(f"files>>:{files}")
        for index, pdf in enumerate(pdfs, start=1):
            print(f"{index}. -> {pdf}")
            pdf_dict[index] = pdf
    return pdf_dict


def get_and_validate_input(pdf_dict: dict) -> list:
    valid_input = False
    while not valid_input:
        try:
            choice = input("please select index of file:")
            pdffile = pdf_dict[int(choice.strip())]
            valid_input = True
        except:
            print("invalid input. try again")
    return pdffile


def decryptpdf(pdffile):
    reader = PdfReader(pdffile)
    writer = PdfWriter()
    if reader.is_encrypted():
        passwd = input(f"please enter password for {pdffile}:")
        reader.decrypt(passwd)
    for page in reader.pages:
        writer.add_page(page)

    with open(f"unlocked_{pdffile}", "wb") as f:
        writer.write(f)


def main():
    file_dict = scan_folder()
    if len(file_dict.keys()) != 0:
        pdffile = get_and_validate_input(file_dict)
        # print(pdffile)
        decryptpdf(pdffile)
    else:
        print("No pdf found!")


if __name__ == "__main__":
    main()
