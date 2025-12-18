#Read an image then display it to the user
'''import cv2
img = cv2.imread("pikachu.png", cv2.IMREAD_COLOR)
cv2.imshow("Pikachu Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
#Read the image then display the image in greyscale
'''import cv2
img = cv2.imread("pikachu.png", 0)
cv2.imshow("Pikachu in greyscale", img)
cv2.waitKey(0)
cv2.destroyAllWindows'''

import cv2
import os

saved_directory = "C:\\Users\\s_ort\\OneDrive\\Desktop"
img = cv2.imread("pikachu.png", 0)
cv2.imshow("Pikachu in Black and White", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
os.chdir(saved_directory)
cv2.imwrite("pikaBlackWhite.png", img)
print("Successfully Saved")