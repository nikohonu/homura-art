# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'collage_preview.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_CollagePreview(object):
    def setupUi(self, CollagePreview):
        if not CollagePreview.objectName():
            CollagePreview.setObjectName(u"CollagePreview")
        CollagePreview.resize(1298, 762)
        self.verticalLayout = QVBoxLayout(CollagePreview)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.file = QLabel(CollagePreview)
        self.file.setObjectName(u"file")
        self.file.setMinimumSize(QSize(1280, 720))
        self.file.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.file)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 6, -1)
        self.button_box = QDialogButtonBox(CollagePreview)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.button_box)

        self.button_next = QPushButton(CollagePreview)
        self.button_next.setObjectName(u"button_next")

        self.horizontalLayout.addWidget(self.button_next)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CollagePreview)
        self.button_box.rejected.connect(CollagePreview.reject)
        self.button_box.accepted.connect(CollagePreview.accept)

        QMetaObject.connectSlotsByName(CollagePreview)
    # setupUi

    def retranslateUi(self, CollagePreview):
        CollagePreview.setWindowTitle(QCoreApplication.translate("CollagePreview", u"Dialog", None))
        self.file.setText(QCoreApplication.translate("CollagePreview", u"TextLabel", None))
        self.button_next.setText(QCoreApplication.translate("CollagePreview", u"Next (S)", None))
    # retranslateUi

