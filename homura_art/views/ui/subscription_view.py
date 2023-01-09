# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subscription_view.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
    QGridLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QWidget)

class Ui_SubscriptionView(object):
    def setupUi(self, SubscriptionView):
        if not SubscriptionView.objectName():
            SubscriptionView.setObjectName(u"SubscriptionView")
        SubscriptionView.resize(710, 506)
        self.action_add = QAction(SubscriptionView)
        self.action_add.setObjectName(u"action_add")
        self.action_edit = QAction(SubscriptionView)
        self.action_edit.setObjectName(u"action_edit")
        self.action_delete = QAction(SubscriptionView)
        self.action_delete.setObjectName(u"action_delete")
        self.gridLayout = QGridLayout(SubscriptionView)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_edit = QPushButton(SubscriptionView)
        self.button_edit.setObjectName(u"button_edit")

        self.gridLayout.addWidget(self.button_edit, 3, 2, 1, 1)

        self.button_add = QPushButton(SubscriptionView)
        self.button_add.setObjectName(u"button_add")

        self.gridLayout.addWidget(self.button_add, 3, 1, 1, 1)

        self.spacer = QSpacerItem(431, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.spacer, 3, 0, 1, 1)

        self.button_delete = QPushButton(SubscriptionView)
        self.button_delete.setObjectName(u"button_delete")

        self.gridLayout.addWidget(self.button_delete, 3, 3, 1, 1)

        self.view = QTableView(SubscriptionView)
        self.view.setObjectName(u"view")

        self.gridLayout.addWidget(self.view, 0, 0, 1, 5)

        self.button_box = QDialogButtonBox(SubscriptionView)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.button_box.setCenterButtons(False)

        self.gridLayout.addWidget(self.button_box, 4, 0, 1, 4)


        self.retranslateUi(SubscriptionView)
        self.button_box.accepted.connect(SubscriptionView.accept)
        self.button_box.rejected.connect(SubscriptionView.reject)
        self.button_add.clicked.connect(self.action_add.trigger)
        self.button_delete.clicked.connect(self.action_delete.trigger)
        self.button_edit.clicked.connect(self.action_edit.trigger)

        QMetaObject.connectSlotsByName(SubscriptionView)
    # setupUi

    def retranslateUi(self, SubscriptionView):
        SubscriptionView.setWindowTitle(QCoreApplication.translate("SubscriptionView", u"Subscriptions", None))
        self.action_add.setText(QCoreApplication.translate("SubscriptionView", u"add", None))
#if QT_CONFIG(shortcut)
        self.action_add.setShortcut(QCoreApplication.translate("SubscriptionView", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.action_edit.setText(QCoreApplication.translate("SubscriptionView", u"edit", None))
#if QT_CONFIG(shortcut)
        self.action_edit.setShortcut(QCoreApplication.translate("SubscriptionView", u"E", None))
#endif // QT_CONFIG(shortcut)
        self.action_delete.setText(QCoreApplication.translate("SubscriptionView", u"delete", None))
#if QT_CONFIG(shortcut)
        self.action_delete.setShortcut(QCoreApplication.translate("SubscriptionView", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.button_edit.setText(QCoreApplication.translate("SubscriptionView", u"Edit (E)", None))
        self.button_add.setText(QCoreApplication.translate("SubscriptionView", u"Add (A)", None))
        self.button_delete.setText(QCoreApplication.translate("SubscriptionView", u"Delete (D)", None))
    # retranslateUi

