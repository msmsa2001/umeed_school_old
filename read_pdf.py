import sys
from pypdf import PdfReader

def extract_text(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"--- Page {i+1} ---\n"
            text += page.extract_text() + "\n"
        
        with open("pdf_content.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Successfully extracted text to pdf_content.txt")
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_text(sys.argv[1])
