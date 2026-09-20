from PySide6.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Grabar")
        self.label = QLabel("")

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.label)

        self.button.pressed.connect(self.on_pressed)
        self.button.released.connect(self.on_released)

    def on_pressed(self):
        print("Botón pulsado")
        self.label.setText("Grabando...")

    def on_released(self):
        print("Botón soltado")
        self.label.setText("")
