import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        # create widgets
        self.label = QLabel()
        self.line_edit = QLineEdit()


        self.button = QPushButton('Click me')
        # connects signal button clicked to slot--button clicked class
        self.button.clicked.connect(self.button_clicked)

        # if we wanted to just display continuosly the updated text:
        #line_edit.textChanged.connect(label.setText)

        # if we wanted to display continuously the updated modified text:
        #self.line_edit.textChanged.connect(self.set_special_text)

        # place the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # show the window
        self.show()

    def button_clicked(self):
        text = self.line_edit.text()
        special_text = "you wrote: " + text
        self.label.setText(special_text)
    
    def set_special_text(self):
        text = self.line_edit.text()
        special_text = "you wrote: " + text
        self.label.setText(special_text)

        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())