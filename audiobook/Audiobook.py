import pyttsx3
from PyPDF2 import PdfReader

# Open PDF
book = open('orv.pdf', 'rb')
pdfReader = PdfReader(book)

# Pages
pages = len(pdfReader.pages)
print("Total pages:", pages)

# Page
page = pdfReader.pages[4067]
text = page.extract_text()

# Speak
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()