from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

class Frame(object):
    def verticalFrame(self, widget):

        self.Frame   = QFrame(widget)
        self.verticalLayout = QVBoxLayout(widget)

        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.Frame)

        self.frame_1    = QFrame(self.Frame)
        self.frame_2    = QFrame(self.Frame)
        
        self.verticalLayout_2   = QVBoxLayout(self.Frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)

        self.verticalLayout_2.addWidget(self.frame_1)
        self.verticalLayout_2.addWidget(self.frame_2)
    
    def horizontalFrame(self, widget):
        self.horizontal_frame_1 = QFrame(widget)
        self.horizontal_frame_2 = QFrame(widget)

        self.horizontal_layout_1    = QHBoxLayout(widget)
        self.horizontal_layout_1.setSpacing(0)
        self.horizontal_layout_1.setContentsMargins(0, 0, 0, 0)

        self.horizontal_layout_1.addWidget(self.horizontal_frame_1)
        self.horizontal_layout_1.addWidget(self.horizontal_frame_2)
        