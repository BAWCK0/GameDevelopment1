'''import cv2
import numpy as np

image1 = cv2.imread("pikachu.png", 1)
image2 = cv2.imread("bee.png", 1)

image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

#Addition
weightedSum = cv2.addWeighted(image1, 0.7, image2, 0.5, 10)
cv2.imshow("Weighted Image", weightedSum)

sub = cv2.subtract(image2, image1)
cv2.imshow("Subtracted Image", sub)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import cv2
img = cv2.imread("pikachu.png", 1)

resized = cv2.resize(img, (1200, 300))
cv2.imshow("Resized image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''#Image Erosion
import cv2
import numpy as np
img = cv2.imread("pikachu.png", 1)

kernel = np.ones((6, 6), np.uint8)
image = cv2.erode(img, kernel)

cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''#Image bordering (CONSTANT)
import cv2
import numpy as np

img = cv2.imread("pikachu.png")

borderImage = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(255, 128, 64))
cv2.imshow("Border Image", borderImage)

cv2.waitKey(0)
cv2.destroyAllWindows()'''

#Image bordering (REFLECT)
import cv2
import numpy as np

img = cv2.imread("pikachu.png")

borderImage = cv2.copyMakeBorder(img, 100, 100, 100, 100, cv2.BORDER_REFLECT)
cv2.imshow("Border Image", borderImage)

cv2.waitKey(0)
cv2.destroyAllWindows()