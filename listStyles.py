import docx


def getText(filename):
    doc = docx.Document(filename)
    print(doc.styles)
