from pixelize import pixelize
import cv2

img = pixelize('1.jpg')
cv2.imshow('Image', img)

# Wait for a key event and close the window when a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
