import sys
from PySide6.QtWidgets import QApplication
from view import MainView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainView()
    window.show()
    sys.exit(app.exec())