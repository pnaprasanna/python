import PyPDF2, sys	#pip3 install PyPDF2
from gtts import gTTS	#pip3 install gTTs


pdfFileObj = open("story.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

mytext = ""

for pageNum in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)

    mytext += pageObj.extractText()

sys.stdout = open("story.txt", "w")    
print(mytext)
sys.stdout.close()

pdfFileObj.close()

tts = gTTS(text=mytext, lang='en')
tts.save("story.mp3")
