from rembg import remove
from PIL import Image
from PIL import Image, ImageDraw

import cv2
import numpy as np
import os

def remove_bg(image):
    try:
        input = Image.open(image) 
        
        output = remove(input) 
        
        output.save(image.rpartition('.')[0] + '_bg.png') 
    except:
        pass
    
    """
    Ben calistirdigim arka plan kaldiriliyor. Ek olarak senden istedigim arkaplanin 
    kaldirilmis resmin acilmasi ve benim mouse ile ona müdahale edebilmem. 
    Bunun icin söyle fonksiyonlar istiyorum. Acilmis resme scroll ile yaklasip 
    uzaklasabilmek. Sol tik ile tikladigim yerlerin direkt olarak ayni arka 
    planda oldugu gibi silinmesi ve sag tik ile bastigim yerlerde orjinal 
    resmi geri getirmek. Ayrica mousenin sol tiki ve sag tiki ile yaptigim 
    tüm islemler ben tiklardan parmagimi kaldirdigimda kaydedilsin. Böylece 
    ctrl+z yaptigimda islemi geri alabileyim
    """

def find_max_differences(points):
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    
    # En büyük x ve y farklarını bulma
    max_x_difference = max_x - min_x
    max_y_difference = max_y - min_y
    
    return max_x_difference, max_y_difference

def image_to_doc(pic):
    file_name, extension = os.path.splitext(pic)

    image = cv2.imread(pic)
    corners = []

    def mouse_pos(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Left Click: x={x}, y={y}")
            corners.append([x, y])
    
    cv2.namedWindow("Select Corner")
    cv2.setMouseCallback("Select Corner", mouse_pos)

    while True:
        cv2.imshow("Select Corner", image)

        if len(corners) == 4:
            break
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    width, height = find_max_differences(corners)

    pts1 = np.float32(corners)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    im = cv2.warpPerspective(image, matrix, (width, height))
    cv2.imwrite(file_name + '_' + extension, im)

def crop_image(pic):
    file_name, extension = os.path.splitext(pic)

    image = cv2.imread(pic)
    corners = []

    def mouse_pos(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Left Click: x={x}, y={y}")
            corners.append([x, y])
    
    cv2.namedWindow("Select Corner")
    cv2.setMouseCallback("Select Corner", mouse_pos)

    while True:
        cv2.imshow("Select Corner", image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    im = image[corners[0][1]:corners[1][1], corners[0][0]:corners[1][0]]
    cv2.imwrite(file_name + '_cropped' + extension, im)

def compress_image(pic, quality=50):
    file_name, extension = os.path.splitext(pic)

    image = cv2.imread(pic)

    cv2.imwrite(file_name + '_compressed' + extension, image, [cv2.IMWRITE_JPEG_QUALITY, quality])
