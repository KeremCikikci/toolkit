from PyPDF2 import PdfWriter

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

import fitz
from ebooklib import epub

from PIL import Image

import os
import subprocess

def merge(pdfs):
    merger = PdfWriter()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write("merged_" + pdfs[0])

def split(PyPDF2, pdf_yolu, bolme_noktalari):
    try:
        # PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Belirtilen bölme noktaları üzerinden döngü
            for i, bolme_noktasi in enumerate(bolme_noktalari):
                hedef_icin_pdf = PyPDF2.PdfFileWriter()
                
                # Belirtilen sayfa numarasına kadar içeriği al
                for sayfa_index in range(bolme_noktasi):
                    hedef_icin_pdf.addPage(pdf_okuyucu.getPage(sayfa_index))
                
                # Yeni PDF dosyasını oluştur
                yeni_pdf_ad = f"{pdf_yolu.split('.')[0]}_{i+1}.pdf"
                with open(yeni_pdf_ad, 'wb') as hedef_dosya:
                    hedef_icin_pdf.write(hedef_dosya)
                    
        print("PDF dosyası başarıyla bölündü.")
    except Exception as e:
        print("Hata:", str(e))

def rotate(PyPDF2, pdf_yolu, dondurme_sayisi, döndürülecek_sayfalar=None):
    try:
        # PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_yazici = PyPDF2.PdfFileWriter()
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Döndürülecek sayfaların belirlenmesi
            if döndürülecek_sayfalar is None:
                döndürülecek_sayfalar = range(pdf_okuyucu.numPages)
            
            # Belirtilen sayfa numaraları üzerinden döngü
            for sayfa_index in range(pdf_okuyucu.numPages):
                if sayfa_index in döndürülecek_sayfalar:
                    sayfa = pdf_okuyucu.getPage(sayfa_index)
                    for _ in range(dondurme_sayisi):
                        sayfa.rotateClockwise(90)
                    pdf_yazici.addPage(sayfa)
                else:
                    pdf_yazici.addPage(pdf_okuyucu.getPage(sayfa_index))
            
            # Yeni PDF dosyasını oluştur
            with open(f"rotated_{pdf_yolu}", 'wb') as yeni_pdf:
                pdf_yazici.write(yeni_pdf)
                
        print("PDF sayfaları başarıyla döndürüldü.")
    except Exception as e:
        print("Hata:", str(e))

def extract(PyPDF2, pdf_yolu, sayfa_araligi):
    try:
        # PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Yeni PDF dosyasını oluştur
            yeni_pdf_adi = f"{pdf_yolu.split('.')[0]}_{sayfa_araligi[0]}_{sayfa_araligi[1]}.pdf"
            yeni_pdf = PyPDF2.PdfFileWriter()
            
            # Belirtilen sayfa aralığını diğer PDF dosyasına kopyala
            for sayfa_index in range(sayfa_araligi[0] - 1, sayfa_araligi[1]):
                yeni_pdf.addPage(pdf_okuyucu.getPage(sayfa_index))
            
            # Yeni PDF dosyasını kaydet
            with open(yeni_pdf_adi, 'wb') as yeni_pdf_dosyasi:
                yeni_pdf.write(yeni_pdf_dosyasi)
                
        print("PDF sayfaları başarıyla çıkartıldı.")
    except Exception as e:
        print("Hata:", str(e))

def number(PyPDF2, pdf_yolu, numara_yeri=(550, 30)):
    try:
        # Orjinal PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Yeni PDF dosyasını oluştur
            yeni_pdf_adi = f"{pdf_yolu.split('.')[0]}_numaralı.pdf"
            yeni_pdf = PyPDF2.PdfFileWriter()
            
            # Numaralandırılmış sayfaları oluştur
            for sayfa_index in range(pdf_okuyucu.numPages):
                sayfa = pdf_okuyucu.getPage(sayfa_index)
                genislik = sayfa.mediaBox.getWidth()
                yukseklik = sayfa.mediaBox.getHeight()
                
                # Numaralandırma için bir PDF sayfası oluştur
                numara_sayfasi = canvas.Canvas("temp.pdf", pagesize=letter)
                numara_sayfasi.drawString(genislik - 100, 30, str(sayfa_index + 1))
                numara_sayfasi.save()
                
                # Numaralandırılmış sayfayı birleştir
                with open("temp.pdf", 'rb') as numara_dosyasi:
                    numara_pdf = PyPDF2.PdfFileReader(numara_dosyasi)
                    numaralandirilmis_sayfa = numara_pdf.getPage(0)
                    numaralandirilmis_sayfa.mergePage(sayfa)
                    yeni_pdf.addPage(numaralandirilmis_sayfa)
                
                # Geçici PDF dosyasını sil
                os.remove("temp.pdf")
            
            # Numaralandırılmış PDF dosyasını kaydet
            with open(yeni_pdf_adi, 'wb') as yeni_pdf_dosyasi:
                yeni_pdf.write(yeni_pdf_dosyasi)
                
            print("PDF sayfaları başarıyla numaralandırıldı.")
    except Exception as e:
        print("Hata:", str(e))

