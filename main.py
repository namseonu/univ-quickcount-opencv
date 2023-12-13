# Quick Count using Python and OpenCV

import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import QuickCount

if __name__ == "__main__":
    app = QApplication([])
    quickcount = QuickCount()
    quickcount.show()
    app.exec_()
