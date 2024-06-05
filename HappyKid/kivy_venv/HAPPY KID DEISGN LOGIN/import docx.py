import docx

# Load the document
file_path = "/mnt/data/Chapter II.docx"
doc = docx.Document(file_path)

# Read the document content
doc_text = []
for paragraph in doc.paragraphs:
    doc_text.append(paragraph.text)

# Join the text to make it easier to search
full_text = "\n".join(doc_text)
full_text[:2000]  # Display the first 2000 characters to understand the content structure
