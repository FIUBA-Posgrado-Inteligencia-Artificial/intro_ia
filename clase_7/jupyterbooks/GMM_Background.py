# Importamos las librerías
import numpy as np
import cv2 as cv

# Videos de Videezy.com (Licencia Gratuita)

file_path = './data/Escalator.mp4'
cap = cv.VideoCapture(file_path)

cv.namedWindow('MOG2', cv.WINDOW_NORMAL)

fgbg = cv.createBackgroundSubtractorMOG2(history=20, varThreshold=50)
# fgbg = cv.createBackgroundSubtractorMOG2()

while (1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    # cv.imshow('Frame', frame)
    cv.imshow('MOG2', fgmask)
    k = cv.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv.destroyAllWindows()