def pdf_to_epub(PyPDF2, pdf_path):
    try:
        # EPUB dosyasını oluştur
        epub_path = f"{os.path.splitext(pdf_path)[0]}.epub"
        kitap = epub.EpubBook()
        
        # PDF dosyasını aç
        with open(pdf_path, 'rb') as pdf_file:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_file)
            
            # Her sayfa için içerik al
            for sayfa_index in range(pdf_okuyucu.numPages):
                sayfa = pdf_okuyucu.getPage(sayfa_index)
                icerik = sayfa.extractText()
                
                # EPUB'a eklemek için yeni bir bölüm oluştur
                bolum = epub.EpubHtml(title=f"Sayfa {sayfa_index + 1}", file_name=f"page_{sayfa_index + 1}.xhtml", lang='tr')
                bolum.content = f"<html><body><p>{icerik}</p></body></html>"
                
                # Bölümü kitaba ekle
                kitap.add_item(bolum)
                kitap.toc.append((bolum, f"Sayfa {sayfa_index + 1}"))
        
        # Kitabı oluştur
        kitap.toc = tuple(kitap.toc)
        kitap.add_item(epub.EpubNcx())
        kitap.add_item(epub.EpubNav())
        kitap.spine = ['nav'] + [bolum]
        
        # EPUB dosyasını kaydet
        epub.write_epub(epub_path, kitap, {})
        
        print("PDF dosyası EPUB'a başarıyla dönüştürüldü.")
    except Exception as e:
        print("Hata:", str(e))

def png_to_pdf(png_files):
    try:
        if not png_files:
            raise ValueError("Hiç PNG dosyası bulunamadı.")
        
        # İlk PNG dosyasının adını al
        pdf_name = os.path.splitext(png_files[0])[0] + ".pdf"
        
        # Yeni bir PDF oluştur
        c = canvas.Canvas(pdf_name, pagesize=letter)
        
        # PNG dosyalarını PDF'e ekle
        for png_file in png_files:
            img = Image.open(png_file)
            width, height = img.size
            c.setPageSize((width, height))
            c.drawInlineImage(png_file, 0, 0)
            c.showPage()
        
        # PDF dosyasını kaydet
        c.save()
        
        print("PNG dosyaları PDF'e başarıyla dönüştürüldü.")
    except Exception as e:
        print("Hata:", str(e))

def page_remover(PyPDF2, pdf_yolu, silinecek_sayfalar):
    try:
        # Orjinal PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Yeni PDF dosyasını oluştur
            yeni_pdf_adi = f"{os.path.splitext(pdf_yolu)[0]}_düzenlenmis.pdf"
            yeni_pdf = PyPDF2.PdfFileWriter()
            
            # Silinmeyecek sayfaları yeni PDF'e ekle
            for sayfa_index in range(pdf_okuyucu.numPages):
                if sayfa_index not in silinecek_sayfalar:
                    sayfa = pdf_okuyucu.getPage(sayfa_index)
                    yeni_pdf.addPage(sayfa)
            
            # Yeni PDF dosyasını kaydet
            with open(yeni_pdf_adi, 'wb') as yeni_pdf_dosyasi:
                yeni_pdf.write(yeni_pdf_dosyasi)
                
            print("PDF sayfaları başarıyla silindi.")
    except Exception as e:
        print("Hata:", str(e))

def compress(PyPDF2, pdf_yolu):
    try:
        # Orjinal PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Yeni PDF dosyasını oluştur
            yeni_pdf_adi = f"{os.path.splitext(pdf_yolu)[0]}_sikistirilmis.pdf"
            yeni_pdf = PyPDF2.PdfFileWriter()
            
            # Her sayfanın sıkıştırma düzeyini ayarla
            for sayfa_index in range(pdf_okuyucu.numPages):
                sayfa = pdf_okuyucu.getPage(sayfa_index)
                sayfa.compress_content_streams()
                yeni_pdf.addPage(sayfa)
            
            # Yeni PDF dosyasını kaydet
            with open(yeni_pdf_adi, 'wb') as yeni_pdf_dosyasi:
                yeni_pdf.write(yeni_pdf_dosyasi)
                
            print("PDF başarıyla sıkıştırıldı.")
    except Exception as e:
        print("Hata:", str(e))

def sort(PyPDF2, pdf_yolu, siralama):
    try:
        # Orjinal PDF dosyasını aç
        with open(pdf_yolu, 'rb') as pdf_dosyasi:
            pdf_okuyucu = PyPDF2.PdfFileReader(pdf_dosyasi)
            
            # Yeni PDF dosyasını oluştur
            yeni_pdf_adi = f"{os.path.splitext(pdf_yolu)[0]}_siralanmis.pdf"
            yeni_pdf = PyPDF2.PdfFileWriter()
            
            # Sayfaları sıraya göre yeni PDF'e ekle
            for sayfa_index in siralama:
                sayfa = pdf_okuyucu.getPage(sayfa_index - 1)  # Sayfa indeksleri 0'dan başladığı için 1 çıkarıyoruz
                yeni_pdf.addPage(sayfa)
            
            # Yeni PDF dosyasını kaydet
            with open(yeni_pdf_adi, 'wb') as yeni_pdf_dosyasi:
                yeni_pdf.write(yeni_pdf_dosyasi)
                
            print("PDF sayfaları başarıyla sıralandı.")
    except Exception as e:
        print("Hata:", str(e))
