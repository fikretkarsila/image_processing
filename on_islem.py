import cv2

def boyutlandirma(img_path,x,y): # Görüntü Boyutlandırma
    return cv2.resize(img_path,(x,y))

def goruntu_okuma(img_path): # Görüntü Okuma
    img = cv2.imread(img_path)
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

