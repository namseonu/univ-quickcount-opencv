import cv2


class CountingPeople:
    def __init__(self, image):
        self.image = image
        self.processed_image = None
        self.detected_people_count = 0
        self.detected_people_locations = []

    # read the image and detect people
    def get_image_by_opencv(self):
        # read the image
        image = cv2.imread(self.image)

        # detect people in the image
        self.detect_people(image)

        # draw the bounding box of detected people
        self.processed_image = self.draw_bounding_box(image)

        return self.detected_people_count, self.processed_image

    # detect people in the image
    def detect_people(self, image):
        # convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # detect objects in the image
        # reference: https://github.com/opencv/opencv
        face_cascade = cv2.CascadeClassifier("./opencv/haarcascade_fullbody.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # save the number of detected people
        self.detected_people_count = len(faces)

        # save the bounding box of detected people
        self.detected_people_locations = faces

    # draw the bounding box of detected people
    def draw_bounding_box(self, image):
        # copy the image
        processed_image = image.copy()

        # draw the bounding box of detected people
        for (x, y, w, h) in self.detected_people_locations:
            cv2.rectangle(processed_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return processed_image
