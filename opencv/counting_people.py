import cv2
import numpy as np


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
        # load YOLOv3 model
        # reference: https://github.com/pjreddie/darknet
        net = cv2.dnn.readNet('./opencv/yolov3.weights', './opencv/yolov3.cfg')
        layer_names = net.getUnconnectedOutLayersNames()

        # prepare the image for YOLOv3 (scalefactor, size, mean, swapRB, crop)
        blob = cv2.dnn.blobFromImage(image,
                                     scalefactor=0.003,  # original: 0.00392
                                     size=(350, 350),
                                     mean=(0, 0, 0),
                                     swapRB=False,
                                     crop=True)
        net.setInput(blob)

        # get output layer information
        outs = net.forward(layer_names)

        # get information about detected objects
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5 and class_id == 0:  # class_id 0 corresponds to 'person'
                    center_x, center_y, w, h = map(int, detection[0:4] * np.array([image.shape[1],
                                                                                   image.shape[0],
                                                                                   image.shape[1],
                                                                                   image.shape[0]]))

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        # non-maximum suppression to remove overlapping bounding boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.2, nms_threshold=0.4)

        # save the number of detected people
        self.detected_people_count = len(indices)

        # save the bounding box of detected people
        self.detected_people_locations = [boxes[i] for i in indices]

    # draw the bounding box of detected people
    def draw_bounding_box(self, image):
        # copy the image
        copied_image = image.copy()

        # draw the bounding box of detected people
        for (x, y, w, h) in self.detected_people_locations:
            cv2.rectangle(copied_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return copied_image
