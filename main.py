import os
import fitz
import pandas as pd

from datetime import datetime

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

# =========================================================
# PROJECT PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_DIR, "input")

OUTPUT_FOLDER = os.path.join(BASE_DIR, "output")

TEMP_FOLDER = os.path.join(BASE_DIR, "temp")

# =========================================================
# CREATE FOLDERS
# =========================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

os.makedirs(TEMP_FOLDER, exist_ok=True)

# =========================================================
# EXCEL FILES
# =========================================================

CLIENT_FILE = os.path.join(
    INPUT_FOLDER,
    "ClientInputData.xlsx"
)

PORTFOLIO_FILE = os.path.join(
    INPUT_FOLDER,
    "ConsolidatePortfolio.xlsx"
)

# =========================================================
# LOAD EXCEL FILES
# =========================================================

client_df = pd.read_excel(CLIENT_FILE)

portfolio_df = pd.read_excel(PORTFOLIO_FILE)

print("\nExcel Files Loaded Successfully!")

# =========================================================
# PDF FILES
# =========================================================

PDF_FILES = [

    "HSBC Large Cap.pdf",

    "HSBC Equity Fund.pdf",

    "HSBC Ultra Short Duration Fund.pdf"

]

# =========================================================
# PROCESS ALL PDF FILES
# =========================================================

for pdf_name in PDF_FILES:

    print(f"\nProcessing: {pdf_name}")

    # =====================================================
    # INPUT PDF PATH
    # =====================================================

    pdf_path = os.path.join(
        INPUT_FOLDER,
        pdf_name
    )

    # =====================================================
    # CHECK FILE EXISTS
    # =====================================================

    if not os.path.exists(pdf_path):

        print(f"Missing File: {pdf_name}")

        continue

    # =====================================================
    # OPEN PDF
    # =====================================================

    doc = fitz.open(pdf_path)

    total_pages = len(doc)

    # =====================================================
    # OUTPUT PDF PATH
    # =====================================================

    output_pdf_path = os.path.join(
        OUTPUT_FOLDER,
        pdf_name
    )

    # =====================================================
    # CREATE NEW PDF
    # =====================================================

    c = canvas.Canvas(
        output_pdf_path,
        pagesize=A4
    )

    width, height = A4

    # =====================================================
    # PROCESS EACH PAGE
    # =====================================================

    for page_number in range(total_pages):

        print(f"Processing Page: {page_number + 1}")

        # -------------------------------------------------
        # LOAD PAGE
        # -------------------------------------------------

        page = doc.load_page(page_number)

        # -------------------------------------------------
        # CONVERT PAGE TO IMAGE
        # -------------------------------------------------

        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )

        # -------------------------------------------------
        # TEMP IMAGE PATH
        # -------------------------------------------------

        temp_image = os.path.join(
            TEMP_FOLDER,
            f"{pdf_name}_{page_number}.png"
        )

        pix.save(temp_image)

        # -------------------------------------------------
        # DRAW PAGE IMAGE
        # -------------------------------------------------

        bg = ImageReader(temp_image)

        c.drawImage(
            bg,
            0,
            0,
            width=width,
            height=height
        )

        # =================================================
        # OPTIONAL DYNAMIC OVERLAY
        # =================================================

        # -------------------------------------------------
        # GENERATED LABEL
        # -------------------------------------------------

        c.setFillColor(colors.red)

        c.setFont(
            "Helvetica-Bold",
            8
        )

        c.drawString(
            430,
            10,
            "Generated Using Python Automation"
        )

        # -------------------------------------------------
        # DATE
        # -------------------------------------------------

        today = datetime.today().strftime(
            "%d-%m-%Y"
        )

        c.setFillColor(colors.black)

        c.setFont(
            "Helvetica",
            7
        )

        c.drawString(
            500,
            15,
            today
        )

        # -------------------------------------------------
        # CLIENT NAME
        # -------------------------------------------------

        try:

            client_name = str(
                client_df.iloc[0, 0]
            )

        except:

            client_name = "Client"

        c.setFont(
            "Helvetica",
            7
        )

        c.drawString(
            40,
            15,
            f"Client: {client_name}"
        )

        # =================================================
        # NEXT PAGE
        # =================================================

        c.showPage()

    # =====================================================
    # SAVE PDF
    # =====================================================

    c.save()

    print(f"\nCreated Successfully:")
    print(output_pdf_path)

# =========================================================
# FINISHED
# =========================================================

print("\nALL PDF FILES GENERATED SUCCESSFULLY!")