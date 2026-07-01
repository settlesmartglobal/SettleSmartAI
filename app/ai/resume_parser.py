import fitz
import re


class ResumeParser:

    def parse(self, pdf_path):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    def extract_name(self, text):

        lines = text.split("\n")

        for line in lines:
            line = line.strip()

            if len(line) > 3:
                return line

        return ""

    def extract_email(self, text):

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )

        return match.group(0) if match else ""

    def extract_phone(self, text):

        match = re.search(
            r"(\+?\d[\d\s\-]{8,}\d)",
            text
        )

        return match.group(0) if match else ""

    def resume_data(self, pdf_path):

        text = self.parse(pdf_path)

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "text": text
        }