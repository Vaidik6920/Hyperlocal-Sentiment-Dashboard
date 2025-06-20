from fpdf import FPDF
from datetime import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Hyperlocal Sentiment Report", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def generate_pdf_summary(df):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    summary = df["sentiment_label"].value_counts()
    total = len(df)

    pdf.cell(0, 10, f"Total Records Analyzed: {total}", ln=True)
    for sentiment, count in summary.items():
        pdf.cell(0, 10, f"{sentiment}: {count} ({count/total*100:.1f}%)", ln=True)

    pdf.cell(0, 10, f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
    return pdf

