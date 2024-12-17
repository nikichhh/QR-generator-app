from PyQt5.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QPushButton, QFileDialog,
    QMessageBox, QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from logic import generate_qr_code, print_image
from styles import STYLESHEET


class QRCodeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("logo.ico"))
        self.qr_file_path = None
        self.initUI()
        self.load_stylesheet()

    def initUI(self):
        self.setWindowTitle("QR Code Generator")
        self.setFixedSize(400, 500)

        # Main layout
        main_layout = QVBoxLayout()

        # Title
        self.title_label = QLabel("QR Code Generator")
        self.title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.title_label)

        # Input field
        input_layout = QHBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter data to generate QR code")
        input_layout.addWidget(self.input_field)

        self.generate_button = QPushButton("Create QR Code")
        self.generate_button.clicked.connect(self.generate_qr)
        input_layout.addWidget(self.generate_button)

        main_layout.addLayout(input_layout)

        # QR code display
        self.qr_label = QLabel()
        self.qr_label.setAlignment(Qt.AlignCenter)
        self.qr_label.setFixedSize(200, 200)
        main_layout.addWidget(self.qr_label, alignment=Qt.AlignCenter)

        # Print button
        self.print_button = QPushButton("Print")
        self.print_button.setDisabled(True)
        self.print_button.clicked.connect(self.handle_print)
        main_layout.addWidget(self.print_button, alignment=Qt.AlignCenter)

        # Set main widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def generate_qr(self):
        data = self.input_field.text().strip()
        if not data:
            QMessageBox.warning(self, "Error", "Please enter valid data to generate a QR code!")
            return

        save_path = QFileDialog.getSaveFileName(
            self, "Save QR Code", "", "PNG files (*.png);;All Files (*)"
        )[0]

        if not save_path:
            return

        try:
            generate_qr_code(data, save_path)
            self.qr_file_path = save_path

            # Display the QR code
            pixmap = QPixmap(save_path)
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)
            self.qr_label.setPixmap(pixmap)

            # Enable the Print button
            self.print_button.setDisabled(False)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def handle_print(self):
        if self.qr_file_path:
            try:
                print_image(self.qr_file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to print the file: {e}")
        else:
            QMessageBox.warning(self, "Error", "No QR code to print. Please create one first.")

    def load_stylesheet(self):
        self.setStyleSheet(STYLESHEET)
