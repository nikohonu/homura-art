# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 717)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 6)
        self.files_layout = QHBoxLayout()
        self.files_layout.setSpacing(0)
        self.files_layout.setObjectName(u"files_layout")
        self.left_file = QLabel(self.central_widget)
        self.left_file.setObjectName(u"left_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_file.sizePolicy().hasHeightForWidth())
        self.left_file.setSizePolicy(sizePolicy1)

        self.files_layout.addWidget(self.left_file)

        self.right_file = QLabel(self.central_widget)
        self.right_file.setObjectName(u"right_file")
        sizePolicy1.setHeightForWidth(self.right_file.sizePolicy().hasHeightForWidth())
        self.right_file.setSizePolicy(sizePolicy1)

        self.files_layout.addWidget(self.right_file)


        self.verticalLayout.addLayout(self.files_layout)

        self.control_buttons_layout = QHBoxLayout()
        self.control_buttons_layout.setObjectName(u"control_buttons_layout")
        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_buttons_layout.addItem(self.left_spacer)

        self.delete_left_button = QPushButton(self.central_widget)
        self.delete_left_button.setObjectName(u"delete_left_button")
        self.delete_left_button.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.delete_left_button)

        self.left_win_button = QPushButton(self.central_widget)
        self.left_win_button.setObjectName(u"left_win_button")
        self.left_win_button.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.left_win_button)

        self.tie_button = QPushButton(self.central_widget)
        self.tie_button.setObjectName(u"tie_button")
        self.tie_button.setMinimumSize(QSize(0, 0))

        self.control_buttons_layout.addWidget(self.tie_button)

        self.right_win_button = QPushButton(self.central_widget)
        self.right_win_button.setObjectName(u"right_win_button")
        self.right_win_button.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.right_win_button)

        self.delete_right_button = QPushButton(self.central_widget)
        self.delete_right_button.setObjectName(u"delete_right_button")
        self.delete_right_button.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.delete_right_button)

        self.right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_buttons_layout.addItem(self.right_spacer)


        self.verticalLayout.addLayout(self.control_buttons_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.collage_button = QPushButton(self.central_widget)
        self.collage_button.setObjectName(u"collage_button")
        self.collage_button.setMinimumSize(QSize(125, 0))

        self.horizontalLayout.addWidget(self.collage_button)

        self.pushButton = QPushButton(self.central_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(125, 0))

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_file.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.right_file.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.delete_left_button.setText(QCoreApplication.translate("MainWindow", u"Delete (Q)", None))
        self.left_win_button.setText(QCoreApplication.translate("MainWindow", u"Left win (A)", None))
        self.tie_button.setText(QCoreApplication.translate("MainWindow", u"Tie (W)", None))
        self.right_win_button.setText(QCoreApplication.translate("MainWindow", u"Right win (D)", None))
        self.delete_right_button.setText(QCoreApplication.translate("MainWindow", u"Delete (E)", None))
        self.collage_button.setText(QCoreApplication.translate("MainWindow", u"Collage (Enter)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Undo (Space)", None))
    # retranslateUi

