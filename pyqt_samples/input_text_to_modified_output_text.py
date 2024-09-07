import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QVBoxLayout
)


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('Qt Signals & Slots')

        # create widgets
        self.label = QLabel()
        self.line_edit = QLineEdit()

        #self.set_special_text1(label, line_edit)
        #line_edit.textChanged.connect(label.setText)

        # this line here is what connects the signal of text changed to slot--set special text
        # without connecting the signal to slot it wouldn't update
        # however note this updates continuously as we write
        # different from setting a button to print when we hit "print"
        self.line_edit.textChanged.connect(self.set_special_text)

        # place the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # show the window
        self.show()
    

    def set_special_text(self):
        text = self.line_edit.text()
        special_text = "you wrote: " + text
        self.label.setText(special_text)

    def set_special_text1(self, lab, le):
        text = le.text()
        special_text = "you wrote: " + text
        lab.setText(special_text)
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())