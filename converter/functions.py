from pdf2docx import Converter
from PIL import Image
import os
from pydub import AudioSegment 
from docx2pdf import convert

def pdf2doc(doc):
    file_name, extension = os.path.splitext(doc)

    cv = Converter(doc)
    cv.convert(file_name + '.docx')
    cv.close()

def convertImage(img):
    file_name, extension = os.path.splitext(img)

    if extension == 'jpg':
        img = Image.open(img)
        img.save(file_name + '.png')
        img.close()
    else:
        img = Image.open(img)
        img.save(file_name + '.jpg')
        img.close()

def doc2pdf(doc): # directory de verilebilir ama sonuna / konulmali
    convert(doc)

# denenmedi bu function
def wav2mp3(doc):
    file_name, extension = os.path.splitext(doc)
    
    sound = AudioSegment.from_mp3(doc) 
    sound.export(file_name, format="wav")
    


    