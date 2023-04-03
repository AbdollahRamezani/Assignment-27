import cv2

image = cv2.imread('input/batman.jpg')
image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
_, image = cv2.threshold(image, 140, 255, cv2.THRESH_BINARY_INV)
cv2.putText(image, "BATMAN",(400, 480), cv2.FONT_HERSHEY_PLAIN, 3, 255)

cv2.imshow("",image)
cv2.waitKey()

cv2.imwrite('output/batman.jpg',image)