# Youtube Transcription Desktop App

This app is centered around a small python script that fetches English-language transcriptions for user-provided youtube urls. The core process is wrapped in a GUI and packaged as an executable (on MacOS Sonoma or later) so you do not need python to run it. 

I built this app because I wanted to make a desktop GUI around a python app, and distribute it as an executable file. I love command line but not everyone can use it. Today we seem to distribute code by hosting it on web servers and bringing the user to us, but that requires a lot of centralization. I miss the old CD days where you'd download an application and run your code locally. 

## Core Python Script

The core python script is located in yt_transcription.py (and an actual older script version of the same thing is in the script folder). Here we define a class that accepts a url, pulls the transcript, and writes it to a text file. 

## GUI with PyQT

The GUI is built with PyQT. The app lives at app_gui.py. You can run the GUI standalone by running `python app_gui.py` in the root directory. In order to make the app I learned some pyqt basics by making a few dummy apps, and also included those in the pyqt_samples directory. 

The GUI itself is fairly straight-forward. You paste the url in one dialog box, you specify a directory where you want to download output to, you give your output file a name, and it'll write a text file under that name to that directory containing the transcript of the video you passed.

## Executable with PyInstaller

The pyinstaller-made executable file is located at /pyinstaller_executable_app/dist/app_gui/app_gui. Run by double clicking! However, you have to download the whole dist/app_gui directory to run it. 

