# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        self.action_delete_left = QAction(MainWindow)
        self.action_delete_left.setObjectName(u"action_delete_left")
        self.action_delete_right = QAction(MainWindow)
        self.action_delete_right.setObjectName(u"action_delete_right")
        self.action_left_win = QAction(MainWindow)
        self.action_left_win.setObjectName(u"action_left_win")
        self.action_right_win = QAction(MainWindow)
        self.action_right_win.setObjectName(u"action_right_win")
        self.action_tie = QAction(MainWindow)
        self.action_tie.setObjectName(u"action_tie")
        self.action_collage = QAction(MainWindow)
        self.action_collage.setObjectName(u"action_collage")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
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
        self.file = QLabel(self.central_widget)
        self.file.setObjectName(u"file")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.file.sizePolicy().hasHeightForWidth())
        self.file.setSizePolicy(sizePolicy1)
        self.file.setAlignment(Qt.AlignCenter)

        self.files_layout.addWidget(self.file)


        self.verticalLayout.addLayout(self.files_layout)

        self.control_buttons_layout = QHBoxLayout()
        self.control_buttons_layout.setObjectName(u"control_buttons_layout")
        self.left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_buttons_layout.addItem(self.left_spacer)

        self.button_delete_left = QPushButton(self.central_widget)
        self.button_delete_left.setObjectName(u"button_delete_left")
        self.button_delete_left.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.button_delete_left)

        self.button_left_win = QPushButton(self.central_widget)
        self.button_left_win.setObjectName(u"button_left_win")
        self.button_left_win.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.button_left_win)

        self.button_tie = QPushButton(self.central_widget)
        self.button_tie.setObjectName(u"button_tie")
        self.button_tie.setMinimumSize(QSize(0, 0))

        self.control_buttons_layout.addWidget(self.button_tie)

        self.button_right_win = QPushButton(self.central_widget)
        self.button_right_win.setObjectName(u"button_right_win")
        self.button_right_win.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.button_right_win)

        self.button_delete_right = QPushButton(self.central_widget)
        self.button_delete_right.setObjectName(u"button_delete_right")
        self.button_delete_right.setMinimumSize(QSize(100, 0))

        self.control_buttons_layout.addWidget(self.button_delete_right)

        self.right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.control_buttons_layout.addItem(self.right_spacer)


        self.verticalLayout.addLayout(self.control_buttons_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_collage = QPushButton(self.central_widget)
        self.button_collage.setObjectName(u"button_collage")
        self.button_collage.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.button_collage)

        self.button_undo = QPushButton(self.central_widget)
        self.button_undo.setObjectName(u"button_undo")
        self.button_undo.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.button_undo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1024, 30))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_delete_left)
        self.menuFile.addAction(self.action_delete_right)
        self.menuFile.addAction(self.action_left_win)
        self.menuFile.addAction(self.action_right_win)
        self.menuFile.addAction(self.action_tie)
        self.menuFile.addAction(self.action_collage)
        self.menuFile.addAction(self.action_undo)

        self.retranslateUi(MainWindow)
        self.button_collage.clicked.connect(self.action_collage.trigger)
        self.button_delete_left.clicked.connect(self.action_delete_left.trigger)
        self.button_delete_right.clicked.connect(self.action_delete_right.trigger)
        self.button_left_win.clicked.connect(self.action_left_win.trigger)
        self.button_right_win.clicked.connect(self.action_right_win.trigger)
        self.button_tie.clicked.connect(self.action_tie.trigger)
        self.button_undo.clicked.connect(self.action_undo.trigger)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_delete_left.setText(QCoreApplication.translate("MainWindow", u"Delete left", None))
#if QT_CONFIG(tooltip)
        self.action_delete_left.setToolTip(QCoreApplication.translate("MainWindow", u"Delete left file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_delete_left.setShortcut(QCoreApplication.translate("MainWindow", u"Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_delete_right.setText(QCoreApplication.translate("MainWindow", u"Delete right", None))
#if QT_CONFIG(tooltip)
        self.action_delete_right.setToolTip(QCoreApplication.translate("MainWindow", u"Delete right file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_delete_right.setShortcut(QCoreApplication.translate("MainWindow", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.action_left_win.setText(QCoreApplication.translate("MainWindow", u"Left win", None))
#if QT_CONFIG(tooltip)
        self.action_left_win.setToolTip(QCoreApplication.translate("MainWindow", u"Left file win", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_left_win.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.action_right_win.setText(QCoreApplication.translate("MainWindow", u"Right win", None))
#if QT_CONFIG(tooltip)
        self.action_right_win.setToolTip(QCoreApplication.translate("MainWindow", u"Right file win", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_right_win.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.action_tie.setText(QCoreApplication.translate("MainWindow", u"Tie", None))
#if QT_CONFIG(tooltip)
        self.action_tie.setToolTip(QCoreApplication.translate("MainWindow", u"A tie between files", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_tie.setShortcut(QCoreApplication.translate("MainWindow", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.action_collage.setText(QCoreApplication.translate("MainWindow", u"Collage", None))
#if QT_CONFIG(tooltip)
        self.action_collage.setToolTip(QCoreApplication.translate("MainWindow", u"Show collage", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_collage.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(tooltip)
        self.action_undo.setToolTip(QCoreApplication.translate("MainWindow", u"Undo last action", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_undo.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.file.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.button_delete_left.setText(QCoreApplication.translate("MainWindow", u"Delete (Q)", None))
        self.button_left_win.setText(QCoreApplication.translate("MainWindow", u"Left win (A)", None))
        self.button_tie.setText(QCoreApplication.translate("MainWindow", u"Tie (W)", None))
        self.button_right_win.setText(QCoreApplication.translate("MainWindow", u"Right win (D)", None))
        self.button_delete_right.setText(QCoreApplication.translate("MainWindow", u"Delete (E)", None))
        self.button_collage.setText(QCoreApplication.translate("MainWindow", u"Collage (S)", None))
        self.button_undo.setText(QCoreApplication.translate("MainWindow", u"Undo (Space)", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

