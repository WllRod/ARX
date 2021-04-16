import sys
from PyQt5.QtWidgets import (QWidget,
                         QPushButton, QApplication, QGridLayout, QLabel)
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtGui import QMovie
import os

assets  = os.getcwd()+"\\assets"
class Worker(QObject):

    finished = pyqtSignal()  # give worker class a finished signal

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True  # provide a bool run condition for the class

    def do_work(self):
        i = 1
        while self.continue_run:  # give the loop a stoppable condition
            QThread.sleep(1)
            i = i + 1
            if(i > 5):
                break
        self.finished.emit()  # emit the finished signal when the loop is done

    def stop(self):
        self.continue_run = False  # set the run condition to false on stop


class Gui(QWidget):

    stop_signal = pyqtSignal()  # make a stop signal to communicate with the worker in another thread

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        # Buttons:
        '''self.btn_start = QPushButton('Start')
        self.btn_start.resize(self.btn_start.sizeHint())
        self.btn_start.move(50, 50)
        self.btn_stop = QPushButton('Stop')
        self.btn_stop.resize(self.btn_stop.sizeHint())
        self.btn_stop.move(150, 50)'''
        self.label_test = QLabel(self)
        self.movie      = QMovie(assets+"\\loading.gif")
        self.label_test.setMovie(self.movie)
        self.movie.start()

        # GUI title, size, etc...
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('ThreadTest')
        self.layout = QGridLayout()
        self.layout.addWidget(self.label_test)
        
        self.setLayout(self.layout)

        # Thread:
        self.thread = QThread()
        self.worker = Worker()
        self.stop_signal.connect(self.worker.stop)  # connect stop signal to worker stop method
        self.worker.moveToThread(self.thread)

        self.worker.finished.connect(self.thread.quit)  # connect the workers finished signal to stop thread
        self.worker.finished.connect(self.worker.deleteLater)  # connect the workers finished signal to clean up worker
        self.thread.finished.connect(self.thread.deleteLater)  # connect threads finished signal to clean up thread
        self.thread.finished.connect(self.close)

        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.worker.stop)

        # Start Button action:
        #self.btn_start.clicked.connect(self.thread.start)
        self.thread.start()
        # Stop Button action:
        #self.btn_stop.clicked.connect(self.stop_thread)

        self.showMaximized()

    # When stop_btn is clicked this runs. Terminates the worker and the thread.
    def stop_thread(self):
        
        self.stop_signal.emit()  # emit the finished signal on stop

def main_loading():

    app = QApplication(sys.argv)
    gui = Gui()
    app.exec_()

    
