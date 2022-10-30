# Importar a biblioteca openCV.
import cv2

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
#    print('Deu certo')
    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("janela", frame)
        key = cv2.waitKey(5)
        if key == 27: #ESC
            break