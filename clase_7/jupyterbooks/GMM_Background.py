# Importamos las librerías
import numpy as np
import cv2 as cv

# Videos de Videezy.com (Licencia Gratuita)

# cap = cv.VideoCapture('data/People_walking_in_airport.mov')
cap = cv.VideoCapture('data/sidewalk.mp4')

cv.namedWindow('MOG2', cv.WINDOW_NORMAL)

fgbg = cv.createBackgroundSubtractorMOG2()

while (1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('MOG2', fgmask)
    k = cv.waitKey(30) & 0xff

    if k == 27:
        break

cap.release()
cv.destroyAllWindows()