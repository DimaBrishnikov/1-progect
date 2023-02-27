import cv2
from PIL import Image

image_path = 'cat.jpeg'
image = cv2.imread(image_path)
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cat_face = cat_face_cascade.detectMultiScale(image)

cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
print(cat_face)
for (x, y, w, h) in cat_face:
    #cv2.rectangle(image, (x, y), (x+w, y+h), (0,0,255))
    glasses = glasses.resize((w, int(h/2)))
    cat.paste(glasses,(x, int(y + h/4)-int(0.5*h)), glasses)
    cat.save("newCat.png")
    cat_with_glasses = cv2.imread("newCat.png")
    cv2.imshow("Cat", cat_with_glasses)
    cv2.waitKey()

