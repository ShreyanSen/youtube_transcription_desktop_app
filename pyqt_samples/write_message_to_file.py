import sys
import os
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

        self.setWindowTitle('Write Message To File')

        # make sure we have data dir
        if 'data' not in os.listdir():
            os.mkdir('data')

        # create widgets
        self.top_label = QLabel('Write to text:')
        self.text_line_edit = QLineEdit()
        self.filename_line_edit = QLineEdit()
        self.button = QPushButton('Save File')
        self.close_button = QPushButton('Close')

        self.bottom_label = QLabel()

        # connects signal button clicked to slot--button clicked class
        self.button.clicked.connect(self.button_clicked)
        self.close_button.clicked.connect(self.close)


        # if we wanted to just display continuosly the updated text:
        #line_edit.textChanged.connect(label.setText)

        # if we wanted to display continuously the updated modified text:
        #self.line_edit.textChanged.connect(self.set_special_text)

        # place the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.top_label)
        layout.addWidget(self.text_line_edit)
        layout.addWidget(self.filename_line_edit)
        layout.addWidget(self.bottom_label)
        layout.addWidget(self.button)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        # show the window
        self.show()

    def button_clicked(self):
        write_text = self.text_line_edit.text()
        filename = self.filename_line_edit.text()
        with open('data/' + filename, 'w') as f:
            f.write(write_text)
        self.bottom_label.setText('wrote to data/' + filename)
        return 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())