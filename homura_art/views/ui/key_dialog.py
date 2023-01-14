# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_KeyDialog(object):
    def setupUi(self, KeyDialog):
        if not KeyDialog.objectName():
            KeyDialog.setObjectName(u"KeyDialog")
        KeyDialog.resize(422, 90)
        self.gridLayout = QGridLayout(KeyDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacer, 1, 0, 1, 2)

        self.label = QLabel(KeyDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.button_box = QDialogButtonBox(KeyDialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 2)

        self.edit_key = QLineEdit(KeyDialog)
        self.edit_key.setObjectName(u"edit_key")

        self.gridLayout.addWidget(self.edit_key, 0, 1, 1, 1)


        self.retranslateUi(KeyDialog)
        self.button_box.accepted.connect(KeyDialog.accept)
        self.button_box.rejected.connect(KeyDialog.reject)

        QMetaObject.connectSlotsByName(KeyDialog)
    # setupUi

    def retranslateUi(self, KeyDialog):
        KeyDialog.setWindowTitle(QCoreApplication.translate("KeyDialog", u"Hydrus Client API Access Key", None))
        self.label.setText(QCoreApplication.translate("KeyDialog", u"Hydrus Client API Access Key:", None))
    # retranslateUi

