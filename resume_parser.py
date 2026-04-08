import docx2txt
import PyPDF2
import pdfplumber


def extract_text_from_pdf(file_path):

    text = ""

    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except:
        pass

    if text.strip() == "":
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
        except:
            pass

    return text


def extract_text_from_docx(file_path):

    text = docx2txt.process(file_path)

    if text:
        return text
    else:
        return ""


def extract_text_from_txt(file_path):

    text = ""

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except:
        pass

    return text


def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)

    elif file_path.endswith(".txt"):
        return extract_text_from_txt(file_path)

    else:
        return ""