import docx
import makeDir

outputDir = '/output/'
makeDir.makeDir(outputDir)

doc = docx.Document()
doc.add_paragraph('Hello, World!')
# doc.save(output)
doc.save('./output/helloworld.docx')
