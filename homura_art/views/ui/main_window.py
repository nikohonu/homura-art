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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTabWidget,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.action_quit = QAction(MainWindow)
        self.action_quit.setObjectName(u"action_quit")
        self.action_manage_subscriptions = QAction(MainWindow)
        self.action_manage_subscriptions.setObjectName(u"action_manage_subscriptions")
        self.action_manage_sources = QAction(MainWindow)
        self.action_manage_sources.setObjectName(u"action_manage_sources")
        self.action_options = QAction(MainWindow)
        self.action_options.setObjectName(u"action_options")
        self.action_import = QAction(MainWindow)
        self.action_import.setObjectName(u"action_import")
        self.action_sync = QAction(MainWindow)
        self.action_sync.setObjectName(u"action_sync")
        self.central_widget = QWidget(MainWindow)
        self.central_widget.setObjectName(u"central_widget")
        self.gridLayout = QGridLayout(self.central_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tab_widget = QTabWidget(self.central_widget)
        self.tab_widget.setObjectName(u"tab_widget")

        self.gridLayout.addWidget(self.tab_widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QMenuBar(MainWindow)
        self.menu_bar.setObjectName(u"menu_bar")
        self.menu_bar.setGeometry(QRect(0, 0, 800, 24))
        self.menu_subscriptions = QMenu(self.menu_bar)
        self.menu_subscriptions.setObjectName(u"menu_subscriptions")
        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menu_bar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_subscriptions.menuAction())
        self.menu_subscriptions.addAction(self.action_manage_sources)
        self.menu_subscriptions.addAction(self.action_manage_subscriptions)
        self.menu_subscriptions.addAction(self.action_sync)
        self.menu_file.addAction(self.action_import)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_options)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)

        self.retranslateUi(MainWindow)
        self.action_quit.triggered["bool"].connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Homura Art", None))
        self.action_quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.action_quit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.action_manage_subscriptions.setText(QCoreApplication.translate("MainWindow", u"Manage subscriptions", None))
        self.action_manage_sources.setText(QCoreApplication.translate("MainWindow", u"Manage sources", None))
        self.action_options.setText(QCoreApplication.translate("MainWindow", u"Options", None))
        self.action_import.setText(QCoreApplication.translate("MainWindow", u"Import files", None))
        self.action_sync.setText(QCoreApplication.translate("MainWindow", u"Sync", None))
        self.menu_subscriptions.setTitle(QCoreApplication.translate("MainWindow", u"Network", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

