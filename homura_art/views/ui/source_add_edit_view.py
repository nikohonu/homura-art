# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'source_add_edit_view.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SourceAddEditView(object):
    def setupUi(self, SourceAddEditView):
        if not SourceAddEditView.objectName():
            SourceAddEditView.setObjectName(u"SourceAddEditView")
        SourceAddEditView.resize(300, 150)
        self.gridLayout = QGridLayout(SourceAddEditView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_key = QLabel(SourceAddEditView)
        self.label_key.setObjectName(u"label_key")

        self.gridLayout.addWidget(self.label_key, 2, 0, 1, 1)

        self.label_api = QLabel(SourceAddEditView)
        self.label_api.setObjectName(u"label_api")

        self.gridLayout.addWidget(self.label_api, 1, 0, 1, 1)

        self.label_address = QLabel(SourceAddEditView)
        self.label_address.setObjectName(u"label_address")

        self.gridLayout.addWidget(self.label_address, 0, 0, 1, 1)

        self.combo_box_api = QComboBox(SourceAddEditView)
        self.combo_box_api.setObjectName(u"combo_box_api")

        self.gridLayout.addWidget(self.combo_box_api, 1, 1, 1, 1)

        self.edit_key = QLineEdit(SourceAddEditView)
        self.edit_key.setObjectName(u"edit_key")

        self.gridLayout.addWidget(self.edit_key, 2, 1, 1, 1)

        self.edit_address = QLineEdit(SourceAddEditView)
        self.edit_address.setObjectName(u"edit_address")

        self.gridLayout.addWidget(self.edit_address, 0, 1, 1, 1)

        self.button_box = QDialogButtonBox(SourceAddEditView)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.button_box, 4, 0, 1, 2)

        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacer, 3, 0, 1, 1)


        self.retranslateUi(SourceAddEditView)
        self.button_box.accepted.connect(SourceAddEditView.accept)
        self.button_box.rejected.connect(SourceAddEditView.reject)

        QMetaObject.connectSlotsByName(SourceAddEditView)
    # setupUi

    def retranslateUi(self, SourceAddEditView):
        SourceAddEditView.setWindowTitle(QCoreApplication.translate("SourceAddEditView", u"New source", None))
        self.label_key.setText(QCoreApplication.translate("SourceAddEditView", u"Key:", None))
        self.label_api.setText(QCoreApplication.translate("SourceAddEditView", u"API:", None))
        self.label_address.setText(QCoreApplication.translate("SourceAddEditView", u"Address:", None))
    # retranslateUi

