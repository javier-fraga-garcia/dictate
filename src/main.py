import sys
from PySide6.QtWidgets import QApplication

from window import Window

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        w = Window()
        w.show()
        sys.exit(app.exec())

    except KeyboardInterrupt:
        print("\nSaliendo del programa")
