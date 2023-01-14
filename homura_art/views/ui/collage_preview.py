# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collage_preview.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CollageDialog(object):
    def setupUi(self, CollageDialog):
        if not CollageDialog.objectName():
            CollageDialog.setObjectName(u"CollageDialog")
        CollageDialog.resize(1280, 768)
        self.action_next = QAction(CollageDialog)
        self.action_next.setObjectName(u"action_next")
        self.verticalLayout = QVBoxLayout(CollageDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.file = QLabel(CollageDialog)
        self.file.setObjectName(u"file")
        self.file.setMinimumSize(QSize(1280, 720))
        self.file.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.file)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.button_box = QDialogButtonBox(CollageDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.button_box)

        self.button_next = QPushButton(CollageDialog)
        self.button_next.setObjectName(u"button_next")

        self.horizontalLayout.addWidget(self.button_next)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CollageDialog)
        self.button_box.rejected.connect(CollageDialog.reject)
        self.button_box.accepted.connect(CollageDialog.accept)
        self.button_next.clicked.connect(self.action_next.trigger)

        QMetaObject.connectSlotsByName(CollageDialog)
    # setupUi

    def retranslateUi(self, CollageDialog):
        CollageDialog.setWindowTitle(QCoreApplication.translate("CollageDialog", u"Dialog", None))
        self.action_next.setText(QCoreApplication.translate("CollageDialog", u"Next", None))
#if QT_CONFIG(tooltip)
        self.action_next.setToolTip(QCoreApplication.translate("CollageDialog", u"Next collage", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.action_next.setShortcut(QCoreApplication.translate("CollageDialog", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.file.setText(QCoreApplication.translate("CollageDialog", u"TextLabel", None))
        self.button_next.setText(QCoreApplication.translate("CollageDialog", u"Next (S)", None))
    # retranslateUi

