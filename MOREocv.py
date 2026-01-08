import cv2

image = cv2.imread("pikachu.png", 1)
if image is None:
    print("Image not loaded")
R, G, B = cv2.split(image)

cv2.imshow("Original!", image)
cv2.waitKey(0)

cv2.imshow("Blue saturation!", B)
cv2.waitKey(0)

cv2.imshow("Goblin saturation!", G)
cv2.waitKey(0)

cv2.imshow("Red saturation!", R)
cv2.waitKey(0)

cv2.destroyAllWindows()