from langchain_community.document_loaders import PyPDFLoader

for i in range(18):
    loader = PyPDFLoader(f"pdf/page-{i}.pdf")
    docs = loader.load()
    content = docs[0].page_content
    with open(f"text/page-{i}.txt", "w", encoding="utf-8") as f:
        f.write(content)
