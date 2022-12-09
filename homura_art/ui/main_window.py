# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
        MainWindow.resize(1024, 768)
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_widget.sizePolicy().hasHeightForWidth())
        self.central_widget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.central_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.files_layout = QHBoxLayout()
        self.files_layout.setObjectName(u"files_layout")
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.left_control_buttons_layout = QHBoxLayout()
        self.left_control_buttons_layout.setObjectName(u"left_control_buttons_layout")
        self.delete_left_button = QPushButton(self.central_widget)
        self.delete_left_button.setObjectName(u"delete_left_button")

        self.left_control_buttons_layout.addWidget(self.delete_left_button)

        self.safe_left_button = QPushButton(self.central_widget)
        self.safe_left_button.setObjectName(u"safe_left_button")

        self.left_control_buttons_layout.addWidget(self.safe_left_button)


        self.left_layout.addLayout(self.left_control_buttons_layout)

        self.left_file = QLabel(self.central_widget)
        self.left_file.setObjectName(u"left_file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.left_file.sizePolicy().hasHeightForWidth())
        self.left_file.setSizePolicy(sizePolicy1)
        self.left_file.setMinimumSize(QSize(1, 1))
        self.left_file.setScaledContents(False)

        self.left_layout.addWidget(self.left_file)


        self.files_layout.addLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.right_control_buttons_layout = QHBoxLayout()
        self.right_control_buttons_layout.setObjectName(u"right_control_buttons_layout")
        self.delete_right_button = QPushButton(self.central_widget)
        self.delete_right_button.setObjectName(u"delete_right_button")

        self.right_control_buttons_layout.addWidget(self.delete_right_button)

        self.safe_right_button = QPushButton(self.central_widget)
        self.safe_right_button.setObjectName(u"safe_right_button")

        self.right_control_buttons_layout.addWidget(self.safe_right_button)


        self.right_layout.addLayout(self.right_control_buttons_layout)

        self.right_file = QLabel(self.central_widget)
        self.right_file.setObjectName(u"right_file")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_file.sizePolicy().hasHeightForWidth())
        self.right_file.setSizePolicy(sizePolicy2)
        self.right_file.setMinimumSize(QSize(1, 1))
        self.right_file.setScaledContents(False)

        self.right_layout.addWidget(self.right_file)


        self.files_layout.addLayout(self.right_layout)


        self.verticalLayout.addLayout(self.files_layout)

        self.control_buttons_layout = QHBoxLayout()
        self.control_buttons_layout.setObjectName(u"control_buttons_layout")
        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_buttons_layout.addItem(self.left_spacer)

        self.left_win_button = QPushButton(self.central_widget)
        self.left_win_button.setObjectName(u"left_win_button")

        self.control_buttons_layout.addWidget(self.left_win_button)

        self.tie_button = QPushButton(self.central_widget)
        self.tie_button.setObjectName(u"tie_button")

        self.control_buttons_layout.addWidget(self.tie_button)

        self.skip_button = QPushButton(self.central_widget)
        self.skip_button.setObjectName(u"skip_button")

        self.control_buttons_layout.addWidget(self.skip_button)

        self.right_win_button = QPushButton(self.central_widget)
        self.right_win_button.setObjectName(u"right_win_button")

        self.control_buttons_layout.addWidget(self.right_win_button)

        self.right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_buttons_layout.addItem(self.right_spacer)


        self.verticalLayout.addLayout(self.control_buttons_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.collage_button = QPushButton(self.central_widget)
        self.collage_button.setObjectName(u"collage_button")

        self.horizontalLayout.addWidget(self.collage_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.delete_left_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.safe_left_button.setText(QCoreApplication.translate("MainWindow", u"Safe", None))
        self.left_file.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.delete_right_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.safe_right_button.setText(QCoreApplication.translate("MainWindow", u"Safe", None))
        self.right_file.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.left_win_button.setText(QCoreApplication.translate("MainWindow", u"Left win", None))
        self.tie_button.setText(QCoreApplication.translate("MainWindow", u"Tie", None))
        self.skip_button.setText(QCoreApplication.translate("MainWindow", u"Skip", None))
        self.right_win_button.setText(QCoreApplication.translate("MainWindow", u"Right win", None))
        self.collage_button.setText(QCoreApplication.translate("MainWindow", u"Generate collage", None))
    # retranslateUi

