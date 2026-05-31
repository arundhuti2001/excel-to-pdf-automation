# excel-to-pdf-automation
Automated PDF report generation from Excel and PDF inputs using Python, Pandas, ReportLab, and PyMuPDF.

# Excel to PDF Automation
## Overview

This project automates the generation of PDF reports using Excel datasets and fund factsheet PDFs. The solution reads client and portfolio information from Excel files, processes PDF documents, and generates customized output PDFs with dynamic overlays such as client details and report generation date.

## Features

- Read client and portfolio data from Excel files
- Process multiple PDF documents automatically
- Generate customized PDF reports
- Add dynamic client information
- Add report generation date
- Batch processing of multiple PDF files
- Automated report creation using Python

## Technologies Used

- Python
- Pandas
- PyMuPDF (fitz)
- ReportLab
- Pillow
- OpenPyXL

## Project Structure

```text
Excel-to-PDF-Automation/
│
├── main.py
├── requirements.txt
│
├── input/
│   ├── ClientInputData.xlsx
│   ├── ConsolidatePortfolio.xlsx
│   ├── HSBC Large Cap.pdf
│   ├── HSBC Equity Fund.pdf
│   └── HSBC Ultra Short Duration Fund.pdf
│
├── output/
│
└── temp/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/arundhuti2001/excel-to-pdf-automation.git
cd excel-to-pdf-automation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Required Packages

```text
pandas
openpyxl
PyMuPDF
reportlab
Pillow
```

## Usage

Place the required input files inside the `input` folder:

- ClientInputData.xlsx
- ConsolidatePortfolio.xlsx
- Fund Factsheet PDFs

Run the script:

```bash
python main.py
```

Generated reports will be saved in the `output` folder.

## Workflow

1. Read client information from Excel.
2. Read portfolio data from Excel.
3. Open fund factsheet PDFs.
4. Convert PDF pages to images.
5. Overlay dynamic information:
   - Client details
   - Report generation date
6. Generate customized PDF reports.
7. Save final reports to the output directory.

## Sample Output

The generated PDF includes:

- Original fund factsheet content
- Client identifier
- Report generation date
- Automation watermark

## Use Cases

- Financial Report Automation
- Portfolio Report Generation
- Wealth Management Reporting
- PDF Document Personalization
- FinTech Process Automation

## Author

**Arundhuti Dey**

M.Sc. Data Science & Analytics  
Python | SQL | Power BI | AI/ML | Data Analytics

LinkedIn: https://linkedin.com/in/arundhutidey-61429b1a9
