import cv2
import numpy as np

image = cv2.imread('input/tv.jpg')

print(image.shape)  #تعدا سطر وستون عکس

writer = cv2.VideoWriter('output/tv_noice.mp4', cv2.VideoWriter_fourcc(*'XVID'), 40 ,(560, 400))
while True:
    image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    row = 230
    col = 310
    noice = np.random.random((row, col)) * 255
    noice = np.array(noice, dtype=np.uint8)

    image[85:85+row, 80:80+col] = noice
    image=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
    writer.write(image)
    cv2.imshow("TV Noice", image)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break
writer.release()


