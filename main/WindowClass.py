import sys
from PyQt6.QtWidgets import QWidget, QApplication

class Window(QWidget): 
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Subtitle Filmmaker v1.0")
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())