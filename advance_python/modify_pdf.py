# from pypdf import PdfReader
# from pathlib import Path

# pdf_path = (
#     Path.home()
#     / "creating-and-modifying-pdfs"
#    / "practice_files"
# / "Pride_and_Prejudice.pdf"
# )

# pdf_reader = PdfReader(pdf_path)

# # len(pdf_reader.pages)
# # pdf_reader.metadata
# # pdf_reader.metadata.title


# text_file =  Path.home() / "Pride_and_Prejudice.txt"

# content = [
#     f"{pdf_reader.metadata.title}",
#     f"Number Of Pages: {len(pdf_reader.pages)}"
# ]

# for page in pdf_reader.pages:
#     content.append(page.extract_text())

# text_file.write_text("\n".join(content))


# pdf_path = (
#     Path.home()
#     / "pratice-pdf-exercise"
#     / "zen.pdf"
# )

# pdf_reader = PdfReader(pdf_path)

# text_file = Path.home() / "zen-G.txt"

# contents = [
#     f"{pdf_reader.metadata.title}",
#     f"Number Of Pages: {len(pdf_reader.pages)}"
# ]


# for page in pdf_reader.pages:
#     contents.append(page.extract_text())

# text_file.write_text("\n".join(contents),encoding="utf-8")


# retreive page or range of pages from pdf and saving it to another pdf file.

# from pypdf import PdfWriter

# pdf_writer = PdfWriter()

# # add a balank page to the pdf_writer object before you can save them.

# pdf_writer.add_blank_page(width=8.27*72,height=11.7*72)
# pdf_writer.write("blank.pdf")



# Extract firs chapter from pdf and save it ti another.

# from pathlib import Path
# from pypdf import PdfReader,PdfWriter

# pdf_path =  (
#     Path.home()
#     / "creating-and-modifying-pdfs"
#     / "practice_files"
#     / "Pride_and_Prejudice.pdf"
# )

# input_pdf = PdfReader(pdf_path)

# # output_pdf = PdfWriter()
# # for page in input_pdf.pages[1:4]:
# #     output_pdf.add_page(page)

# # output_pdf.write("chapter-1.pdf")

# # extract last page and store it into the pdf
# output_pdf = PdfWriter()
# output_pdf.add_page(input_pdf.pages[-1])
# output_pdf.write("last-page.pdf")


# MERGING AND CONCATENATING PDF FILES.

from pathlib import Path
from pypdf import PdfWriter

reports_dir = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "expense_reports"
)

# for path in reports_dir.glob("*.pdf"):
#     print(path.name)
expense_reports = sorted(reports_dir.glob("*.pdf"))

pdf_merger = PdfWriter()
for path in expense_reports:
    # print(path.name)
    pdf_merger.append(path)


pdf_merger.write("monthly-expense-reports.pdf")

