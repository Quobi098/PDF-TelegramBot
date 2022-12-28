from PyPDF2 import PdfReader


def about_pdf(file):
    with open(file, "rb") as pdf_file:
        reader = PdfReader(pdf_file)
        return (f"<b>Автор файла</b>: {reader.metadata['/Author']}"
                f"\n<b>Название файла</b>: {reader.metadata['/Title']}"
                f"\n<b>Число страниц в файле</b>: {len(reader.pages)}")
