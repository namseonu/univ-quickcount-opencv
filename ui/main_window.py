from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget
from model import Answer
from opencv import CountingPeople


# Main window of the game
class QuickCount(QMainWindow):
    # initialize the values needed for the game
    def __init__(self):
        super().__init__()

        # initialize the values needed for the game
        self.images = Answer.get_images()
        self.answers = Answer.get_answers()

        self.current_image_index = 0
        self.answers_by_user = []
        self.answers_by_opencv = []

        self.lbl_image = None
        self.lbl_input_by_user = None
        self.lbl_answer_by_opencv = None
        self.lbl_result = None
        self.input_by_user = None
        self.btn_start = None
        self.btn_confirm = None
        self.btn_next = None
        self.btn_close = None
        self.timer = None

        self.init()

    # initialize the UI
    def init(self):
        self.setWindowTitle("Quick Count")

        self.lbl_image = QLabel(self)
        self.lbl_image.hide()

        self.lbl_input_by_user = QLabel(self)
        self.lbl_input_by_user.hide()

        self.lbl_answer_by_opencv = QLabel(self)
        self.lbl_answer_by_opencv.hide()

        self.lbl_result = QLabel(self)
        self.lbl_result.hide()

        self.input_by_user = QLineEdit(self)
        self.input_by_user.hide()

        # Start Button
        self.btn_start = QPushButton("Start", self)
        self.btn_start.clicked.connect(self.start_game)

        # Confirm Button
        self.btn_confirm = QPushButton("Confirm", self)
        self.btn_confirm.clicked.connect(self.confirm_answer)
        self.btn_confirm.hide()

        # Next Button
        self.btn_next = QPushButton("Next", self)
        self.btn_next.clicked.connect(self.show_next_image)
        self.btn_next.hide()

        # Close Button
        self.btn_close = QPushButton("Close", self)
        self.btn_close.clicked.connect(self.close_game)
        self.btn_close.hide()

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_image)
        layout.addWidget(self.lbl_input_by_user)
        layout.addWidget(self.lbl_answer_by_opencv)
        layout.addWidget(self.lbl_result)
        layout.addWidget(self.input_by_user)
        layout.addWidget(self.btn_start)
        layout.addWidget(self.btn_confirm)
        layout.addWidget(self.btn_next)
        layout.addWidget(self.btn_close)

        # Widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.enter_count_by_user)

    # start the game when the start button is clicked
    def start_game(self):
        self.btn_start.hide()
        self.show_next_image_for_short_seconds()

    # show the image of current index
    def show_next_image_for_short_seconds(self):
        self.lbl_answer_by_opencv.hide()
        self.btn_next.hide()

        self.lbl_image.show()

        if self.current_image_index < len(self.images):
            image = self.images[self.current_image_index]
            self.lbl_image.setPixmap(QPixmap(image))

            # after about 1 second, then execute the function enter_count_by_user
            self.timer.start(1500)

    # show the window for user input
    def enter_count_by_user(self):
        self.timer.stop()

        self.lbl_image.hide()

        self.lbl_input_by_user.show()
        self.lbl_input_by_user.setText("Count by User: ")

        self.input_by_user.show()
        self.input_by_user.setText("")
        self.input_by_user.setFocus()

        self.btn_confirm.show()

    # save the answer by user and show the image by OpenCV
    def confirm_answer(self):
        # save the answer by user
        input_count = self.input_by_user.text()
        if input_count == "":
            input_count = 0

        answer_by_user = int(input_count)
        self.answers_by_user.append(answer_by_user)

        # show the image by OpenCV
        self.show_image_by_opencv()

    # show the image by OpenCV
    def show_image_by_opencv(self):
        self.lbl_input_by_user.hide()
        self.input_by_user.hide()
        self.btn_confirm.hide()

        self.lbl_image.show()
        self.lbl_answer_by_opencv.show()
        self.btn_next.show()

        image = self.images[self.current_image_index]
        counting_people = CountingPeople(image)
        answer_by_opencv, image_by_opencv = counting_people.get_image_by_opencv()

        self.answers_by_opencv.append(answer_by_opencv)

        # convert the numpy array to QImage
        height, width, channel = image_by_opencv.shape
        bytes_per_line = 3 * width
        q_image = QImage(image_by_opencv.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.lbl_image.setPixmap(QPixmap(q_image))
        self.lbl_answer_by_opencv.setText("Count by OpenCV: " + str(answer_by_opencv))

        self.current_image_index += 1

    # show the next image
    def show_next_image(self):
        # if the game is not finished, show the next image
        if self.current_image_index < len(self.images):
            self.show_next_image_for_short_seconds()
        # if the game is finished, show the game result
        else:
            self.show_game_result()

    # show the game result (i.e., winner)
    def show_game_result(self):
        self.lbl_image.hide()
        self.lbl_answer_by_opencv.hide()
        self.btn_next.hide()

        self.lbl_result.show()
        self.btn_close.show()

        score_by_user = sum(answer_by_user == answer
                            for answer_by_user, answer in zip(self.answers_by_user, self.answers))
        score_by_opencv = sum(answer_by_opencv == answer
                              for answer_by_opencv, answer in zip(self.answers_by_opencv, self.answers))

        result = "User " + str(score_by_user) + " vs. " + "OpenCV " + str(score_by_opencv)

        if score_by_user > score_by_opencv:
            result += "\nUser wins!"
        elif score_by_user < score_by_opencv:
            result += "\nOpenCV wins!"
        else:
            result += "\nDraw!"

        self.lbl_result.setText(result)

    # close the game window
    def close_game(self):
        self.close()
