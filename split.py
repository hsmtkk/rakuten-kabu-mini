import pypdf

with open("pdf/pdf_01.pdf", "rb") as f:
    pdf = pypdf.PdfReader(f)
    for i in range(len(pdf.pages)):
        writer = pypdf.PdfWriter()
        writer.add_page(pdf.pages[i])
        with open(f"pdf/page-{i}.pdf", "wb") as g:
            writer.write(g)
