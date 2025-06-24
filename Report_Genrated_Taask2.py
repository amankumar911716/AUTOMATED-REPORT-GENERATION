import os
import pandas as pd
from fpdf import FPDF

# -----------------------------
# STEP 1: Ensure 'data.csv' exists
# -----------------------------

file_path = 'data.csv'

# Auto-create sample data if file doesn't exist

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        f.write("Name,Score,Grade\nAMAN KUMAR,88,A\nARYAN,83,B\nKOMAL KUMARI,82,C\nHIMESH KUMAR,80,D\nMUKESH KUMAR,79,E\nRIMANSHU KUMAR,75,F\n")
    print("Sample 'data.csv' created.\n")

# -----------------------------
# STEP 2: Load Data
# -----------------------------

df = pd.read_csv(file_path)

# -----------------------------
# STEP 3: Analyze Data
# -----------------------------

average_score = df['Score'].mean()
topper = df.loc[df['Score'].idxmax(), 'Name']

# -----------------------------
# STEP 4: Create PDF Report
# -----------------------------

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Performance Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Summary section

pdf.cell(0, 10, f"Total Students: {len(df)}", ln=True)
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(0, 10, f"Topper: {topper}", ln=True)
pdf.ln(10)

# Table Header

pdf.set_font("Arial", "B", 12)
pdf.cell(50, 10, "Name", 1)
pdf.cell(40, 10, "Score", 1)
pdf.cell(40, 10, "Grade", 1)
pdf.ln()

# Table Rows

pdf.set_font("Arial", size=12)
for _, row in df.iterrows():
    pdf.cell(50, 10, str(row['Name']), 1)
    pdf.cell(40, 10, str(row['Score']), 1)
    pdf.cell(40, 10, str(row['Grade']), 1)
    pdf.ln()

# Save PDF

pdf.output("student_report.pdf")
print("PDF Report Generated: student_report.pdf")
