import cv2
import numpy as np
from tkinter import Tk, Canvas, Button, filedialog
from PIL import Image, ImageTk
import img2pdf

def kagit_tespit_ve_duzelt(imaj_yolu):
    # Görüntüyü yükle
    imaj = cv2.imread(imaj_yolu)
    orijinal_imaj = imaj.copy()

    # Gri tonlamalı görüntü elde et
    gri_imaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2GRAY)

    # Kenar tespiti yap
    kenarlar = cv2.Canny(gri_imaj, 50, 150)

    # Köşeleri algıla
    konturlar, _ = cv2.findContours(kenarlar.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    konturlar = sorted(konturlar, key=cv2.contourArea, reverse=True)

    for kontur in konturlar:
        # Konturun yaklaşık bir şeklini bul
        epsilon = 0.02 * cv2.arcLength(kontur, True)
        yaklasik_sekil = cv2.approxPolyDP(kontur, epsilon, True)

        # Kâğıt olduğunu varsayalım, dört köşe noktasını alalım
        if len(yaklasik_sekil) == 4:
            kagit_kose_noktalari = yaklasik_sekil
            break

    # Kâğıt köşelerini işaretle
    for nokta in kagit_kose_noktalari:
        x, y = nokta[0]
        cv2.circle(imaj, (x, y), 5, (0, 255, 0), -1)

    # Kullanıcı tarafından köşe noktalarını belirlemek için GUI oluştur
    def nokta_belirle(event):
        x, y = event.x, event.y
        cv2.circle(imaj, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow("Kâğıt Tespiti ve Düzeltme", imaj)

    def kaydet_ve_kapat():
        cv2.destroyAllWindows()

        # Kullanıcı tarafından işaretlenen noktaları al
        secilen_noktalar = []
        for nokta in kagit_kose_noktalari:
            secilen_noktalar.append([nokta[0][0], nokta[0][1]])

        # Kullanıcı tarafından işaretlenen noktaları kullanarak görüntüyü düzelt
        secilen_noktalar = np.array(secilen_noktalar)
        genislik = 500  # Düzeltilecek görüntünün genişliği
        yukseklik = 700  # Düzeltilecek görüntünün yüksekliği
        yeni_noktalar = np.array([[0, 0], [genislik, 0], [genislik, yukseklik], [0, yukseklik]], np.float32)
        transformasyon_matrix = cv2.getPerspectiveTransform(secilen_noktalar, yeni_noktalar)
        duzeltilmis_imaj = cv2.warpPerspective(orijinal_imaj, transformasyon_matrix, (genislik, yukseklik))

        # Düzeltme sonrası görüntüyü PDF'e dönüştür
        pdf_adi = imaj_yolu.replace(".jpg", "_duzeltilmis.pdf")
        with open(pdf_adi, "wb") as pdf_dosyasi:
            pdf_dosyasi.write(img2pdf.convert(duzeltilmis_imaj.tobytes()))

    # GUI oluştur
    pencere = Tk()
    pencere.title("Kâğıt Tespiti ve Düzeltme")
    pencere.geometry("800x600")

    imaj = cv2.cvtColor(imaj, cv2.COLOR_BGR2RGB)
    imaj = Image.fromarray(imaj)
    imaj = ImageTk.PhotoImage(image=imaj)

    cerceve = Canvas(pencere, width=800, height=600)
    cerceve.create_image(0, 0, anchor="nw", image=imaj)
    cerceve.pack()

    cerceve.bind("<Button-1>", nokta_belirle)

    kaydet_butonu = Button(pencere, text="Kaydet ve Kapat", command=kaydet_ve_kapat)
    kaydet_butonu.pack()

    pencere.mainloop()

# Kullanım örneği
kagit_tespit_ve_duzelt('a.jpg')
