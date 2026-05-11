from docx import Document

doc = Document('assets/Make2.docx')
text = ''
for para in doc.paragraphs:
    text += para.text + '\n'

with open('makes/week02.md', 'w') as f:
    f.write(text)