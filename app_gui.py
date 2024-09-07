import sys
import os
from pathlib import Path
from yt_transcription import yt_transcript
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

        # create widgets

        self.yt_url_line_edit = QLineEdit(placeholderText='https://www.youtube.com/...')
        
   
        dir_btn = QPushButton('Browse')
        dir_btn.clicked.connect(self.open_dir_dialog)
        self.dir_name_edit = QLineEdit()

        self.filename_line_edit = QLineEdit(placeholderText='transcript.txt')
        self.button = QPushButton('Save File')

        self.close_button = QPushButton('Close')


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
        layout.addWidget(QLabel('Youtube Video URL:'), 1, 0)
        layout.addWidget(self.yt_url_line_edit,1,1, 1, 5)

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

        if not self.yt_url_line_edit.text():
            self.bottom_label.setText('Please enter valid youtube url')
        elif not self.filename_line_edit.text():
            self.bottom_label.setText('Please enter output filename')
        else: 
            yt_url = self.yt_url_line_edit.text()
            path = self.dir_name_edit.text()
            filename = self.filename_line_edit.text()
            filepath = os.path.join(path, filename)
            yt_transcript_obj = yt_transcript(yt_url=yt_url)
            yt_transcript_obj.pull_and_write(output_file = filepath)
            self.bottom_label.setText('File Saved!')
            # TODO: currently if no captions are found the program just dies instead of complaining
            # could have it so yt_transcript_obj returns an error if it can't finish and the bottom label
            # displays it
        return 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())