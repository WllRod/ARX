from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *    


class CRUD_Buttons(QPushButton):
    def __init__(self):
        super().__init__()
        self.add_user_btn = QPushButton()
        self.add_user_btn.setStyleSheet("margin-top: 5%; border-radius: 2px;background: rgb(85, 170, 255)")
        self.add_user_btn.hide()
        self.add_user_btn.setMaximumSize(QSize(105, 50))
        
        self.add_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

            #self.frame_icon_include_btn  = QFrame(self.add_user_btn)
        self.add_user_btn.setIcon(QIcon("assets\\add.png"))
        self.add_user_btn.setIconSize(QSize(25, 50))
        #===================================================================
        self.edit_user_btn = QPushButton()
        self.edit_user_btn.setStyleSheet("margin-top: 5%; border-radius: 2px;background: rgb(85, 170, 255)")
        self.edit_user_btn.hide()
        self.edit_user_btn.setMaximumSize(QSize(105, 50))
        
        self.edit_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

            #self.frame_icon_include_btn  = QFrame(self.edit_user_btn)
        self.edit_user_btn.setIcon(QIcon("assets\\edit.png"))
        self.edit_user_btn.setIconSize(QSize(25, 50))

        #===================================================================
        self.del_user_btn = QPushButton()
        self.del_user_btn.setStyleSheet("margin-top: 5%; border-radius: 2px;background: #D22121")
        self.del_user_btn.hide()
        self.del_user_btn.setMaximumSize(QSize(105, 50))
        
        self.del_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

            #self.frame_icon_include_btn  = QFrame(self.del_user_btn)
        self.del_user_btn.setIcon(QIcon("assets\\delete.png"))
        self.del_user_btn.setIconSize(QSize(25, 50))