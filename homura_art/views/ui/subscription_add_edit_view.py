# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subscription_add_edit_view.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_SubscriptionAddEditView(object):
    def setupUi(self, SubscriptionAddEditView):
        if not SubscriptionAddEditView.objectName():
            SubscriptionAddEditView.setObjectName(u"SubscriptionAddEditView")
        SubscriptionAddEditView.resize(300, 117)
        self.gridLayout = QGridLayout(SubscriptionAddEditView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.spacer, 2, 0, 1, 1)

        self.button_box = QDialogButtonBox(SubscriptionAddEditView)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.button_box, 3, 0, 1, 2)

        self.edit_query = QLineEdit(SubscriptionAddEditView)
        self.edit_query.setObjectName(u"edit_query")

        self.gridLayout.addWidget(self.edit_query, 0, 1, 1, 1)

        self.combo_box_source = QComboBox(SubscriptionAddEditView)
        self.combo_box_source.setObjectName(u"combo_box_source")

        self.gridLayout.addWidget(self.combo_box_source, 1, 1, 1, 1)

        self.label_source = QLabel(SubscriptionAddEditView)
        self.label_source.setObjectName(u"label_source")

        self.gridLayout.addWidget(self.label_source, 1, 0, 1, 1)

        self.label_query = QLabel(SubscriptionAddEditView)
        self.label_query.setObjectName(u"label_query")

        self.gridLayout.addWidget(self.label_query, 0, 0, 1, 1)


        self.retranslateUi(SubscriptionAddEditView)
        self.button_box.accepted.connect(SubscriptionAddEditView.accept)
        self.button_box.rejected.connect(SubscriptionAddEditView.reject)

        QMetaObject.connectSlotsByName(SubscriptionAddEditView)
    # setupUi

    def retranslateUi(self, SubscriptionAddEditView):
        SubscriptionAddEditView.setWindowTitle(QCoreApplication.translate("SubscriptionAddEditView", u"New subscription", None))
        self.label_source.setText(QCoreApplication.translate("SubscriptionAddEditView", u"Source:", None))
        self.label_query.setText(QCoreApplication.translate("SubscriptionAddEditView", u"Query:", None))
    # retranslateUi

