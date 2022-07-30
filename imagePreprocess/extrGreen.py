import cv2

img = cv2.imread("C:/Users/young/Desktop/Image_01L.jpg", 1)
print(img.shape)
print(img.size)
print(img.dtype)

# b, g, r = cv2.split(img)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)
# img = cv2.merge((b, g, r))
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyWindow()



