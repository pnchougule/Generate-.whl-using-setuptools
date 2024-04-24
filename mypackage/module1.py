import pandas as pd
import fitz
import os

def extract_excel_coordinates():
    excel_path = os.path.join(os.path.dirname(__file__), 'data', 'coordinates.xlsx')
    excel = pd.read_excel(excel_path)
    column = excel['coordinates'].apply(lambda x: tuple(map(float, str(x).strip('()').split(',')))).tolist()
    return column

def extract_pdf_by_coordinates():
    pdf_path = os.path.join(os.path.dirname(__file__), 'data', 'Form_K1.pdf')
    doc = fitz.open(pdf_path)
    coordinates = extract_excel_coordinates()
    for i in coordinates:
        print(doc[1].get_text("text", clip=(i)))


