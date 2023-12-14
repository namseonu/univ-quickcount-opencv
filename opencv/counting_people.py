import sys
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
        yolo_model = './opencv/yolov3.weights'
        yolo_config = './opencv/yolov3.cfg'

        # create network object
        net = cv2.dnn.readNet(yolo_model, yolo_config)
        if net.empty():
            print('Net open failed!')
            sys.exit()

        # get output layer names
        layer_names = net.getUnconnectedOutLayersNames()

        # prepare the image for YOLOv3 (scalefactor, size, mean, swapRB, crop)
        blob = cv2.dnn.blobFromImage(image,
                                     scalefactor=0.003,
                                     size=(416, 416),
                                     mean=(0, 0, 0),
                                     swapRB=True,
                                     crop=True)
        net.setInput(blob)
        outs = net.forward(layer_names)

        # get information about detected objects
        class_ids = []
        confidences = []
        boxes = []

        img_height = image.shape[0]
        img_width = image.shape[1]

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.4 and class_id == 0:  # class_id 0 corresponds to 'person'
                    center_x = int(detection[0] * img_width)
                    center_y = int(detection[1] * img_height)
                    w = int(detection[2] * img_width)
                    h = int(detection[3] * img_height)

                    # extract bounding box coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        # non-maximum suppression to remove overlapping bounding boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=0.5, nms_threshold=0.4)

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
