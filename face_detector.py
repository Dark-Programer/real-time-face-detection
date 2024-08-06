import pathlib
import cv2 as cv

path = str(pathlib.Path(cv.__file__).parent.absolute() /
           "data/haarcascade_frontalface_default.xml")

#  building classifier use to find face in the image or video
classifier = cv.CascadeClassifier(path)

camera = cv.VideoCapture(0)

b, g, r = (255, 255, 0)  # BGR color

print("Turning on Camera...")

while True:
    _, frame = camera.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # detect the face using the classifier
    faces = classifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv.CASCADE_SCALE_IMAGE
    )

    for (x, y, width, height) in faces:
        cv.rectangle(frame, (x, y), (x + width, y + height),
                     color=(b, g, r), thickness=2)

    cv.imshow("Detecting Faces", frame)

    if cv.waitKey(1) == ord("x"):
        break

camera.release()
print("Turning off Camera...")
cv.destroyAllWindows()
