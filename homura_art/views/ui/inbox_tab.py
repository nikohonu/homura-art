# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inbox_tab.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QListView, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_InboxTab(object):
    def setupUi(self, InboxTab):
        if not InboxTab.objectName():
            InboxTab.setObjectName(u"InboxTab")
        InboxTab.resize(731, 583)
        self.action_filter = QAction(InboxTab)
        self.action_filter.setObjectName(u"action_filter")
        self.gridLayout = QGridLayout(InboxTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_filter = QPushButton(InboxTab)
        self.button_filter.setObjectName(u"button_filter")

        self.gridLayout.addWidget(self.button_filter, 1, 1, 1, 1)

        self.spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacer, 1, 0, 1, 1)

        self.view = QListView(InboxTab)
        self.view.setObjectName(u"view")
        self.view.setResizeMode(QListView.Adjust)
        self.view.setViewMode(QListView.IconMode)
        self.view.setUniformItemSizes(False)
        self.view.setWordWrap(False)
        self.view.setItemAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.view, 0, 0, 1, 2)


        self.retranslateUi(InboxTab)
        self.button_filter.clicked.connect(self.action_filter.trigger)

        QMetaObject.connectSlotsByName(InboxTab)
    # setupUi

    def retranslateUi(self, InboxTab):
        InboxTab.setWindowTitle(QCoreApplication.translate("InboxTab", u"Form", None))
        self.action_filter.setText(QCoreApplication.translate("InboxTab", u"filter", None))
#if QT_CONFIG(shortcut)
        self.action_filter.setShortcut(QCoreApplication.translate("InboxTab", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.button_filter.setText(QCoreApplication.translate("InboxTab", u"Filter", None))
    # retranslateUi

