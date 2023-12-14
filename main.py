# Quick Count using Python and OpenCV

from PyQt5.QtWidgets import QApplication
from ui import QuickCount

if __name__ == "__main__":
    app = QApplication([])
    quickcount = QuickCount()
    quickcount.show()
    app.exec_()
