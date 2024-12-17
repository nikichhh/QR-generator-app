import sys
from PyQt5.QtWidgets import QApplication
from ui import QRCodeGenerator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRCodeGenerator()
    window.show()
    sys.exit(app.exec_())
