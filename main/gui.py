
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QDialog

app = QApplication(sys.argv)

window = QWidget()

window.show()

sys.exit(app.exec())