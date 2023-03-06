import cv2
import numpy as np

img = cv2.imread('do1.jpg')

kernel_size = (3, 3)

kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

filtered_img = cv2.filter2D(img, -1, kernel)

combined_img = np.hstack([img, filtered_img])
cv2.imshow('Original vs Filtered', combined_img)
cv2.waitKey(0)
cv2.destroyAllWindows()