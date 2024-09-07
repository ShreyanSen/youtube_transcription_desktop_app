import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QFileDialog
)
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Write Message To File')
        self.setGeometry(100, 100, 600, 100)
        # make sure we have data dir
        if 'data' not in os.listdir():
            os.mkdir('data')

        # create widgets
        self.text_line_edit = QLineEdit()

        dir_btn = QPushButton('Browse')
        dir_btn.clicked.connect(self.open_dir_dialog)
        self.dir_name_edit = QLineEdit()

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
        layout = QGridLayout()
        layout.addWidget(QLabel('Text to save:'), 1, 0)
        layout.addWidget(self.text_line_edit,1,1, 1, 5)

        layout.addWidget(QLabel('Directory:'), 2, 0)
        layout.addWidget(self.dir_name_edit,2,1,1,5)
        layout.addWidget(dir_btn, 2,6)

        layout.addWidget(QLabel('Choose Filename:'), 3, 0)
        layout.addWidget(self.filename_line_edit,3,1,1,5)
        layout.addWidget(self.button,3,6)
        
        layout.addWidget(self.bottom_label,4,0)
        layout.addWidget(self.close_button, 4,6)
        self.setLayout(layout)

        # show the window
        self.show()
    
    def open_dir_dialog(self):
        dir_name = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if dir_name:
            path = Path(dir_name)
            self.dir_name_edit.setText(str(path))

    def button_clicked(self):
        write_text = self.text_line_edit.text()
        path = self.dir_name_edit.text()
        filename = self.filename_line_edit.text()
        filepath = os.path.join(path, filename)
        with open(filepath, 'w') as f:
            f.write(write_text)
        self.bottom_label.setText('wrote to ' + filename)
        return 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())