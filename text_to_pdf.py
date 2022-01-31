from fpdf import FPDF


def text_to_pdf(text, folder_name):

    print("[*] Your transcription is being converted to PDF")

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=15)

    pdf.multi_cell(0, 10, txt=text, border=1, align='L')

    file_name = f"{folder_name}.pdf"
    pdf.output(file_name)

    print(f"Your transcription saved to {file_name}")
