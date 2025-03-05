# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
from VortexStation import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1914, 1136)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"\n"
"QLabel{\n"
"	\n"
"	color: rgb(248, 248, 242);\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 5px; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"	background-color: #FFB86C; /* Hover background color (darker green) */ 	\n"
"	border-color: #FFB86C; /* Hover border color */ \n"
"} \n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMinimumSize(QSize(0, 50))
        self.headerFrame.setMaximumSize(QSize(16777215, 50))
        self.headerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.headerFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.navigationButtonFrame = QFrame(self.headerFrame)
        self.navigationButtonFrame.setObjectName(u"navigationButtonFrame")
        self.navigationButtonFrame.setMinimumSize(QSize(100, 0))
        self.navigationButtonFrame.setMaximumSize(QSize(100, 16777215))
        self.navigationButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.navigationButtonFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.navigationButton = QPushButton(self.navigationButtonFrame)
        self.navigationButton.setObjectName(u"navigationButton")
        self.navigationButton.setMinimumSize(QSize(0, 50))
        self.navigationButton.setMaximumSize(QSize(16777215, 50))
        icon = QIcon()
        icon.addFile(u":/headerLeftButton/feather/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.navigationButton.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.navigationButton)


        self.horizontalLayout_3.addWidget(self.navigationButtonFrame)

        self.headerTitleFrame = QFrame(self.headerFrame)
        self.headerTitleFrame.setObjectName(u"headerTitleFrame")
        self.headerTitleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerTitleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.headerTitleFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tittleLabel = QLabel(self.headerTitleFrame)
        self.tittleLabel.setObjectName(u"tittleLabel")
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.tittleLabel.setFont(font)
        self.tittleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.tittleLabel)


        self.horizontalLayout_3.addWidget(self.headerTitleFrame)

        self.headerRightButtonsFrame = QFrame(self.headerFrame)
        self.headerRightButtonsFrame.setObjectName(u"headerRightButtonsFrame")
        self.headerRightButtonsFrame.setMinimumSize(QSize(150, 0))
        self.headerRightButtonsFrame.setMaximumSize(QSize(150, 16777215))
        self.headerRightButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headerRightButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.headerRightButtonsFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.headerRightButtonsFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setMinimumSize(QSize(0, 50))
        self.minimizeButton.setMaximumSize(QSize(16777215, 50))
        icon1 = QIcon()
        icon1.addFile(u":/headerRightButtons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.minimizeButton)

        self.maximizeButton = QPushButton(self.headerRightButtonsFrame)
        self.maximizeButton.setObjectName(u"maximizeButton")
        self.maximizeButton.setMinimumSize(QSize(0, 50))
        self.maximizeButton.setMaximumSize(QSize(16777215, 50))
        icon2 = QIcon()
        icon2.addFile(u":/headerRightButtons/feather/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.maximizeButton)

        self.exitButton = QPushButton(self.headerRightButtonsFrame)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setMinimumSize(QSize(0, 50))
        self.exitButton.setMaximumSize(QSize(16777215, 50))
        icon3 = QIcon()
        icon3.addFile(u":/headerRightButtons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon3)

        self.horizontalLayout_4.addWidget(self.exitButton)


        self.horizontalLayout_3.addWidget(self.headerRightButtonsFrame)


        self.verticalLayout.addWidget(self.headerFrame)

        self.mainBodyFrame = QFrame(self.centralwidget)
        self.mainBodyFrame.setObjectName(u"mainBodyFrame")
        self.mainBodyFrame.setStyleSheet(u"QPushButton{ \n"
"	background-repeat: no-repeat;\n"
"	background-position: left center;\n"
"	padding-left:30px;\n"
"	padding-bottom: 10px; \n"
"	padding-top: 10px; \n"
"	color: #F8F8F2; \n"
"	font-size: 15px; \n"
"} ")
        self.mainBodyFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainBodyFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyFrame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainBodyLeftButtonsFrame = QFrame(self.mainBodyFrame)
        self.mainBodyLeftButtonsFrame.setObjectName(u"mainBodyLeftButtonsFrame")
        self.mainBodyLeftButtonsFrame.setMinimumSize(QSize(100, 0))
        self.mainBodyLeftButtonsFrame.setMaximumSize(QSize(0, 16777215))
        self.mainBodyLeftButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainBodyLeftButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyLeftButtonsFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.homeButton.setObjectName(u"homeButton")
        font1 = QFont()
        font1.setBold(True)
        self.homeButton.setFont(font1)
        self.homeButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/home.svg); \n"
"}\n"
"\n"
"QPushButton{border-left: 3px solid #FFB86C;}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.homeButton)

        self.cameraButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.cameraButton.setObjectName(u"cameraButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraButton.sizePolicy().hasHeightForWidth())
        self.cameraButton.setSizePolicy(sizePolicy)
        self.cameraButton.setMinimumSize(QSize(100, 0))
        self.cameraButton.setFont(font1)
        self.cameraButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/camera.svg); \n"
"} ")

        self.verticalLayout_2.addWidget(self.cameraButton)

        self.ocrButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.ocrButton.setObjectName(u"ocrButton")
        self.ocrButton.setFont(font1)
        self.ocrButton.setStyleSheet(u"QPushButton{ \n"
"	background-image: url(:/mainBodyLeftButtons/feather/file-text.svg);\n"
"}\n"
"\n"
"QPushButton{border-left: 3px solid #FFB86C;}\n"
"\n"
"")

        self.verticalLayout_2.addWidget(self.ocrButton)

        self.verticalSpacer = QSpacerItem(20, 403, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingsButton = QPushButton(self.mainBodyLeftButtonsFrame)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setFont(font1)
        self.settingsButton.setStyleSheet(u"QPushButton{ \n"
"background-image: url(:/mainBodyLeftButtons/feather/settings.svg); \n"
"} ")

        self.verticalLayout_2.addWidget(self.settingsButton)


        self.horizontalLayout_7.addWidget(self.mainBodyLeftButtonsFrame)

        self.mainBodyStackedWidget = QStackedWidget(self.mainBodyFrame)
        self.mainBodyStackedWidget.setObjectName(u"mainBodyStackedWidget")
        self.mainBodyStackedWidget.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"QScrollArea {\n"
"        border: 2px solid #5e5e5e;\n"
"        background-color: #f0f0f0;\n"
"    }")
        self.horizontalLayout_9 = QHBoxLayout(self.homePage)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.homePageFrame = QFrame(self.homePage)
        self.homePageFrame.setObjectName(u"homePageFrame")
        self.homePageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homePageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.homePageFrame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.homePageStackedWidgetFrame = QFrame(self.homePageFrame)
        self.homePageStackedWidgetFrame.setObjectName(u"homePageStackedWidgetFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homePageStackedWidgetFrame.sizePolicy().hasHeightForWidth())
        self.homePageStackedWidgetFrame.setSizePolicy(sizePolicy1)
        self.homePageStackedWidgetFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.homePageStackedWidgetFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homePageStackedWidgetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.homePageStackedWidgetFrame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.navigationIndicatorFrame = QFrame(self.homePageStackedWidgetFrame)
        self.navigationIndicatorFrame.setObjectName(u"navigationIndicatorFrame")
        self.navigationIndicatorFrame.setMinimumSize(QSize(400, 150))
        self.navigationIndicatorFrame.setMaximumSize(QSize(16777215, 150))
        self.navigationIndicatorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.navigationIndicatorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.navigationIndicatorFrame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(1203, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)

        self.artificialHorizonFrame = QFrame(self.navigationIndicatorFrame)
        self.artificialHorizonFrame.setObjectName(u"artificialHorizonFrame")
        self.artificialHorizonFrame.setMinimumSize(QSize(200, 150))
        self.artificialHorizonFrame.setMaximumSize(QSize(200, 150))
        self.artificialHorizonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.artificialHorizonFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.artificialHorizonFrame)

        self.CompassFrame = QFrame(self.navigationIndicatorFrame)
        self.CompassFrame.setObjectName(u"CompassFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.CompassFrame.sizePolicy().hasHeightForWidth())
        self.CompassFrame.setSizePolicy(sizePolicy2)
        self.CompassFrame.setMinimumSize(QSize(200, 150))
        self.CompassFrame.setMaximumSize(QSize(200, 150))
        self.CompassFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.CompassFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_16.addWidget(self.CompassFrame)


        self.verticalLayout_23.addWidget(self.navigationIndicatorFrame)

        self.homePageStackedWidget = QStackedWidget(self.homePageStackedWidgetFrame)
        self.homePageStackedWidget.setObjectName(u"homePageStackedWidget")
        self.mainHomePage = QWidget()
        self.mainHomePage.setObjectName(u"mainHomePage")
        self.horizontalLayout_47 = QHBoxLayout(self.mainHomePage)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageCamerasFrame = QFrame(self.mainHomePage)
        self.mainHomePageCamerasFrame.setObjectName(u"mainHomePageCamerasFrame")
        self.mainHomePageCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.mainHomePageCamerasFrame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageTopCamerasFrame = QFrame(self.mainHomePageCamerasFrame)
        self.mainHomePageTopCamerasFrame.setObjectName(u"mainHomePageTopCamerasFrame")
        self.mainHomePageTopCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.mainHomePageTopCamerasFrame)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageTopLeftCamerasFrame = QFrame(self.mainHomePageTopCamerasFrame)
        self.mainHomePageTopLeftCamerasFrame.setObjectName(u"mainHomePageTopLeftCamerasFrame")
        self.mainHomePageTopLeftCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopLeftCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.mainHomePageTopLeftCamerasFrame)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageTopLeftCameraLabelFrame = QFrame(self.mainHomePageTopLeftCamerasFrame)
        self.mainHomePageTopLeftCameraLabelFrame.setObjectName(u"mainHomePageTopLeftCameraLabelFrame")
        self.mainHomePageTopLeftCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.mainHomePageTopLeftCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.mainHomePageTopLeftCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.mainHomePageTopLeftCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopLeftCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.mainHomePageTopLeftCameraLabelFrame)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageTopLeftCameraLabel = QLabel(self.mainHomePageTopLeftCameraLabelFrame)
        self.mainHomePageTopLeftCameraLabel.setObjectName(u"mainHomePageTopLeftCameraLabel")
        self.mainHomePageTopLeftCameraLabel.setMinimumSize(QSize(800, 400))
        self.mainHomePageTopLeftCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_59.addWidget(self.mainHomePageTopLeftCameraLabel)


        self.verticalLayout_12.addWidget(self.mainHomePageTopLeftCameraLabelFrame)

        self.mainHomePageTopLeftCamerasIndicators = QFrame(self.mainHomePageTopLeftCamerasFrame)
        self.mainHomePageTopLeftCamerasIndicators.setObjectName(u"mainHomePageTopLeftCamerasIndicators")
        self.mainHomePageTopLeftCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.mainHomePageTopLeftCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.mainHomePageTopLeftCamerasIndicators.setStyleSheet(u"")
        self.mainHomePageTopLeftCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopLeftCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.mainHomePageTopLeftCamerasIndicators)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.mainHomePageTopLeftCamerasNumberLabel = QLabel(self.mainHomePageTopLeftCamerasIndicators)
        self.mainHomePageTopLeftCamerasNumberLabel.setObjectName(u"mainHomePageTopLeftCamerasNumberLabel")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.mainHomePageTopLeftCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_63.addWidget(self.mainHomePageTopLeftCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_12.addWidget(self.mainHomePageTopLeftCamerasIndicators)


        self.horizontalLayout_55.addWidget(self.mainHomePageTopLeftCamerasFrame)

        self.mainHomePageTopRightCamerasFrame = QFrame(self.mainHomePageTopCamerasFrame)
        self.mainHomePageTopRightCamerasFrame.setObjectName(u"mainHomePageTopRightCamerasFrame")
        self.mainHomePageTopRightCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopRightCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.mainHomePageTopRightCamerasFrame)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageTopRightCameraLabelFrame = QFrame(self.mainHomePageTopRightCamerasFrame)
        self.mainHomePageTopRightCameraLabelFrame.setObjectName(u"mainHomePageTopRightCameraLabelFrame")
        self.mainHomePageTopRightCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.mainHomePageTopRightCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.mainHomePageTopRightCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.mainHomePageTopRightCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopRightCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.mainHomePageTopRightCameraLabelFrame)
        self.horizontalLayout_60.setSpacing(0)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageTopRightCameraLabel = QLabel(self.mainHomePageTopRightCameraLabelFrame)
        self.mainHomePageTopRightCameraLabel.setObjectName(u"mainHomePageTopRightCameraLabel")
        self.mainHomePageTopRightCameraLabel.setMinimumSize(QSize(800, 400))
        self.mainHomePageTopRightCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_60.addWidget(self.mainHomePageTopRightCameraLabel)


        self.verticalLayout_13.addWidget(self.mainHomePageTopRightCameraLabelFrame)

        self.mainHomePageTopRightCamerasIndicators = QFrame(self.mainHomePageTopRightCamerasFrame)
        self.mainHomePageTopRightCamerasIndicators.setObjectName(u"mainHomePageTopRightCamerasIndicators")
        self.mainHomePageTopRightCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.mainHomePageTopRightCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.mainHomePageTopRightCamerasIndicators.setStyleSheet(u"")
        self.mainHomePageTopRightCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageTopRightCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.mainHomePageTopRightCamerasIndicators)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.mainHomePageTopRightCamerasNumberLabel = QLabel(self.mainHomePageTopRightCamerasIndicators)
        self.mainHomePageTopRightCamerasNumberLabel.setObjectName(u"mainHomePageTopRightCamerasNumberLabel")
        self.mainHomePageTopRightCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_64.addWidget(self.mainHomePageTopRightCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_13.addWidget(self.mainHomePageTopRightCamerasIndicators)


        self.horizontalLayout_55.addWidget(self.mainHomePageTopRightCamerasFrame)


        self.verticalLayout_11.addWidget(self.mainHomePageTopCamerasFrame)

        self.mainHomePageBottomCamerasFrame = QFrame(self.mainHomePageCamerasFrame)
        self.mainHomePageBottomCamerasFrame.setObjectName(u"mainHomePageBottomCamerasFrame")
        self.mainHomePageBottomCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.mainHomePageBottomCamerasFrame)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageBottomLeftCamerasFrame = QFrame(self.mainHomePageBottomCamerasFrame)
        self.mainHomePageBottomLeftCamerasFrame.setObjectName(u"mainHomePageBottomLeftCamerasFrame")
        self.mainHomePageBottomLeftCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomLeftCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.mainHomePageBottomLeftCamerasFrame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageBottomLeftCameraLabelFrame = QFrame(self.mainHomePageBottomLeftCamerasFrame)
        self.mainHomePageBottomLeftCameraLabelFrame.setObjectName(u"mainHomePageBottomLeftCameraLabelFrame")
        self.mainHomePageBottomLeftCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.mainHomePageBottomLeftCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.mainHomePageBottomLeftCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.mainHomePageBottomLeftCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomLeftCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.mainHomePageBottomLeftCameraLabelFrame)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageBottomLeftCameraLabel = QLabel(self.mainHomePageBottomLeftCameraLabelFrame)
        self.mainHomePageBottomLeftCameraLabel.setObjectName(u"mainHomePageBottomLeftCameraLabel")
        self.mainHomePageBottomLeftCameraLabel.setMinimumSize(QSize(800, 400))
        self.mainHomePageBottomLeftCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_62.addWidget(self.mainHomePageBottomLeftCameraLabel)


        self.verticalLayout_15.addWidget(self.mainHomePageBottomLeftCameraLabelFrame)

        self.mainHomePageBottomLeftCamerasIndicators = QFrame(self.mainHomePageBottomLeftCamerasFrame)
        self.mainHomePageBottomLeftCamerasIndicators.setObjectName(u"mainHomePageBottomLeftCamerasIndicators")
        self.mainHomePageBottomLeftCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.mainHomePageBottomLeftCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.mainHomePageBottomLeftCamerasIndicators.setStyleSheet(u"")
        self.mainHomePageBottomLeftCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomLeftCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.mainHomePageBottomLeftCamerasIndicators)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.mainHomePageBottomLeftCamerasNumberLabel = QLabel(self.mainHomePageBottomLeftCamerasIndicators)
        self.mainHomePageBottomLeftCamerasNumberLabel.setObjectName(u"mainHomePageBottomLeftCamerasNumberLabel")
        self.mainHomePageBottomLeftCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_65.addWidget(self.mainHomePageBottomLeftCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_15.addWidget(self.mainHomePageBottomLeftCamerasIndicators)


        self.horizontalLayout_56.addWidget(self.mainHomePageBottomLeftCamerasFrame)

        self.mainHomePageBottomRightCamerasFrame = QFrame(self.mainHomePageBottomCamerasFrame)
        self.mainHomePageBottomRightCamerasFrame.setObjectName(u"mainHomePageBottomRightCamerasFrame")
        self.mainHomePageBottomRightCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomRightCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.mainHomePageBottomRightCamerasFrame)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageBottomRightCameraLabelFrame = QFrame(self.mainHomePageBottomRightCamerasFrame)
        self.mainHomePageBottomRightCameraLabelFrame.setObjectName(u"mainHomePageBottomRightCameraLabelFrame")
        self.mainHomePageBottomRightCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.mainHomePageBottomRightCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.mainHomePageBottomRightCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.mainHomePageBottomRightCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomRightCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.mainHomePageBottomRightCameraLabelFrame)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.mainHomePageBottomRightCameraLabel = QLabel(self.mainHomePageBottomRightCameraLabelFrame)
        self.mainHomePageBottomRightCameraLabel.setObjectName(u"mainHomePageBottomRightCameraLabel")
        self.mainHomePageBottomRightCameraLabel.setMinimumSize(QSize(800, 400))
        self.mainHomePageBottomRightCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_61.addWidget(self.mainHomePageBottomRightCameraLabel)


        self.verticalLayout_14.addWidget(self.mainHomePageBottomRightCameraLabelFrame)

        self.mainHomePageBottomRightCamerasIndicators = QFrame(self.mainHomePageBottomRightCamerasFrame)
        self.mainHomePageBottomRightCamerasIndicators.setObjectName(u"mainHomePageBottomRightCamerasIndicators")
        self.mainHomePageBottomRightCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.mainHomePageBottomRightCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.mainHomePageBottomRightCamerasIndicators.setStyleSheet(u"")
        self.mainHomePageBottomRightCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainHomePageBottomRightCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.mainHomePageBottomRightCamerasIndicators)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.mainHomePageBottomRightCamerasNumberLabel = QLabel(self.mainHomePageBottomRightCamerasIndicators)
        self.mainHomePageBottomRightCamerasNumberLabel.setObjectName(u"mainHomePageBottomRightCamerasNumberLabel")
        self.mainHomePageBottomRightCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_66.addWidget(self.mainHomePageBottomRightCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_14.addWidget(self.mainHomePageBottomRightCamerasIndicators)


        self.horizontalLayout_56.addWidget(self.mainHomePageBottomRightCamerasFrame)


        self.verticalLayout_11.addWidget(self.mainHomePageBottomCamerasFrame)


        self.horizontalLayout_47.addWidget(self.mainHomePageCamerasFrame)

        self.homePageStackedWidget.addWidget(self.mainHomePage)
        self.secondayHomePage = QWidget()
        self.secondayHomePage.setObjectName(u"secondayHomePage")
        self.horizontalLayout_54 = QHBoxLayout(self.secondayHomePage)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageCamerasFrame = QFrame(self.secondayHomePage)
        self.secondaryHomePageCamerasFrame.setObjectName(u"secondaryHomePageCamerasFrame")
        self.secondaryHomePageCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.secondaryHomePageCamerasFrame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageTopCamerasFrame = QFrame(self.secondaryHomePageCamerasFrame)
        self.secondaryHomePageTopCamerasFrame.setObjectName(u"secondaryHomePageTopCamerasFrame")
        self.secondaryHomePageTopCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.secondaryHomePageTopCamerasFrame)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageTopLeftCamerasFrame = QFrame(self.secondaryHomePageTopCamerasFrame)
        self.secondaryHomePageTopLeftCamerasFrame.setObjectName(u"secondaryHomePageTopLeftCamerasFrame")
        self.secondaryHomePageTopLeftCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopLeftCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.secondaryHomePageTopLeftCamerasFrame)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageTopLeftCameraLabelFrame = QFrame(self.secondaryHomePageTopLeftCamerasFrame)
        self.secondaryHomePageTopLeftCameraLabelFrame.setObjectName(u"secondaryHomePageTopLeftCameraLabelFrame")
        self.secondaryHomePageTopLeftCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageTopLeftCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.secondaryHomePageTopLeftCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.secondaryHomePageTopLeftCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopLeftCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.secondaryHomePageTopLeftCameraLabelFrame)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageTopLeftCameraLabel = QLabel(self.secondaryHomePageTopLeftCameraLabelFrame)
        self.secondaryHomePageTopLeftCameraLabel.setObjectName(u"secondaryHomePageTopLeftCameraLabel")
        self.secondaryHomePageTopLeftCameraLabel.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageTopLeftCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_67.addWidget(self.secondaryHomePageTopLeftCameraLabel)


        self.verticalLayout_18.addWidget(self.secondaryHomePageTopLeftCameraLabelFrame)

        self.secondaryHomePageTopLeftCamerasIndicators = QFrame(self.secondaryHomePageTopLeftCamerasFrame)
        self.secondaryHomePageTopLeftCamerasIndicators.setObjectName(u"secondaryHomePageTopLeftCamerasIndicators")
        self.secondaryHomePageTopLeftCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.secondaryHomePageTopLeftCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.secondaryHomePageTopLeftCamerasIndicators.setStyleSheet(u"")
        self.secondaryHomePageTopLeftCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopLeftCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.secondaryHomePageTopLeftCamerasIndicators)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.secondaryHomePageTopLeftCamerasNumberLabel = QLabel(self.secondaryHomePageTopLeftCamerasIndicators)
        self.secondaryHomePageTopLeftCamerasNumberLabel.setObjectName(u"secondaryHomePageTopLeftCamerasNumberLabel")
        self.secondaryHomePageTopLeftCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_71.addWidget(self.secondaryHomePageTopLeftCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_18.addWidget(self.secondaryHomePageTopLeftCamerasIndicators)


        self.horizontalLayout_58.addWidget(self.secondaryHomePageTopLeftCamerasFrame)

        self.secondaryHomePageTopRightCamerasFrame = QFrame(self.secondaryHomePageTopCamerasFrame)
        self.secondaryHomePageTopRightCamerasFrame.setObjectName(u"secondaryHomePageTopRightCamerasFrame")
        self.secondaryHomePageTopRightCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopRightCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.secondaryHomePageTopRightCamerasFrame)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageTopRightCameraLabelFrame = QFrame(self.secondaryHomePageTopRightCamerasFrame)
        self.secondaryHomePageTopRightCameraLabelFrame.setObjectName(u"secondaryHomePageTopRightCameraLabelFrame")
        self.secondaryHomePageTopRightCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageTopRightCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.secondaryHomePageTopRightCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.secondaryHomePageTopRightCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopRightCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.secondaryHomePageTopRightCameraLabelFrame)
        self.horizontalLayout_68.setSpacing(0)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.horizontalLayout_68.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageTopRightCameraLabel = QLabel(self.secondaryHomePageTopRightCameraLabelFrame)
        self.secondaryHomePageTopRightCameraLabel.setObjectName(u"secondaryHomePageTopRightCameraLabel")
        self.secondaryHomePageTopRightCameraLabel.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageTopRightCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_68.addWidget(self.secondaryHomePageTopRightCameraLabel)


        self.verticalLayout_19.addWidget(self.secondaryHomePageTopRightCameraLabelFrame)

        self.secondaryHomePageTopRightCamerasIndicators = QFrame(self.secondaryHomePageTopRightCamerasFrame)
        self.secondaryHomePageTopRightCamerasIndicators.setObjectName(u"secondaryHomePageTopRightCamerasIndicators")
        self.secondaryHomePageTopRightCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.secondaryHomePageTopRightCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.secondaryHomePageTopRightCamerasIndicators.setStyleSheet(u"")
        self.secondaryHomePageTopRightCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageTopRightCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.secondaryHomePageTopRightCamerasIndicators)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.secondaryHomePageTopRightCamerasNumberLabel = QLabel(self.secondaryHomePageTopRightCamerasIndicators)
        self.secondaryHomePageTopRightCamerasNumberLabel.setObjectName(u"secondaryHomePageTopRightCamerasNumberLabel")
        self.secondaryHomePageTopRightCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_72.addWidget(self.secondaryHomePageTopRightCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_19.addWidget(self.secondaryHomePageTopRightCamerasIndicators)


        self.horizontalLayout_58.addWidget(self.secondaryHomePageTopRightCamerasFrame)


        self.verticalLayout_20.addWidget(self.secondaryHomePageTopCamerasFrame)

        self.secondaryHomePageBottomCamerasFrame = QFrame(self.secondaryHomePageCamerasFrame)
        self.secondaryHomePageBottomCamerasFrame.setObjectName(u"secondaryHomePageBottomCamerasFrame")
        self.secondaryHomePageBottomCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.secondaryHomePageBottomCamerasFrame)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageBottomLeftCamerasFrame = QFrame(self.secondaryHomePageBottomCamerasFrame)
        self.secondaryHomePageBottomLeftCamerasFrame.setObjectName(u"secondaryHomePageBottomLeftCamerasFrame")
        self.secondaryHomePageBottomLeftCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomLeftCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.secondaryHomePageBottomLeftCamerasFrame)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageBottomLeftCameraLabelFrame = QFrame(self.secondaryHomePageBottomLeftCamerasFrame)
        self.secondaryHomePageBottomLeftCameraLabelFrame.setObjectName(u"secondaryHomePageBottomLeftCameraLabelFrame")
        self.secondaryHomePageBottomLeftCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageBottomLeftCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.secondaryHomePageBottomLeftCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.secondaryHomePageBottomLeftCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomLeftCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.secondaryHomePageBottomLeftCameraLabelFrame)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageBottomLeftCameraLabel = QLabel(self.secondaryHomePageBottomLeftCameraLabelFrame)
        self.secondaryHomePageBottomLeftCameraLabel.setObjectName(u"secondaryHomePageBottomLeftCameraLabel")
        self.secondaryHomePageBottomLeftCameraLabel.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageBottomLeftCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_69.addWidget(self.secondaryHomePageBottomLeftCameraLabel)


        self.verticalLayout_16.addWidget(self.secondaryHomePageBottomLeftCameraLabelFrame)

        self.secondaryHomePageBottomLeftCamerasIndicators = QFrame(self.secondaryHomePageBottomLeftCamerasFrame)
        self.secondaryHomePageBottomLeftCamerasIndicators.setObjectName(u"secondaryHomePageBottomLeftCamerasIndicators")
        self.secondaryHomePageBottomLeftCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.secondaryHomePageBottomLeftCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.secondaryHomePageBottomLeftCamerasIndicators.setStyleSheet(u"")
        self.secondaryHomePageBottomLeftCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomLeftCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.secondaryHomePageBottomLeftCamerasIndicators)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.secondaryHomePageBottomLeftCamerasNumberLabel = QLabel(self.secondaryHomePageBottomLeftCamerasIndicators)
        self.secondaryHomePageBottomLeftCamerasNumberLabel.setObjectName(u"secondaryHomePageBottomLeftCamerasNumberLabel")
        self.secondaryHomePageBottomLeftCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_73.addWidget(self.secondaryHomePageBottomLeftCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_16.addWidget(self.secondaryHomePageBottomLeftCamerasIndicators)


        self.horizontalLayout_57.addWidget(self.secondaryHomePageBottomLeftCamerasFrame)

        self.secondaryHomePageBottomRightCamerasFrame = QFrame(self.secondaryHomePageBottomCamerasFrame)
        self.secondaryHomePageBottomRightCamerasFrame.setObjectName(u"secondaryHomePageBottomRightCamerasFrame")
        self.secondaryHomePageBottomRightCamerasFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomRightCamerasFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.secondaryHomePageBottomRightCamerasFrame)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageBottomRightCameraLabelFrame = QFrame(self.secondaryHomePageBottomRightCamerasFrame)
        self.secondaryHomePageBottomRightCameraLabelFrame.setObjectName(u"secondaryHomePageBottomRightCameraLabelFrame")
        self.secondaryHomePageBottomRightCameraLabelFrame.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageBottomRightCameraLabelFrame.setMaximumSize(QSize(800, 400))
        self.secondaryHomePageBottomRightCameraLabelFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #282A36;\n"
"}\n"
"")
        self.secondaryHomePageBottomRightCameraLabelFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomRightCameraLabelFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.secondaryHomePageBottomRightCameraLabelFrame)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.secondaryHomePageBottomRightCameraLabel = QLabel(self.secondaryHomePageBottomRightCameraLabelFrame)
        self.secondaryHomePageBottomRightCameraLabel.setObjectName(u"secondaryHomePageBottomRightCameraLabel")
        self.secondaryHomePageBottomRightCameraLabel.setMinimumSize(QSize(800, 400))
        self.secondaryHomePageBottomRightCameraLabel.setMaximumSize(QSize(800, 400))

        self.horizontalLayout_70.addWidget(self.secondaryHomePageBottomRightCameraLabel)


        self.verticalLayout_17.addWidget(self.secondaryHomePageBottomRightCameraLabelFrame)

        self.secondaryHomePageBottomRightCamerasIndicators = QFrame(self.secondaryHomePageBottomRightCamerasFrame)
        self.secondaryHomePageBottomRightCamerasIndicators.setObjectName(u"secondaryHomePageBottomRightCamerasIndicators")
        self.secondaryHomePageBottomRightCamerasIndicators.setMinimumSize(QSize(800, 50))
        self.secondaryHomePageBottomRightCamerasIndicators.setMaximumSize(QSize(800, 50))
        self.secondaryHomePageBottomRightCamerasIndicators.setStyleSheet(u"")
        self.secondaryHomePageBottomRightCamerasIndicators.setFrameShape(QFrame.Shape.StyledPanel)
        self.secondaryHomePageBottomRightCamerasIndicators.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.secondaryHomePageBottomRightCamerasIndicators)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.secondaryHomePageBottomRightCamerasNumberLabel = QLabel(self.secondaryHomePageBottomRightCamerasIndicators)
        self.secondaryHomePageBottomRightCamerasNumberLabel.setObjectName(u"secondaryHomePageBottomRightCamerasNumberLabel")
        self.secondaryHomePageBottomRightCamerasNumberLabel.setFont(font2)

        self.horizontalLayout_74.addWidget(self.secondaryHomePageBottomRightCamerasNumberLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_17.addWidget(self.secondaryHomePageBottomRightCamerasIndicators)


        self.horizontalLayout_57.addWidget(self.secondaryHomePageBottomRightCamerasFrame)


        self.verticalLayout_20.addWidget(self.secondaryHomePageBottomCamerasFrame)


        self.horizontalLayout_54.addWidget(self.secondaryHomePageCamerasFrame)

        self.homePageStackedWidget.addWidget(self.secondayHomePage)

        self.verticalLayout_23.addWidget(self.homePageStackedWidget)


        self.horizontalLayout_12.addWidget(self.homePageStackedWidgetFrame)

        self.homePageIndicatorFrame = QFrame(self.homePageFrame)
        self.homePageIndicatorFrame.setObjectName(u"homePageIndicatorFrame")
        self.homePageIndicatorFrame.setMinimumSize(QSize(200, 0))
        self.homePageIndicatorFrame.setMaximumSize(QSize(200, 16777215))
        self.homePageIndicatorFrame.setStyleSheet(u"")
        self.homePageIndicatorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.homePageIndicatorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.homePageIndicatorFrame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gaugeFrame = QFrame(self.homePageIndicatorFrame)
        self.gaugeFrame.setObjectName(u"gaugeFrame")
        self.gaugeFrame.setStyleSheet(u"")
        self.gaugeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gaugeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.gaugeFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fourThrustersFrame = QFrame(self.gaugeFrame)
        self.fourThrustersFrame.setObjectName(u"fourThrustersFrame")
        self.fourThrustersFrame.setMinimumSize(QSize(150, 150))
        self.fourThrustersFrame.setMaximumSize(QSize(150, 150))
        self.fourThrustersFrame.setStyleSheet(u"")
        self.fourThrustersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fourThrustersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.fourThrustersGauge = QFrame(self.fourThrustersFrame)
        self.fourThrustersGauge.setObjectName(u"fourThrustersGauge")
        self.fourThrustersGauge.setGeometry(QRect(10, 10, 130, 130))
        self.fourThrustersGauge.setMinimumSize(QSize(130, 130))
        self.fourThrustersGauge.setMaximumSize(QSize(130, 130))
        self.fourThrustersGauge.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(68, 71, 90, 255), stop:0.750 rgba(255, 184, 108, 255));\n"
"}\n"
"")
        self.fourThrustersGauge.setFrameShape(QFrame.Shape.StyledPanel)
        self.fourThrustersGauge.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG = QFrame(self.fourThrustersFrame)
        self.circularBG.setObjectName(u"circularBG")
        self.circularBG.setGeometry(QRect(10, 10, 130, 130))
        self.circularBG.setMinimumSize(QSize(130, 130))
        self.circularBG.setMaximumSize(QSize(130, 130))
        self.circularBG.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: rgba(77, 77, 127, 100);\n"
"}")
        self.circularBG.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBG.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.fourThrustersFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 110, 110))
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius:55px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(27, 27, 55, 55))
        self.frame_2.setStyleSheet(u"border-radius:70px;\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.fourThrustersLabel = QLabel(self.frame_2)
        self.fourThrustersLabel.setObjectName(u"fourThrustersLabel")
        self.fourThrustersLabel.setScaledContents(True)
        self.fourThrustersLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_13.addWidget(self.fourThrustersLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.circularBG.raise_()
        self.fourThrustersGauge.raise_()
        self.frame.raise_()

        self.verticalLayout_8.addWidget(self.fourThrustersFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.upDownThrustersFrame = QFrame(self.gaugeFrame)
        self.upDownThrustersFrame.setObjectName(u"upDownThrustersFrame")
        self.upDownThrustersFrame.setMinimumSize(QSize(150, 150))
        self.upDownThrustersFrame.setMaximumSize(QSize(150, 150))
        self.upDownThrustersFrame.setStyleSheet(u"")
        self.upDownThrustersFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.upDownThrustersFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.upDownThrustersGauge = QFrame(self.upDownThrustersFrame)
        self.upDownThrustersGauge.setObjectName(u"upDownThrustersGauge")
        self.upDownThrustersGauge.setGeometry(QRect(10, 10, 130, 130))
        self.upDownThrustersGauge.setMinimumSize(QSize(130, 130))
        self.upDownThrustersGauge.setMaximumSize(QSize(130, 130))
        self.upDownThrustersGauge.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(68, 71, 90, 255), stop:0.750 rgba(255, 184, 108, 255));\n"
"}\n"
"")
        self.upDownThrustersGauge.setFrameShape(QFrame.Shape.StyledPanel)
        self.upDownThrustersGauge.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7 = QFrame(self.upDownThrustersFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(20, 20, 110, 110))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	border-radius:55px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(27, 27, 55, 55))
        self.frame_9.setStyleSheet(u"border-radius:70px;\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.upDownThrustersLabel = QLabel(self.frame_9)
        self.upDownThrustersLabel.setObjectName(u"upDownThrustersLabel")
        self.upDownThrustersLabel.setScaledContents(True)
        self.upDownThrustersLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.upDownThrustersLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.circularBG_4 = QFrame(self.upDownThrustersFrame)
        self.circularBG_4.setObjectName(u"circularBG_4")
        self.circularBG_4.setGeometry(QRect(10, 10, 130, 130))
        self.circularBG_4.setMinimumSize(QSize(130, 130))
        self.circularBG_4.setMaximumSize(QSize(130, 130))
        self.circularBG_4.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: rgba(77, 77, 127, 100);\n"
"}")
        self.circularBG_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBG_4.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG_4.raise_()
        self.upDownThrustersGauge.raise_()
        self.frame_7.raise_()

        self.verticalLayout_8.addWidget(self.upDownThrustersFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.servoFrame = QFrame(self.gaugeFrame)
        self.servoFrame.setObjectName(u"servoFrame")
        self.servoFrame.setMinimumSize(QSize(150, 150))
        self.servoFrame.setMaximumSize(QSize(150, 150))
        self.servoFrame.setStyleSheet(u"")
        self.servoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.servoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.servoGauge = QFrame(self.servoFrame)
        self.servoGauge.setObjectName(u"servoGauge")
        self.servoGauge.setGeometry(QRect(10, 10, 130, 130))
        self.servoGauge.setMinimumSize(QSize(130, 130))
        self.servoGauge.setMaximumSize(QSize(130, 130))
        self.servoGauge.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(68, 71, 90, 255), stop:0.750 rgba(255, 184, 108, 255));\n"
"}\n"
"")
        self.servoGauge.setFrameShape(QFrame.Shape.StyledPanel)
        self.servoGauge.setFrameShadow(QFrame.Shadow.Raised)
        self.circularBG_2 = QFrame(self.servoFrame)
        self.circularBG_2.setObjectName(u"circularBG_2")
        self.circularBG_2.setGeometry(QRect(10, 10, 130, 130))
        self.circularBG_2.setMinimumSize(QSize(130, 130))
        self.circularBG_2.setMaximumSize(QSize(130, 130))
        self.circularBG_2.setStyleSheet(u"QFrame{\n"
"	border-radius:65px;\n"
"	background-color: rgba(77, 77, 127, 100);\n"
"}")
        self.circularBG_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.circularBG_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.servoFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 20, 110, 110))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border-radius:55px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(27, 27, 55, 55))
        self.frame_4.setStyleSheet(u"border-radius:70px;\n"
"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.servoLabel = QLabel(self.frame_4)
        self.servoLabel.setObjectName(u"servoLabel")
        self.servoLabel.setScaledContents(True)
        self.servoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_34.addWidget(self.servoLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.circularBG_2.raise_()
        self.servoGauge.raise_()
        self.frame_3.raise_()

        self.verticalLayout_8.addWidget(self.servoFrame, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.gaugeFrame)

        self.indicatorsFrame = QFrame(self.homePageIndicatorFrame)
        self.indicatorsFrame.setObjectName(u"indicatorsFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.indicatorsFrame.sizePolicy().hasHeightForWidth())
        self.indicatorsFrame.setSizePolicy(sizePolicy3)
        self.indicatorsFrame.setStyleSheet(u"QFrame{\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"")
        self.indicatorsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.indicatorsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.indicatorsFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.armingFrame = QFrame(self.indicatorsFrame)
        self.armingFrame.setObjectName(u"armingFrame")
        self.armingFrame.setMaximumSize(QSize(16777215, 30))
        self.armingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.armingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.armingFrame)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.armingLabel = QLabel(self.armingFrame)
        self.armingLabel.setObjectName(u"armingLabel")
        self.armingLabel.setFont(font2)
        self.armingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_89.addWidget(self.armingLabel)


        self.verticalLayout_4.addWidget(self.armingFrame)

        self.ledFrame = QFrame(self.indicatorsFrame)
        self.ledFrame.setObjectName(u"ledFrame")
        self.ledFrame.setMaximumSize(QSize(16777215, 30))
        self.ledFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ledFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.ledFrame)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.ledLabel = QLabel(self.ledFrame)
        self.ledLabel.setObjectName(u"ledLabel")
        self.ledLabel.setMaximumSize(QSize(16777215, 30))
        self.ledLabel.setFont(font2)
        self.ledLabel.setStyleSheet(u"")
        self.ledLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_42.addWidget(self.ledLabel)


        self.verticalLayout_4.addWidget(self.ledFrame)

        self.rightGripperFrame = QFrame(self.indicatorsFrame)
        self.rightGripperFrame.setObjectName(u"rightGripperFrame")
        self.rightGripperFrame.setMaximumSize(QSize(16777215, 30))
        self.rightGripperFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightGripperFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.rightGripperFrame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.gripperLabel = QLabel(self.rightGripperFrame)
        self.gripperLabel.setObjectName(u"gripperLabel")
        self.gripperLabel.setFont(font2)
        self.gripperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_43.addWidget(self.gripperLabel)


        self.verticalLayout_4.addWidget(self.rightGripperFrame)

        self.leftGripperFrame = QFrame(self.indicatorsFrame)
        self.leftGripperFrame.setObjectName(u"leftGripperFrame")
        self.leftGripperFrame.setMaximumSize(QSize(16777215, 30))
        self.leftGripperFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftGripperFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.leftGripperFrame)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.leftGripperLabel = QLabel(self.leftGripperFrame)
        self.leftGripperLabel.setObjectName(u"leftGripperLabel")
        self.leftGripperLabel.setFont(font2)
        self.leftGripperLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.leftGripperLabel)


        self.verticalLayout_4.addWidget(self.leftGripperFrame)

        self.fluidSuctionFrame = QFrame(self.indicatorsFrame)
        self.fluidSuctionFrame.setObjectName(u"fluidSuctionFrame")
        self.fluidSuctionFrame.setMaximumSize(QSize(16777215, 30))
        self.fluidSuctionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.fluidSuctionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.fluidSuctionFrame)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.fluidSuctionLabel = QLabel(self.fluidSuctionFrame)
        self.fluidSuctionLabel.setObjectName(u"fluidSuctionLabel")
        self.fluidSuctionLabel.setFont(font2)
        self.fluidSuctionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_45.addWidget(self.fluidSuctionLabel)


        self.verticalLayout_4.addWidget(self.fluidSuctionFrame)

        self.floatingDebrisFrame = QFrame(self.indicatorsFrame)
        self.floatingDebrisFrame.setObjectName(u"floatingDebrisFrame")
        self.floatingDebrisFrame.setMaximumSize(QSize(16777215, 30))
        self.floatingDebrisFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.floatingDebrisFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.floatingDebrisFrame)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.floatingDebrisLabel = QLabel(self.floatingDebrisFrame)
        self.floatingDebrisLabel.setObjectName(u"floatingDebrisLabel")
        self.floatingDebrisLabel.setFont(font2)
        self.floatingDebrisLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_48.addWidget(self.floatingDebrisLabel)


        self.verticalLayout_4.addWidget(self.floatingDebrisFrame)

        self.altitudeHoldFrame = QFrame(self.indicatorsFrame)
        self.altitudeHoldFrame.setObjectName(u"altitudeHoldFrame")
        self.altitudeHoldFrame.setMaximumSize(QSize(16777215, 30))
        self.altitudeHoldFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.altitudeHoldFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.altitudeHoldFrame)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.altitudeHoldLabel = QLabel(self.altitudeHoldFrame)
        self.altitudeHoldLabel.setObjectName(u"altitudeHoldLabel")
        self.altitudeHoldLabel.setFont(font2)
        self.altitudeHoldLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_49.addWidget(self.altitudeHoldLabel)


        self.verticalLayout_4.addWidget(self.altitudeHoldFrame)

        self.stabilizeFrame = QFrame(self.indicatorsFrame)
        self.stabilizeFrame.setObjectName(u"stabilizeFrame")
        self.stabilizeFrame.setMaximumSize(QSize(16777215, 30))
        self.stabilizeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.stabilizeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.stabilizeFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.stabilizeFrameLabel = QLabel(self.stabilizeFrame)
        self.stabilizeFrameLabel.setObjectName(u"stabilizeFrameLabel")
        self.stabilizeFrameLabel.setFont(font2)
        self.stabilizeFrameLabel.setStyleSheet(u"")
        self.stabilizeFrameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.stabilizeFrameLabel)


        self.verticalLayout_4.addWidget(self.stabilizeFrame)


        self.verticalLayout_3.addWidget(self.indicatorsFrame)

        self.sensorReadingFrame = QFrame(self.homePageIndicatorFrame)
        self.sensorReadingFrame.setObjectName(u"sensorReadingFrame")
        self.sensorReadingFrame.setMaximumSize(QSize(16777215, 16777215))
        self.sensorReadingFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.sensorReadingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sensorReadingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.sensorReadingFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.rollFrame = QFrame(self.sensorReadingFrame)
        self.rollFrame.setObjectName(u"rollFrame")
        self.rollFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.rollFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rollFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.rollFrame)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.rollLabel = QLabel(self.rollFrame)
        self.rollLabel.setObjectName(u"rollLabel")
        self.rollLabel.setFont(font2)
        self.rollLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_88.addWidget(self.rollLabel)

        self.rollReadingLabel = QLabel(self.rollFrame)
        self.rollReadingLabel.setObjectName(u"rollReadingLabel")
        self.rollReadingLabel.setFont(font2)
        self.rollReadingLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_88.addWidget(self.rollReadingLabel)


        self.verticalLayout_9.addWidget(self.rollFrame)

        self.pitchFrame = QFrame(self.sensorReadingFrame)
        self.pitchFrame.setObjectName(u"pitchFrame")
        self.pitchFrame.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setBold(False)
        self.pitchFrame.setFont(font3)
        self.pitchFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.pitchFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pitchFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.pitchFrame)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.pitchLabel = QLabel(self.pitchFrame)
        self.pitchLabel.setObjectName(u"pitchLabel")
        self.pitchLabel.setFont(font2)
        self.pitchLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_81.addWidget(self.pitchLabel)

        self.pitchReadingLabel = QLabel(self.pitchFrame)
        self.pitchReadingLabel.setObjectName(u"pitchReadingLabel")
        self.pitchReadingLabel.setFont(font2)
        self.pitchReadingLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_81.addWidget(self.pitchReadingLabel)


        self.verticalLayout_9.addWidget(self.pitchFrame)

        self.gainFrame = QFrame(self.sensorReadingFrame)
        self.gainFrame.setObjectName(u"gainFrame")
        self.gainFrame.setMaximumSize(QSize(16777215, 30))
        self.gainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.gainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.gainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.gainFrame)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.gainLabel = QLabel(self.gainFrame)
        self.gainLabel.setObjectName(u"gainLabel")
        self.gainLabel.setFont(font2)
        self.gainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_53.addWidget(self.gainLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.gainReadingLabel = QLabel(self.gainFrame)
        self.gainReadingLabel.setObjectName(u"gainReadingLabel")
        self.gainReadingLabel.setFont(font2)
        self.gainReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_53.addWidget(self.gainReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.gainFrame)

        self.phSensorFrame = QFrame(self.sensorReadingFrame)
        self.phSensorFrame.setObjectName(u"phSensorFrame")
        self.phSensorFrame.setMaximumSize(QSize(16777215, 30))
        self.phSensorFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.phSensorFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.phSensorFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.phSensorFrame)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.phLael = QLabel(self.phSensorFrame)
        self.phLael.setObjectName(u"phLael")
        self.phLael.setFont(font2)
        self.phLael.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.phLael, 0, Qt.AlignmentFlag.AlignLeft)

        self.phSensorReadingLabel = QLabel(self.phSensorFrame)
        self.phSensorReadingLabel.setObjectName(u"phSensorReadingLabel")
        self.phSensorReadingLabel.setFont(font2)
        self.phSensorReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_50.addWidget(self.phSensorReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.phSensorFrame)

        self.headingFrame = QFrame(self.sensorReadingFrame)
        self.headingFrame.setObjectName(u"headingFrame")
        self.headingFrame.setMaximumSize(QSize(16777215, 30))
        self.headingFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.headingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.headingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.headingFrame)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.headingLabel = QLabel(self.headingFrame)
        self.headingLabel.setObjectName(u"headingLabel")
        self.headingLabel.setFont(font2)
        self.headingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.headingLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.headingReadingLabel = QLabel(self.headingFrame)
        self.headingReadingLabel.setObjectName(u"headingReadingLabel")
        self.headingReadingLabel.setFont(font2)
        self.headingReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_52.addWidget(self.headingReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.headingFrame)

        self.depthFrame = QFrame(self.sensorReadingFrame)
        self.depthFrame.setObjectName(u"depthFrame")
        self.depthFrame.setMaximumSize(QSize(16777215, 30))
        self.depthFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #6272A4;\n"
"}")
        self.depthFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.depthFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.depthFrame)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.depthLabel = QLabel(self.depthFrame)
        self.depthLabel.setObjectName(u"depthLabel")
        self.depthLabel.setFont(font2)
        self.depthLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_51.addWidget(self.depthLabel, 0, Qt.AlignmentFlag.AlignLeft)

        self.depthReadingLabel = QLabel(self.depthFrame)
        self.depthReadingLabel.setObjectName(u"depthReadingLabel")
        self.depthReadingLabel.setFont(font2)
        self.depthReadingLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_51.addWidget(self.depthReadingLabel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_9.addWidget(self.depthFrame)


        self.verticalLayout_3.addWidget(self.sensorReadingFrame, 0, Qt.AlignmentFlag.AlignBottom)


        self.horizontalLayout_12.addWidget(self.homePageIndicatorFrame)


        self.horizontalLayout_9.addWidget(self.homePageFrame)

        self.mainBodyStackedWidget.addWidget(self.homePage)
        self.ocrPage = QWidget()
        self.ocrPage.setObjectName(u"ocrPage")
        self.verticalLayout_24 = QVBoxLayout(self.ocrPage)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.mainOCRFrame = QFrame(self.ocrPage)
        self.mainOCRFrame.setObjectName(u"mainOCRFrame")
        self.mainOCRFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainOCRFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.mainOCRFrame)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.ocrResults = QLabel(self.mainOCRFrame)
        self.ocrResults.setObjectName(u"ocrResults")
        self.ocrResults.setMinimumSize(QSize(0, 100))
        self.ocrResults.setMaximumSize(QSize(16777215, 100))
        self.ocrResults.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_25.addWidget(self.ocrResults)

        self.ocrTextbox = QTextEdit(self.mainOCRFrame)
        self.ocrTextbox.setObjectName(u"ocrTextbox")
        self.ocrTextbox.setMinimumSize(QSize(0, 200))
        self.ocrTextbox.setMaximumSize(QSize(16777215, 200))
        font4 = QFont()
        font4.setPointSize(16)
        self.ocrTextbox.setFont(font4)
        self.ocrTextbox.setStyleSheet(u"background-color: rgb(248, 248, 242);")

        self.verticalLayout_25.addWidget(self.ocrTextbox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_3)


        self.verticalLayout_24.addWidget(self.mainOCRFrame)

        self.textSubmitFrame = QFrame(self.ocrPage)
        self.textSubmitFrame.setObjectName(u"textSubmitFrame")
        self.textSubmitFrame.setMinimumSize(QSize(0, 100))
        self.textSubmitFrame.setMaximumSize(QSize(16777215, 100))
        self.textSubmitFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.textSubmitFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.textSubmitFrame)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.ocrTextSubmitButton = QPushButton(self.textSubmitFrame)
        self.ocrTextSubmitButton.setObjectName(u"ocrTextSubmitButton")
        self.ocrTextSubmitButton.setMinimumSize(QSize(0, 100))
        self.ocrTextSubmitButton.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout_26.addWidget(self.ocrTextSubmitButton)


        self.verticalLayout_24.addWidget(self.textSubmitFrame)

        self.mainBodyStackedWidget.addWidget(self.ocrPage)
        self.cameraSettingsPage = QWidget()
        self.cameraSettingsPage.setObjectName(u"cameraSettingsPage")
        self.cameraSettingsPage.setStyleSheet(u"")
        self.horizontalLayout_11 = QHBoxLayout(self.cameraSettingsPage)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.cameraSettingsPageFrame = QFrame(self.cameraSettingsPage)
        self.cameraSettingsPageFrame.setObjectName(u"cameraSettingsPageFrame")
        self.cameraSettingsPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraSettingsPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.cameraSettingsPageFrame)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.cameraSettingsCameraMappingFrame = QFrame(self.cameraSettingsPageFrame)
        self.cameraSettingsCameraMappingFrame.setObjectName(u"cameraSettingsCameraMappingFrame")
        self.cameraSettingsCameraMappingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraSettingsCameraMappingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.cameraSettingsCameraMappingFrame)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.cameraSettingsScrollArea = QScrollArea(self.cameraSettingsCameraMappingFrame)
        self.cameraSettingsScrollArea.setObjectName(u"cameraSettingsScrollArea")
        self.cameraSettingsScrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #282A36;\n"
"}\n"
"")
        self.cameraSettingsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1789, 1258))
        self.horizontalLayout_77 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.cameraSettingsCameraMappingFrameInScrollArea = QFrame(self.scrollAreaWidgetContents_2)
        self.cameraSettingsCameraMappingFrameInScrollArea.setObjectName(u"cameraSettingsCameraMappingFrameInScrollArea")
        self.cameraSettingsCameraMappingFrameInScrollArea.setStyleSheet(u"QComboBox{ \n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"} \n"
"\n"
"QComboBox::drop-down { \n"
"	border: 3px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QComboBox::on {\n"
"border: 3px solid #FFB86C;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	border: 3px solid #FFB86C;\n"
"	color: #282A36;\n"
"	background-color: #FFB86C;\n"
"} \n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #FFB86C;\n"
"	background-color: #F1FA8C;\n"
"    selection-background-color: #FFB86C;\n"
"    selection-color: #282A36;\n"
"}\n"
"\n"
"QComboBox QListView::item::selected { \n"
"	border-radius: 5px; \n"
"	border: 3px solid #FFB86C;\n"
"	color: #282A36;\n"
"	background-color: #FFB86C;\n"
"}")
        self.cameraSettingsCameraMappingFrameInScrollArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.cameraSettingsCameraMappingFrameInScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.OAKCameraLocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.OAKCameraLocationFrame.setObjectName(u"OAKCameraLocationFrame")
        self.OAKCameraLocationFrame.setMaximumSize(QSize(16777215, 125))
        self.OAKCameraLocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.OAKCameraLocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.OAKCameraLocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.OAKCameraLocationFrame)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.OAKCameraLocationLabel = QLabel(self.OAKCameraLocationFrame)
        self.OAKCameraLocationLabel.setObjectName(u"OAKCameraLocationLabel")
        self.OAKCameraLocationLabel.setMaximumSize(QSize(400, 100))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.OAKCameraLocationLabel.setFont(font5)

        self.horizontalLayout_80.addWidget(self.OAKCameraLocationLabel)

        self.OAKCameraLocationComboBox = QComboBox(self.OAKCameraLocationFrame)
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.addItem("")
        self.OAKCameraLocationComboBox.setObjectName(u"OAKCameraLocationComboBox")
        self.OAKCameraLocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.OAKCameraLocationComboBox.setFont(font5)
        self.OAKCameraLocationComboBox.setStyleSheet(u"")
        self.OAKCameraLocationComboBox.setEditable(False)

        self.horizontalLayout_80.addWidget(self.OAKCameraLocationComboBox)


        self.verticalLayout_22.addWidget(self.OAKCameraLocationFrame)

        self.RTSPCAMERA1LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA1LocationFrame.setObjectName(u"RTSPCAMERA1LocationFrame")
        self.RTSPCAMERA1LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA1LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA1LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA1LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.RTSPCAMERA1LocationFrame)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.RTSPCAMERA1LocationLabel = QLabel(self.RTSPCAMERA1LocationFrame)
        self.RTSPCAMERA1LocationLabel.setObjectName(u"RTSPCAMERA1LocationLabel")
        self.RTSPCAMERA1LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA1LocationLabel.setFont(font5)

        self.horizontalLayout_78.addWidget(self.RTSPCAMERA1LocationLabel)

        self.RTSPCAMERA1LocationComboBox = QComboBox(self.RTSPCAMERA1LocationFrame)
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.addItem("")
        self.RTSPCAMERA1LocationComboBox.setObjectName(u"RTSPCAMERA1LocationComboBox")
        self.RTSPCAMERA1LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA1LocationComboBox.setFont(font5)
        self.RTSPCAMERA1LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA1LocationComboBox.setEditable(False)

        self.horizontalLayout_78.addWidget(self.RTSPCAMERA1LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA1LocationFrame)

        self.RTSPCAMERA2LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA2LocationFrame.setObjectName(u"RTSPCAMERA2LocationFrame")
        self.RTSPCAMERA2LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA2LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA2LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA2LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.RTSPCAMERA2LocationFrame)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.RTSPCAMERA2LocationLabel = QLabel(self.RTSPCAMERA2LocationFrame)
        self.RTSPCAMERA2LocationLabel.setObjectName(u"RTSPCAMERA2LocationLabel")
        self.RTSPCAMERA2LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA2LocationLabel.setFont(font5)

        self.horizontalLayout_93.addWidget(self.RTSPCAMERA2LocationLabel)

        self.RTSPCAMERA2LocationComboBox = QComboBox(self.RTSPCAMERA2LocationFrame)
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.addItem("")
        self.RTSPCAMERA2LocationComboBox.setObjectName(u"RTSPCAMERA2LocationComboBox")
        self.RTSPCAMERA2LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA2LocationComboBox.setFont(font5)
        self.RTSPCAMERA2LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA2LocationComboBox.setEditable(False)

        self.horizontalLayout_93.addWidget(self.RTSPCAMERA2LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA2LocationFrame)

        self.RTSPCAMERA3LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA3LocationFrame.setObjectName(u"RTSPCAMERA3LocationFrame")
        self.RTSPCAMERA3LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA3LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA3LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA3LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.RTSPCAMERA3LocationFrame)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.RTSPCAMERA3LocationLabel = QLabel(self.RTSPCAMERA3LocationFrame)
        self.RTSPCAMERA3LocationLabel.setObjectName(u"RTSPCAMERA3LocationLabel")
        self.RTSPCAMERA3LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA3LocationLabel.setFont(font5)

        self.horizontalLayout_95.addWidget(self.RTSPCAMERA3LocationLabel)

        self.RTSPCAMERA3LocationComboBox = QComboBox(self.RTSPCAMERA3LocationFrame)
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.addItem("")
        self.RTSPCAMERA3LocationComboBox.setObjectName(u"RTSPCAMERA3LocationComboBox")
        self.RTSPCAMERA3LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA3LocationComboBox.setFont(font5)
        self.RTSPCAMERA3LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA3LocationComboBox.setEditable(False)

        self.horizontalLayout_95.addWidget(self.RTSPCAMERA3LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA3LocationFrame)

        self.RTSPCAMERA4LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA4LocationFrame.setObjectName(u"RTSPCAMERA4LocationFrame")
        self.RTSPCAMERA4LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA4LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA4LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA4LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.RTSPCAMERA4LocationFrame)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.RTSPCAMERA4LocationLabel = QLabel(self.RTSPCAMERA4LocationFrame)
        self.RTSPCAMERA4LocationLabel.setObjectName(u"RTSPCAMERA4LocationLabel")
        self.RTSPCAMERA4LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA4LocationLabel.setFont(font5)

        self.horizontalLayout_83.addWidget(self.RTSPCAMERA4LocationLabel)

        self.RTSPCAMERA4LocationComboBox = QComboBox(self.RTSPCAMERA4LocationFrame)
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.addItem("")
        self.RTSPCAMERA4LocationComboBox.setObjectName(u"RTSPCAMERA4LocationComboBox")
        self.RTSPCAMERA4LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA4LocationComboBox.setFont(font5)
        self.RTSPCAMERA4LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA4LocationComboBox.setEditable(False)

        self.horizontalLayout_83.addWidget(self.RTSPCAMERA4LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA4LocationFrame)

        self.RTSPCAMERA5LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA5LocationFrame.setObjectName(u"RTSPCAMERA5LocationFrame")
        self.RTSPCAMERA5LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA5LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA5LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA5LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.RTSPCAMERA5LocationFrame)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.RTSPCAMERA5LocationLabel = QLabel(self.RTSPCAMERA5LocationFrame)
        self.RTSPCAMERA5LocationLabel.setObjectName(u"RTSPCAMERA5LocationLabel")
        self.RTSPCAMERA5LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA5LocationLabel.setFont(font5)

        self.horizontalLayout_97.addWidget(self.RTSPCAMERA5LocationLabel)

        self.RTSPCAMERA5LocationComboBox = QComboBox(self.RTSPCAMERA5LocationFrame)
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.addItem("")
        self.RTSPCAMERA5LocationComboBox.setObjectName(u"RTSPCAMERA5LocationComboBox")
        self.RTSPCAMERA5LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA5LocationComboBox.setFont(font5)
        self.RTSPCAMERA5LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA5LocationComboBox.setEditable(False)

        self.horizontalLayout_97.addWidget(self.RTSPCAMERA5LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA5LocationFrame)

        self.RTSPCAMERA6LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA6LocationFrame.setObjectName(u"RTSPCAMERA6LocationFrame")
        self.RTSPCAMERA6LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA6LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA6LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA6LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.RTSPCAMERA6LocationFrame)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.RTSPCAMERA6LocationLabel = QLabel(self.RTSPCAMERA6LocationFrame)
        self.RTSPCAMERA6LocationLabel.setObjectName(u"RTSPCAMERA6LocationLabel")
        self.RTSPCAMERA6LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA6LocationLabel.setFont(font5)

        self.horizontalLayout_91.addWidget(self.RTSPCAMERA6LocationLabel)

        self.RTSPCAMERA6LocationComboBox = QComboBox(self.RTSPCAMERA6LocationFrame)
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.addItem("")
        self.RTSPCAMERA6LocationComboBox.setObjectName(u"RTSPCAMERA6LocationComboBox")
        self.RTSPCAMERA6LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA6LocationComboBox.setFont(font5)
        self.RTSPCAMERA6LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA6LocationComboBox.setEditable(False)

        self.horizontalLayout_91.addWidget(self.RTSPCAMERA6LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA6LocationFrame)

        self.RTSPCAMERA7LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA7LocationFrame.setObjectName(u"RTSPCAMERA7LocationFrame")
        self.RTSPCAMERA7LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA7LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA7LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA7LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.RTSPCAMERA7LocationFrame)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.RTSPCAMERA7LocationLabel = QLabel(self.RTSPCAMERA7LocationFrame)
        self.RTSPCAMERA7LocationLabel.setObjectName(u"RTSPCAMERA7LocationLabel")
        self.RTSPCAMERA7LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA7LocationLabel.setFont(font5)

        self.horizontalLayout_85.addWidget(self.RTSPCAMERA7LocationLabel)

        self.RTSPCAMERA7LocationComboBox = QComboBox(self.RTSPCAMERA7LocationFrame)
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.addItem("")
        self.RTSPCAMERA7LocationComboBox.setObjectName(u"RTSPCAMERA7LocationComboBox")
        self.RTSPCAMERA7LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA7LocationComboBox.setFont(font5)
        self.RTSPCAMERA7LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA7LocationComboBox.setEditable(False)

        self.horizontalLayout_85.addWidget(self.RTSPCAMERA7LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA7LocationFrame)

        self.RTSPCAMERA8LocationFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA8LocationFrame.setObjectName(u"RTSPCAMERA8LocationFrame")
        self.RTSPCAMERA8LocationFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA8LocationFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA8LocationFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA8LocationFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.RTSPCAMERA8LocationFrame)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.RTSPCAMERA8LocationLabel = QLabel(self.RTSPCAMERA8LocationFrame)
        self.RTSPCAMERA8LocationLabel.setObjectName(u"RTSPCAMERA8LocationLabel")
        self.RTSPCAMERA8LocationLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA8LocationLabel.setFont(font5)

        self.horizontalLayout_87.addWidget(self.RTSPCAMERA8LocationLabel)

        self.RTSPCAMERA8LocationComboBox = QComboBox(self.RTSPCAMERA8LocationFrame)
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.addItem("")
        self.RTSPCAMERA8LocationComboBox.setObjectName(u"RTSPCAMERA8LocationComboBox")
        self.RTSPCAMERA8LocationComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTSPCAMERA8LocationComboBox.setFont(font5)
        self.RTSPCAMERA8LocationComboBox.setStyleSheet(u"")
        self.RTSPCAMERA8LocationComboBox.setEditable(False)

        self.horizontalLayout_87.addWidget(self.RTSPCAMERA8LocationComboBox)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA8LocationFrame)

        self.RTSPCAMERA1SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA1SourceFrame.setObjectName(u"RTSPCAMERA1SourceFrame")
        self.RTSPCAMERA1SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA1SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA1SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA1SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.RTSPCAMERA1SourceFrame)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.RTSPCAMERA1SourceLabel = QLabel(self.RTSPCAMERA1SourceFrame)
        self.RTSPCAMERA1SourceLabel.setObjectName(u"RTSPCAMERA1SourceLabel")
        self.RTSPCAMERA1SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA1SourceLabel.setFont(font5)

        self.horizontalLayout_79.addWidget(self.RTSPCAMERA1SourceLabel)

        self.lineEditRTSPCAMERA1SourceText = QLineEdit(self.RTSPCAMERA1SourceFrame)
        self.lineEditRTSPCAMERA1SourceText.setObjectName(u"lineEditRTSPCAMERA1SourceText")
        self.lineEditRTSPCAMERA1SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA1SourceText.setFont(font5)
        self.lineEditRTSPCAMERA1SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_79.addWidget(self.lineEditRTSPCAMERA1SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA1SourceFrame)

        self.RTSPCAMERA2SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA2SourceFrame.setObjectName(u"RTSPCAMERA2SourceFrame")
        self.RTSPCAMERA2SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA2SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA2SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA2SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.RTSPCAMERA2SourceFrame)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.RTSPCAMERA2SourceLabel = QLabel(self.RTSPCAMERA2SourceFrame)
        self.RTSPCAMERA2SourceLabel.setObjectName(u"RTSPCAMERA2SourceLabel")
        self.RTSPCAMERA2SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA2SourceLabel.setFont(font5)

        self.horizontalLayout_92.addWidget(self.RTSPCAMERA2SourceLabel)

        self.lineEditRTSPCAMERA2SourceText = QLineEdit(self.RTSPCAMERA2SourceFrame)
        self.lineEditRTSPCAMERA2SourceText.setObjectName(u"lineEditRTSPCAMERA2SourceText")
        self.lineEditRTSPCAMERA2SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA2SourceText.setFont(font5)
        self.lineEditRTSPCAMERA2SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_92.addWidget(self.lineEditRTSPCAMERA2SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA2SourceFrame)

        self.RTSPCAMERA3SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA3SourceFrame.setObjectName(u"RTSPCAMERA3SourceFrame")
        self.RTSPCAMERA3SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA3SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA3SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA3SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.RTSPCAMERA3SourceFrame)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.RTSPCAMERA3SourceLabel = QLabel(self.RTSPCAMERA3SourceFrame)
        self.RTSPCAMERA3SourceLabel.setObjectName(u"RTSPCAMERA3SourceLabel")
        self.RTSPCAMERA3SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA3SourceLabel.setFont(font5)

        self.horizontalLayout_94.addWidget(self.RTSPCAMERA3SourceLabel)

        self.lineEditRTSPCAMERA3SourceText = QLineEdit(self.RTSPCAMERA3SourceFrame)
        self.lineEditRTSPCAMERA3SourceText.setObjectName(u"lineEditRTSPCAMERA3SourceText")
        self.lineEditRTSPCAMERA3SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA3SourceText.setFont(font5)
        self.lineEditRTSPCAMERA3SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_94.addWidget(self.lineEditRTSPCAMERA3SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA3SourceFrame)

        self.RTSPCAMERA4SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA4SourceFrame.setObjectName(u"RTSPCAMERA4SourceFrame")
        self.RTSPCAMERA4SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA4SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA4SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA4SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.RTSPCAMERA4SourceFrame)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.RTSPCAMERA4SourceLabel = QLabel(self.RTSPCAMERA4SourceFrame)
        self.RTSPCAMERA4SourceLabel.setObjectName(u"RTSPCAMERA4SourceLabel")
        self.RTSPCAMERA4SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA4SourceLabel.setFont(font5)

        self.horizontalLayout_82.addWidget(self.RTSPCAMERA4SourceLabel)

        self.lineEditRTSPCAMERA4SourceText = QLineEdit(self.RTSPCAMERA4SourceFrame)
        self.lineEditRTSPCAMERA4SourceText.setObjectName(u"lineEditRTSPCAMERA4SourceText")
        self.lineEditRTSPCAMERA4SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA4SourceText.setFont(font5)
        self.lineEditRTSPCAMERA4SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_82.addWidget(self.lineEditRTSPCAMERA4SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA4SourceFrame)

        self.RTSPCAMERA5SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA5SourceFrame.setObjectName(u"RTSPCAMERA5SourceFrame")
        self.RTSPCAMERA5SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA5SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA5SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA5SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.RTSPCAMERA5SourceFrame)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.RTSPCAMERA5SourceLabel = QLabel(self.RTSPCAMERA5SourceFrame)
        self.RTSPCAMERA5SourceLabel.setObjectName(u"RTSPCAMERA5SourceLabel")
        self.RTSPCAMERA5SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA5SourceLabel.setFont(font5)

        self.horizontalLayout_96.addWidget(self.RTSPCAMERA5SourceLabel)

        self.lineEditRTSPCAMERA5SourceText = QLineEdit(self.RTSPCAMERA5SourceFrame)
        self.lineEditRTSPCAMERA5SourceText.setObjectName(u"lineEditRTSPCAMERA5SourceText")
        self.lineEditRTSPCAMERA5SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA5SourceText.setFont(font5)
        self.lineEditRTSPCAMERA5SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_96.addWidget(self.lineEditRTSPCAMERA5SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA5SourceFrame)

        self.RTSPCAMERA6SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA6SourceFrame.setObjectName(u"RTSPCAMERA6SourceFrame")
        self.RTSPCAMERA6SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA6SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA6SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA6SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.RTSPCAMERA6SourceFrame)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.RTSPCAMERA6SourceLabel = QLabel(self.RTSPCAMERA6SourceFrame)
        self.RTSPCAMERA6SourceLabel.setObjectName(u"RTSPCAMERA6SourceLabel")
        self.RTSPCAMERA6SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA6SourceLabel.setFont(font5)

        self.horizontalLayout_90.addWidget(self.RTSPCAMERA6SourceLabel)

        self.lineEditRTSPCAMERA6SourceText = QLineEdit(self.RTSPCAMERA6SourceFrame)
        self.lineEditRTSPCAMERA6SourceText.setObjectName(u"lineEditRTSPCAMERA6SourceText")
        self.lineEditRTSPCAMERA6SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA6SourceText.setFont(font5)
        self.lineEditRTSPCAMERA6SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_90.addWidget(self.lineEditRTSPCAMERA6SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA6SourceFrame)

        self.RTSPCAMERA7SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA7SourceFrame.setObjectName(u"RTSPCAMERA7SourceFrame")
        self.RTSPCAMERA7SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA7SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA7SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA7SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.RTSPCAMERA7SourceFrame)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.RTSPCAMERA7SourceLabel = QLabel(self.RTSPCAMERA7SourceFrame)
        self.RTSPCAMERA7SourceLabel.setObjectName(u"RTSPCAMERA7SourceLabel")
        self.RTSPCAMERA7SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA7SourceLabel.setFont(font5)

        self.horizontalLayout_84.addWidget(self.RTSPCAMERA7SourceLabel)

        self.lineEditRTSPCAMERA7SourceText = QLineEdit(self.RTSPCAMERA7SourceFrame)
        self.lineEditRTSPCAMERA7SourceText.setObjectName(u"lineEditRTSPCAMERA7SourceText")
        self.lineEditRTSPCAMERA7SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA7SourceText.setFont(font5)
        self.lineEditRTSPCAMERA7SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_84.addWidget(self.lineEditRTSPCAMERA7SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA7SourceFrame)

        self.RTSPCAMERA8SourceFrame = QFrame(self.cameraSettingsCameraMappingFrameInScrollArea)
        self.RTSPCAMERA8SourceFrame.setObjectName(u"RTSPCAMERA8SourceFrame")
        self.RTSPCAMERA8SourceFrame.setMaximumSize(QSize(16777215, 125))
        self.RTSPCAMERA8SourceFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTSPCAMERA8SourceFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTSPCAMERA8SourceFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.RTSPCAMERA8SourceFrame)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.RTSPCAMERA8SourceLabel = QLabel(self.RTSPCAMERA8SourceFrame)
        self.RTSPCAMERA8SourceLabel.setObjectName(u"RTSPCAMERA8SourceLabel")
        self.RTSPCAMERA8SourceLabel.setMaximumSize(QSize(400, 100))
        self.RTSPCAMERA8SourceLabel.setFont(font5)

        self.horizontalLayout_86.addWidget(self.RTSPCAMERA8SourceLabel)

        self.lineEditRTSPCAMERA8SourceText = QLineEdit(self.RTSPCAMERA8SourceFrame)
        self.lineEditRTSPCAMERA8SourceText.setObjectName(u"lineEditRTSPCAMERA8SourceText")
        self.lineEditRTSPCAMERA8SourceText.setMaximumSize(QSize(16777215, 50))
        self.lineEditRTSPCAMERA8SourceText.setFont(font5)
        self.lineEditRTSPCAMERA8SourceText.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QLineEdit::hover{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border: 2px solid #FFB86C;\n"
"	background-color: #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_86.addWidget(self.lineEditRTSPCAMERA8SourceText)


        self.verticalLayout_22.addWidget(self.RTSPCAMERA8SourceFrame)


        self.horizontalLayout_77.addWidget(self.cameraSettingsCameraMappingFrameInScrollArea)

        self.cameraSettingsScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_76.addWidget(self.cameraSettingsScrollArea)


        self.verticalLayout_21.addWidget(self.cameraSettingsCameraMappingFrame)

        self.saveCameraSettingFrame = QFrame(self.cameraSettingsPageFrame)
        self.saveCameraSettingFrame.setObjectName(u"saveCameraSettingFrame")
        self.saveCameraSettingFrame.setMinimumSize(QSize(0, 0))
        self.saveCameraSettingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.saveCameraSettingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.saveCameraSettingFrame)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.saveCameraSettingButton = QPushButton(self.saveCameraSettingFrame)
        self.saveCameraSettingButton.setObjectName(u"saveCameraSettingButton")
        self.saveCameraSettingButton.setStyleSheet(u"QPushButton{\n"
"	font-size: 20px;\n"
"	border-radius: 5px; \n"
"	border: 3px solid #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_98.addWidget(self.saveCameraSettingButton)


        self.verticalLayout_21.addWidget(self.saveCameraSettingFrame)


        self.horizontalLayout_11.addWidget(self.cameraSettingsPageFrame)

        self.mainBodyStackedWidget.addWidget(self.cameraSettingsPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.horizontalLayout_8 = QHBoxLayout(self.settingsPage)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.settingsPageFrame = QFrame(self.settingsPage)
        self.settingsPageFrame.setObjectName(u"settingsPageFrame")
        self.settingsPageFrame.setStyleSheet(u"")
        self.settingsPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.settingsPageFrame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.settingsPageControllerSettingsFrame = QFrame(self.settingsPageFrame)
        self.settingsPageControllerSettingsFrame.setObjectName(u"settingsPageControllerSettingsFrame")
        self.settingsPageControllerSettingsFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.settingsPageControllerSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageControllerSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.settingsPageControllerSettingsFrame)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsButton = QPushButton(self.settingsPageControllerSettingsFrame)
        self.controllerSettingsButton.setObjectName(u"controllerSettingsButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.controllerSettingsButton.sizePolicy().hasHeightForWidth())
        self.controllerSettingsButton.setSizePolicy(sizePolicy4)
        self.controllerSettingsButton.setStyleSheet(u"QPushButton{\n"
"	image: url(:/controllerImage/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Control Screen/Solid/Control Solid Inv 4k.png);\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.controllerSettingsButton)


        self.verticalLayout_5.addWidget(self.settingsPageControllerSettingsFrame)

        self.settingsPageCameraSettingsFrame = QFrame(self.settingsPageFrame)
        self.settingsPageCameraSettingsFrame.setObjectName(u"settingsPageCameraSettingsFrame")
        self.settingsPageCameraSettingsFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.settingsPageCameraSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageCameraSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.settingsPageCameraSettingsFrame)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.cameraSettingsButton = QPushButton(self.settingsPageCameraSettingsFrame)
        self.cameraSettingsButton.setObjectName(u"cameraSettingsButton")
        sizePolicy4.setHeightForWidth(self.cameraSettingsButton.sizePolicy().hasHeightForWidth())
        self.cameraSettingsButton.setSizePolicy(sizePolicy4)
        self.cameraSettingsButton.setFont(font1)

        self.horizontalLayout_75.addWidget(self.cameraSettingsButton)


        self.verticalLayout_5.addWidget(self.settingsPageCameraSettingsFrame)

        self.settingsPageGeneralSettingsFrame = QFrame(self.settingsPageFrame)
        self.settingsPageGeneralSettingsFrame.setObjectName(u"settingsPageGeneralSettingsFrame")
        self.settingsPageGeneralSettingsFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}\n"
"")
        self.settingsPageGeneralSettingsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.settingsPageGeneralSettingsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.settingsPageGeneralSettingsFrame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.generalSettingsButton = QPushButton(self.settingsPageGeneralSettingsFrame)
        self.generalSettingsButton.setObjectName(u"generalSettingsButton")
        sizePolicy4.setHeightForWidth(self.generalSettingsButton.sizePolicy().hasHeightForWidth())
        self.generalSettingsButton.setSizePolicy(sizePolicy4)
        self.generalSettingsButton.setFont(font1)

        self.horizontalLayout_18.addWidget(self.generalSettingsButton)


        self.verticalLayout_5.addWidget(self.settingsPageGeneralSettingsFrame)


        self.horizontalLayout_8.addWidget(self.settingsPageFrame)

        self.mainBodyStackedWidget.addWidget(self.settingsPage)
        self.controllerSettingsPage = QWidget()
        self.controllerSettingsPage.setObjectName(u"controllerSettingsPage")
        self.controllerSettingsPage.setStyleSheet(u"")
        self.horizontalLayout_10 = QHBoxLayout(self.controllerSettingsPage)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsPageFrame = QFrame(self.controllerSettingsPage)
        self.controllerSettingsPageFrame.setObjectName(u"controllerSettingsPageFrame")
        self.controllerSettingsPageFrame.setStyleSheet(u"")
        self.controllerSettingsPageFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerSettingsPageFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.controllerSettingsPageFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsJoystickMappingFrame = QFrame(self.controllerSettingsPageFrame)
        self.controllerSettingsJoystickMappingFrame.setObjectName(u"controllerSettingsJoystickMappingFrame")
        self.controllerSettingsJoystickMappingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerSettingsJoystickMappingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.controllerSettingsJoystickMappingFrame)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsScrollArea = QScrollArea(self.controllerSettingsJoystickMappingFrame)
        self.controllerSettingsScrollArea.setObjectName(u"controllerSettingsScrollArea")
        self.controllerSettingsScrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: 1px solid #282A36;\n"
"}\n"
"")
        self.controllerSettingsScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -1787, 1789, 2768))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.controllerSettingsJoystickMappingFrameInScrollArea = QFrame(self.scrollAreaWidgetContents)
        self.controllerSettingsJoystickMappingFrameInScrollArea.setObjectName(u"controllerSettingsJoystickMappingFrameInScrollArea")
        self.controllerSettingsJoystickMappingFrameInScrollArea.setStyleSheet(u"QComboBox{ \n"
"	border-radius: 5px; \n"
"	border: 2px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"} \n"
"\n"
"QComboBox::drop-down { \n"
"	border: 3px solid #F1FA8C;\n"
"	color: #282A36;\n"
"	background-color: #F1FA8C;\n"
"}\n"
"\n"
"QComboBox::on {\n"
"border: 3px solid #FFB86C;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"	border: 3px solid #FFB86C;\n"
"	color: #282A36;\n"
"	background-color: #FFB86C;\n"
"} \n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid #FFB86C;\n"
"	background-color: #F1FA8C;\n"
"    selection-background-color: #FFB86C;\n"
"    selection-color: #282A36;\n"
"}\n"
"\n"
"QComboBox QListView::item::selected { \n"
"	border-radius: 5px; \n"
"	border: 3px solid #FFB86C;\n"
"	color: #282A36;\n"
"	background-color: #FFB86C;\n"
"}")
        self.controllerSettingsJoystickMappingFrameInScrollArea.setFrameShape(QFrame.Shape.StyledPanel)
        self.controllerSettingsJoystickMappingFrameInScrollArea.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.AButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.AButtonFrame.setObjectName(u"AButtonFrame")
        self.AButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.AButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.AButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.AButtonFrame)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.AButtonLabel = QLabel(self.AButtonFrame)
        self.AButtonLabel.setObjectName(u"AButtonLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.AButtonLabel.sizePolicy().hasHeightForWidth())
        self.AButtonLabel.setSizePolicy(sizePolicy5)
        self.AButtonLabel.setMaximumSize(QSize(100, 100))
        self.AButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/A.svg"))
        self.AButtonLabel.setScaledContents(True)

        self.horizontalLayout_46.addWidget(self.AButtonLabel)

        self.AButtonComboBox = QComboBox(self.AButtonFrame)
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.addItem("")
        self.AButtonComboBox.setObjectName(u"AButtonComboBox")
        self.AButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.AButtonComboBox.setFont(font5)
        self.AButtonComboBox.setEditable(False)

        self.horizontalLayout_46.addWidget(self.AButtonComboBox)


        self.verticalLayout_7.addWidget(self.AButtonFrame)

        self.BButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.BButtonFrame.setObjectName(u"BButtonFrame")
        self.BButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.BButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.BButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.BButtonFrame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.BButtonLabel = QLabel(self.BButtonFrame)
        self.BButtonLabel.setObjectName(u"BButtonLabel")
        sizePolicy5.setHeightForWidth(self.BButtonLabel.sizePolicy().hasHeightForWidth())
        self.BButtonLabel.setSizePolicy(sizePolicy5)
        self.BButtonLabel.setMaximumSize(QSize(100, 100))
        self.BButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/B.svg"))
        self.BButtonLabel.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.BButtonLabel)

        self.BButtonComboBox = QComboBox(self.BButtonFrame)
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.addItem("")
        self.BButtonComboBox.setObjectName(u"BButtonComboBox")
        self.BButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.BButtonComboBox.setFont(font5)
        self.BButtonComboBox.setEditable(False)

        self.horizontalLayout_22.addWidget(self.BButtonComboBox)


        self.verticalLayout_7.addWidget(self.BButtonFrame)

        self.YButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.YButtonFrame.setObjectName(u"YButtonFrame")
        self.YButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.YButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.YButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.YButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.YButtonFrame)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.YButtonLabel = QLabel(self.YButtonFrame)
        self.YButtonLabel.setObjectName(u"YButtonLabel")
        sizePolicy5.setHeightForWidth(self.YButtonLabel.sizePolicy().hasHeightForWidth())
        self.YButtonLabel.setSizePolicy(sizePolicy5)
        self.YButtonLabel.setMaximumSize(QSize(100, 100))
        self.YButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Y.svg"))
        self.YButtonLabel.setScaledContents(True)

        self.horizontalLayout_41.addWidget(self.YButtonLabel)

        self.YButtonComboBox = QComboBox(self.YButtonFrame)
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.addItem("")
        self.YButtonComboBox.setObjectName(u"YButtonComboBox")
        self.YButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.YButtonComboBox.setFont(font5)

        self.horizontalLayout_41.addWidget(self.YButtonComboBox)


        self.verticalLayout_7.addWidget(self.YButtonFrame)

        self.XButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.XButtonFrame.setObjectName(u"XButtonFrame")
        self.XButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.XButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.XButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.XButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.XButtonFrame)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.XButtonLabel = QLabel(self.XButtonFrame)
        self.XButtonLabel.setObjectName(u"XButtonLabel")
        sizePolicy5.setHeightForWidth(self.XButtonLabel.sizePolicy().hasHeightForWidth())
        self.XButtonLabel.setSizePolicy(sizePolicy5)
        self.XButtonLabel.setMaximumSize(QSize(100, 100))
        self.XButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/X.svg"))
        self.XButtonLabel.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.XButtonLabel)

        self.XButtonComboBox = QComboBox(self.XButtonFrame)
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.addItem("")
        self.XButtonComboBox.setObjectName(u"XButtonComboBox")
        self.XButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.XButtonComboBox.setFont(font5)

        self.horizontalLayout_31.addWidget(self.XButtonComboBox)


        self.verticalLayout_7.addWidget(self.XButtonFrame)

        self.LBButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.LBButtonFrame.setObjectName(u"LBButtonFrame")
        self.LBButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.LBButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LBButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LBButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.LBButtonFrame)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.LBButtonLabel = QLabel(self.LBButtonFrame)
        self.LBButtonLabel.setObjectName(u"LBButtonLabel")
        sizePolicy5.setHeightForWidth(self.LBButtonLabel.sizePolicy().hasHeightForWidth())
        self.LBButtonLabel.setSizePolicy(sizePolicy5)
        self.LBButtonLabel.setMaximumSize(QSize(100, 100))
        self.LBButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Bumper.svg"))
        self.LBButtonLabel.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.LBButtonLabel)

        self.LBButtonComboBox = QComboBox(self.LBButtonFrame)
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.addItem("")
        self.LBButtonComboBox.setObjectName(u"LBButtonComboBox")
        self.LBButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.LBButtonComboBox.setFont(font5)

        self.horizontalLayout_23.addWidget(self.LBButtonComboBox)


        self.verticalLayout_7.addWidget(self.LBButtonFrame)

        self.RBButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.RBButtonFrame.setObjectName(u"RBButtonFrame")
        self.RBButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.RBButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RBButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RBButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.RBButtonFrame)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.RBButtonLabel = QLabel(self.RBButtonFrame)
        self.RBButtonLabel.setObjectName(u"RBButtonLabel")
        sizePolicy5.setHeightForWidth(self.RBButtonLabel.sizePolicy().hasHeightForWidth())
        self.RBButtonLabel.setSizePolicy(sizePolicy5)
        self.RBButtonLabel.setMaximumSize(QSize(100, 100))
        self.RBButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Bumper.svg"))
        self.RBButtonLabel.setScaledContents(True)

        self.horizontalLayout_38.addWidget(self.RBButtonLabel)

        self.RBButtonComboBox = QComboBox(self.RBButtonFrame)
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.addItem("")
        self.RBButtonComboBox.setObjectName(u"RBButtonComboBox")
        self.RBButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.RBButtonComboBox.setFont(font5)

        self.horizontalLayout_38.addWidget(self.RBButtonComboBox)


        self.verticalLayout_7.addWidget(self.RBButtonFrame)

        self.STARTButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.STARTButtonFrame.setObjectName(u"STARTButtonFrame")
        self.STARTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.STARTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.STARTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.STARTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.STARTButtonFrame)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.STARTButtonLabel = QLabel(self.STARTButtonFrame)
        self.STARTButtonLabel.setObjectName(u"STARTButtonLabel")
        sizePolicy5.setHeightForWidth(self.STARTButtonLabel.sizePolicy().hasHeightForWidth())
        self.STARTButtonLabel.setSizePolicy(sizePolicy5)
        self.STARTButtonLabel.setMaximumSize(QSize(100, 100))
        self.STARTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Menu.svg"))
        self.STARTButtonLabel.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.STARTButtonLabel)

        self.STARTButtonComboBox = QComboBox(self.STARTButtonFrame)
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.addItem("")
        self.STARTButtonComboBox.setObjectName(u"STARTButtonComboBox")
        self.STARTButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.STARTButtonComboBox.setFont(font5)

        self.horizontalLayout_28.addWidget(self.STARTButtonComboBox)


        self.verticalLayout_7.addWidget(self.STARTButtonFrame)

        self.BACKButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.BACKButtonFrame.setObjectName(u"BACKButtonFrame")
        self.BACKButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.BACKButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.BACKButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.BACKButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.BACKButtonFrame)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.BACKButtonLabel = QLabel(self.BACKButtonFrame)
        self.BACKButtonLabel.setObjectName(u"BACKButtonLabel")
        sizePolicy5.setHeightForWidth(self.BACKButtonLabel.sizePolicy().hasHeightForWidth())
        self.BACKButtonLabel.setSizePolicy(sizePolicy5)
        self.BACKButtonLabel.setMaximumSize(QSize(100, 100))
        self.BACKButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/View.svg"))
        self.BACKButtonLabel.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.BACKButtonLabel)

        self.BACKButtonComboBox = QComboBox(self.BACKButtonFrame)
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.addItem("")
        self.BACKButtonComboBox.setObjectName(u"BACKButtonComboBox")
        self.BACKButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.BACKButtonComboBox.setFont(font5)

        self.horizontalLayout_24.addWidget(self.BACKButtonComboBox)


        self.verticalLayout_7.addWidget(self.BACKButtonFrame)

        self.RIGHTPADButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.RIGHTPADButtonFrame.setObjectName(u"RIGHTPADButtonFrame")
        self.RIGHTPADButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.RIGHTPADButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RIGHTPADButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RIGHTPADButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.RIGHTPADButtonFrame)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.RIGHTPADButtonLabel = QLabel(self.RIGHTPADButtonFrame)
        self.RIGHTPADButtonLabel.setObjectName(u"RIGHTPADButtonLabel")
        sizePolicy5.setHeightForWidth(self.RIGHTPADButtonLabel.sizePolicy().hasHeightForWidth())
        self.RIGHTPADButtonLabel.setSizePolicy(sizePolicy5)
        self.RIGHTPADButtonLabel.setMaximumSize(QSize(100, 100))
        self.RIGHTPADButtonLabel.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.RIGHTPADButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Stick Click.svg"))
        self.RIGHTPADButtonLabel.setScaledContents(True)

        self.horizontalLayout_37.addWidget(self.RIGHTPADButtonLabel)

        self.RIGHTPADButtonComboBox = QComboBox(self.RIGHTPADButtonFrame)
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.addItem("")
        self.RIGHTPADButtonComboBox.setObjectName(u"RIGHTPADButtonComboBox")
        self.RIGHTPADButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.RIGHTPADButtonComboBox.setFont(font5)

        self.horizontalLayout_37.addWidget(self.RIGHTPADButtonComboBox)


        self.verticalLayout_7.addWidget(self.RIGHTPADButtonFrame)

        self.LEFTPADButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.LEFTPADButtonFrame.setObjectName(u"LEFTPADButtonFrame")
        self.LEFTPADButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.LEFTPADButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LEFTPADButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LEFTPADButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.LEFTPADButtonFrame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.LEFTPADButtonLabel = QLabel(self.LEFTPADButtonFrame)
        self.LEFTPADButtonLabel.setObjectName(u"LEFTPADButtonLabel")
        sizePolicy5.setHeightForWidth(self.LEFTPADButtonLabel.sizePolicy().hasHeightForWidth())
        self.LEFTPADButtonLabel.setSizePolicy(sizePolicy5)
        self.LEFTPADButtonLabel.setMaximumSize(QSize(100, 100))
        self.LEFTPADButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Stick Click.svg"))
        self.LEFTPADButtonLabel.setScaledContents(True)

        self.horizontalLayout_35.addWidget(self.LEFTPADButtonLabel)

        self.LEFTPADButtonComboBox = QComboBox(self.LEFTPADButtonFrame)
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.addItem("")
        self.LEFTPADButtonComboBox.setObjectName(u"LEFTPADButtonComboBox")
        self.LEFTPADButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.LEFTPADButtonComboBox.setFont(font5)

        self.horizontalLayout_35.addWidget(self.LEFTPADButtonComboBox)


        self.verticalLayout_7.addWidget(self.LEFTPADButtonFrame)

        self.HOMEButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.HOMEButtonFrame.setObjectName(u"HOMEButtonFrame")
        self.HOMEButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.HOMEButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.HOMEButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.HOMEButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.HOMEButtonFrame)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.HOMEButtonLabel = QLabel(self.HOMEButtonFrame)
        self.HOMEButtonLabel.setObjectName(u"HOMEButtonLabel")
        sizePolicy5.setHeightForWidth(self.HOMEButtonLabel.sizePolicy().hasHeightForWidth())
        self.HOMEButtonLabel.setSizePolicy(sizePolicy5)
        self.HOMEButtonLabel.setMaximumSize(QSize(100, 100))
        self.HOMEButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Home.svg"))
        self.HOMEButtonLabel.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.HOMEButtonLabel)

        self.HOMEButtonComboBox = QComboBox(self.HOMEButtonFrame)
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.addItem("")
        self.HOMEButtonComboBox.setObjectName(u"HOMEButtonComboBox")
        self.HOMEButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.HOMEButtonComboBox.setFont(font5)

        self.horizontalLayout_29.addWidget(self.HOMEButtonComboBox)


        self.verticalLayout_7.addWidget(self.HOMEButtonFrame)

        self.PADUPButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.PADUPButtonFrame.setObjectName(u"PADUPButtonFrame")
        self.PADUPButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADUPButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADUPButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADUPButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.PADUPButtonFrame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.PADUPButtonLabel = QLabel(self.PADUPButtonFrame)
        self.PADUPButtonLabel.setObjectName(u"PADUPButtonLabel")
        sizePolicy5.setHeightForWidth(self.PADUPButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADUPButtonLabel.setSizePolicy(sizePolicy5)
        self.PADUPButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADUPButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Up.svg"))
        self.PADUPButtonLabel.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.PADUPButtonLabel)

        self.PADUPButtonComboBox = QComboBox(self.PADUPButtonFrame)
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.addItem("")
        self.PADUPButtonComboBox.setObjectName(u"PADUPButtonComboBox")
        self.PADUPButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.PADUPButtonComboBox.setFont(font5)

        self.horizontalLayout_25.addWidget(self.PADUPButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADUPButtonFrame)

        self.PADDOWNButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.PADDOWNButtonFrame.setObjectName(u"PADDOWNButtonFrame")
        self.PADDOWNButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADDOWNButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADDOWNButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADDOWNButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.PADDOWNButtonFrame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.PADDOWNButtonLabel = QLabel(self.PADDOWNButtonFrame)
        self.PADDOWNButtonLabel.setObjectName(u"PADDOWNButtonLabel")
        sizePolicy5.setHeightForWidth(self.PADDOWNButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADDOWNButtonLabel.setSizePolicy(sizePolicy5)
        self.PADDOWNButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADDOWNButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Down.svg"))
        self.PADDOWNButtonLabel.setScaledContents(True)

        self.horizontalLayout_36.addWidget(self.PADDOWNButtonLabel)

        self.PADDOWNButtonComboBox = QComboBox(self.PADDOWNButtonFrame)
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.addItem("")
        self.PADDOWNButtonComboBox.setObjectName(u"PADDOWNButtonComboBox")
        self.PADDOWNButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.PADDOWNButtonComboBox.setFont(font5)

        self.horizontalLayout_36.addWidget(self.PADDOWNButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADDOWNButtonFrame)

        self.PADRIGHTButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.PADRIGHTButtonFrame.setObjectName(u"PADRIGHTButtonFrame")
        self.PADRIGHTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADRIGHTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADRIGHTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADRIGHTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.PADRIGHTButtonFrame)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.PADRIGHTButtonLabel = QLabel(self.PADRIGHTButtonFrame)
        self.PADRIGHTButtonLabel.setObjectName(u"PADRIGHTButtonLabel")
        sizePolicy5.setHeightForWidth(self.PADRIGHTButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADRIGHTButtonLabel.setSizePolicy(sizePolicy5)
        self.PADRIGHTButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADRIGHTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Right.svg"))
        self.PADRIGHTButtonLabel.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.PADRIGHTButtonLabel)

        self.PADRIGHTButtonComboBox = QComboBox(self.PADRIGHTButtonFrame)
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.addItem("")
        self.PADRIGHTButtonComboBox.setObjectName(u"PADRIGHTButtonComboBox")
        self.PADRIGHTButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.PADRIGHTButtonComboBox.setFont(font5)

        self.horizontalLayout_33.addWidget(self.PADRIGHTButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADRIGHTButtonFrame)

        self.PADLEFTButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.PADLEFTButtonFrame.setObjectName(u"PADLEFTButtonFrame")
        self.PADLEFTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.PADLEFTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.PADLEFTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.PADLEFTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.PADLEFTButtonFrame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.PADLEFTButtonLabel = QLabel(self.PADLEFTButtonFrame)
        self.PADLEFTButtonLabel.setObjectName(u"PADLEFTButtonLabel")
        sizePolicy5.setHeightForWidth(self.PADLEFTButtonLabel.sizePolicy().hasHeightForWidth())
        self.PADLEFTButtonLabel.setSizePolicy(sizePolicy5)
        self.PADLEFTButtonLabel.setMaximumSize(QSize(100, 100))
        self.PADLEFTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/D-Pad Left.svg"))
        self.PADLEFTButtonLabel.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.PADLEFTButtonLabel)

        self.PADLEFTButtonComboBox = QComboBox(self.PADLEFTButtonFrame)
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.addItem("")
        self.PADLEFTButtonComboBox.setObjectName(u"PADLEFTButtonComboBox")
        self.PADLEFTButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.PADLEFTButtonComboBox.setFont(font5)

        self.horizontalLayout_26.addWidget(self.PADLEFTButtonComboBox)


        self.verticalLayout_7.addWidget(self.PADLEFTButtonFrame)

        self.RIGHTVERTICALAXISFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.RIGHTVERTICALAXISFrame.setObjectName(u"RIGHTVERTICALAXISFrame")
        self.RIGHTVERTICALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.RIGHTVERTICALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RIGHTVERTICALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RIGHTVERTICALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.RIGHTVERTICALAXISFrame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.RIGHTVERTICALAXISLabel = QLabel(self.RIGHTVERTICALAXISFrame)
        self.RIGHTVERTICALAXISLabel.setObjectName(u"RIGHTVERTICALAXISLabel")
        sizePolicy5.setHeightForWidth(self.RIGHTVERTICALAXISLabel.sizePolicy().hasHeightForWidth())
        self.RIGHTVERTICALAXISLabel.setSizePolicy(sizePolicy5)
        self.RIGHTVERTICALAXISLabel.setMaximumSize(QSize(100, 100))
        self.RIGHTVERTICALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Stick Up.svg"))
        self.RIGHTVERTICALAXISLabel.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.RIGHTVERTICALAXISLabel)

        self.RIGHTVERTICALAXISComboBox = QComboBox(self.RIGHTVERTICALAXISFrame)
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.addItem("")
        self.RIGHTVERTICALAXISComboBox.setObjectName(u"RIGHTVERTICALAXISComboBox")
        self.RIGHTVERTICALAXISComboBox.setMaximumSize(QSize(16777215, 50))
        self.RIGHTVERTICALAXISComboBox.setFont(font5)

        self.horizontalLayout_40.addWidget(self.RIGHTVERTICALAXISComboBox)


        self.verticalLayout_7.addWidget(self.RIGHTVERTICALAXISFrame)

        self.RIGHTHORIZONTALAXISFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.RIGHTHORIZONTALAXISFrame.setObjectName(u"RIGHTHORIZONTALAXISFrame")
        self.RIGHTHORIZONTALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.RIGHTHORIZONTALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RIGHTHORIZONTALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RIGHTHORIZONTALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.RIGHTHORIZONTALAXISFrame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.RIGHTHORIZONTALAXISLabel = QLabel(self.RIGHTHORIZONTALAXISFrame)
        self.RIGHTHORIZONTALAXISLabel.setObjectName(u"RIGHTHORIZONTALAXISLabel")
        sizePolicy5.setHeightForWidth(self.RIGHTHORIZONTALAXISLabel.sizePolicy().hasHeightForWidth())
        self.RIGHTHORIZONTALAXISLabel.setSizePolicy(sizePolicy5)
        self.RIGHTHORIZONTALAXISLabel.setMaximumSize(QSize(100, 100))
        self.RIGHTHORIZONTALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Stick Right.svg"))
        self.RIGHTHORIZONTALAXISLabel.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.RIGHTHORIZONTALAXISLabel)

        self.RIGHTHORIZONTALAXISComboBox = QComboBox(self.RIGHTHORIZONTALAXISFrame)
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.addItem("")
        self.RIGHTHORIZONTALAXISComboBox.setObjectName(u"RIGHTHORIZONTALAXISComboBox")
        self.RIGHTHORIZONTALAXISComboBox.setMaximumSize(QSize(16777215, 50))
        self.RIGHTHORIZONTALAXISComboBox.setFont(font5)

        self.horizontalLayout_30.addWidget(self.RIGHTHORIZONTALAXISComboBox)


        self.verticalLayout_7.addWidget(self.RIGHTHORIZONTALAXISFrame)

        self.LEFTVERTICALAXISFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.LEFTVERTICALAXISFrame.setObjectName(u"LEFTVERTICALAXISFrame")
        self.LEFTVERTICALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.LEFTVERTICALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LEFTVERTICALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LEFTVERTICALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.LEFTVERTICALAXISFrame)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.LEFTVERTICALAXISLabel = QLabel(self.LEFTVERTICALAXISFrame)
        self.LEFTVERTICALAXISLabel.setObjectName(u"LEFTVERTICALAXISLabel")
        sizePolicy5.setHeightForWidth(self.LEFTVERTICALAXISLabel.sizePolicy().hasHeightForWidth())
        self.LEFTVERTICALAXISLabel.setSizePolicy(sizePolicy5)
        self.LEFTVERTICALAXISLabel.setMaximumSize(QSize(100, 100))
        self.LEFTVERTICALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Stick Up.svg"))
        self.LEFTVERTICALAXISLabel.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.LEFTVERTICALAXISLabel)

        self.LEFTVERTICALAXISComboBox = QComboBox(self.LEFTVERTICALAXISFrame)
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.addItem("")
        self.LEFTVERTICALAXISComboBox.setObjectName(u"LEFTVERTICALAXISComboBox")
        self.LEFTVERTICALAXISComboBox.setMaximumSize(QSize(16777215, 50))
        self.LEFTVERTICALAXISComboBox.setFont(font5)

        self.horizontalLayout_27.addWidget(self.LEFTVERTICALAXISComboBox)


        self.verticalLayout_7.addWidget(self.LEFTVERTICALAXISFrame)

        self.LEFTHORIZONTALAXISFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.LEFTHORIZONTALAXISFrame.setObjectName(u"LEFTHORIZONTALAXISFrame")
        self.LEFTHORIZONTALAXISFrame.setMaximumSize(QSize(16777215, 125))
        self.LEFTHORIZONTALAXISFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LEFTHORIZONTALAXISFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LEFTHORIZONTALAXISFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.LEFTHORIZONTALAXISFrame)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.LEFTHORIZONTALAXISLabel = QLabel(self.LEFTHORIZONTALAXISFrame)
        self.LEFTHORIZONTALAXISLabel.setObjectName(u"LEFTHORIZONTALAXISLabel")
        sizePolicy5.setHeightForWidth(self.LEFTHORIZONTALAXISLabel.sizePolicy().hasHeightForWidth())
        self.LEFTHORIZONTALAXISLabel.setSizePolicy(sizePolicy5)
        self.LEFTHORIZONTALAXISLabel.setMaximumSize(QSize(100, 100))
        self.LEFTHORIZONTALAXISLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Stick Right.svg"))
        self.LEFTHORIZONTALAXISLabel.setScaledContents(True)

        self.horizontalLayout_39.addWidget(self.LEFTHORIZONTALAXISLabel)

        self.LEFTHORIZONTALAXISComboBox = QComboBox(self.LEFTHORIZONTALAXISFrame)
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.addItem("")
        self.LEFTHORIZONTALAXISComboBox.setObjectName(u"LEFTHORIZONTALAXISComboBox")
        self.LEFTHORIZONTALAXISComboBox.setMaximumSize(QSize(16777215, 50))
        self.LEFTHORIZONTALAXISComboBox.setFont(font5)

        self.horizontalLayout_39.addWidget(self.LEFTHORIZONTALAXISComboBox)


        self.verticalLayout_7.addWidget(self.LEFTHORIZONTALAXISFrame)

        self.RTButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.RTButtonFrame.setObjectName(u"RTButtonFrame")
        self.RTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.RTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.RTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.RTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.RTButtonFrame)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.RTButtonLabel = QLabel(self.RTButtonFrame)
        self.RTButtonLabel.setObjectName(u"RTButtonLabel")
        sizePolicy5.setHeightForWidth(self.RTButtonLabel.sizePolicy().hasHeightForWidth())
        self.RTButtonLabel.setSizePolicy(sizePolicy5)
        self.RTButtonLabel.setMaximumSize(QSize(100, 100))
        self.RTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Right Trigger.svg"))
        self.RTButtonLabel.setScaledContents(True)

        self.horizontalLayout_32.addWidget(self.RTButtonLabel)

        self.RTButtonComboBox = QComboBox(self.RTButtonFrame)
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.addItem("")
        self.RTButtonComboBox.setObjectName(u"RTButtonComboBox")
        self.RTButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.RTButtonComboBox.setFont(font5)

        self.horizontalLayout_32.addWidget(self.RTButtonComboBox)


        self.verticalLayout_7.addWidget(self.RTButtonFrame)

        self.LTButtonFrame = QFrame(self.controllerSettingsJoystickMappingFrameInScrollArea)
        self.LTButtonFrame.setObjectName(u"LTButtonFrame")
        self.LTButtonFrame.setMaximumSize(QSize(16777215, 125))
        self.LTButtonFrame.setStyleSheet(u"QFrame{\n"
"	background-color: #44475A;\n"
"}")
        self.LTButtonFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.LTButtonFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.LTButtonFrame)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.LTButtonLabel = QLabel(self.LTButtonFrame)
        self.LTButtonLabel.setObjectName(u"LTButtonLabel")
        sizePolicy5.setHeightForWidth(self.LTButtonLabel.sizePolicy().hasHeightForWidth())
        self.LTButtonLabel.setSizePolicy(sizePolicy5)
        self.LTButtonLabel.setMaximumSize(QSize(100, 100))
        self.LTButtonLabel.setPixmap(QPixmap(u":/controllerButtons/Xbox Series Button Icons and Controls/Xbox Series Button Icons and Controls/Buttons Full Solid/White/SVG/Left Trigger.svg"))
        self.LTButtonLabel.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.LTButtonLabel)

        self.LTButtonComboBox = QComboBox(self.LTButtonFrame)
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.addItem("")
        self.LTButtonComboBox.setObjectName(u"LTButtonComboBox")
        self.LTButtonComboBox.setMaximumSize(QSize(16777215, 50))
        self.LTButtonComboBox.setFont(font5)

        self.horizontalLayout_21.addWidget(self.LTButtonComboBox)


        self.verticalLayout_7.addWidget(self.LTButtonFrame)


        self.horizontalLayout_20.addWidget(self.controllerSettingsJoystickMappingFrameInScrollArea)

        self.controllerSettingsScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_15.addWidget(self.controllerSettingsScrollArea)


        self.verticalLayout_6.addWidget(self.controllerSettingsJoystickMappingFrame)

        self.saveControllerSettingFrame = QFrame(self.controllerSettingsPageFrame)
        self.saveControllerSettingFrame.setObjectName(u"saveControllerSettingFrame")
        self.saveControllerSettingFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.saveControllerSettingFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.saveControllerSettingFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.saveControllerSettingButton = QPushButton(self.saveControllerSettingFrame)
        self.saveControllerSettingButton.setObjectName(u"saveControllerSettingButton")
        font6 = QFont()
        font6.setBold(False)
        font6.setItalic(False)
        font6.setUnderline(False)
        self.saveControllerSettingButton.setFont(font6)
        self.saveControllerSettingButton.setStyleSheet(u"QPushButton{\n"
"	font-size: 20px;\n"
"	border-radius: 5px; \n"
"	border: 3px solid #FFB86C;\n"
"}\n"
"")

        self.horizontalLayout_14.addWidget(self.saveControllerSettingButton)


        self.verticalLayout_6.addWidget(self.saveControllerSettingFrame)


        self.horizontalLayout_10.addWidget(self.controllerSettingsPageFrame)

        self.mainBodyStackedWidget.addWidget(self.controllerSettingsPage)

        self.horizontalLayout_7.addWidget(self.mainBodyStackedWidget)


        self.verticalLayout.addWidget(self.mainBodyFrame)

        self.footerFrame = QFrame(self.centralwidget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setMinimumSize(QSize(0, 20))
        self.footerFrame.setMaximumSize(QSize(16777215, 20))
        self.footerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.footerFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.footerVersionFrame = QFrame(self.footerFrame)
        self.footerVersionFrame.setObjectName(u"footerVersionFrame")
        self.footerVersionFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.footerVersionFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footerVersionFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.footerVersionFrame)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.footerVersionFrame, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalSpacer = QSpacerItem(733, 15, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sizeGripFrame = QFrame(self.footerFrame)
        self.sizeGripFrame.setObjectName(u"sizeGripFrame")
        self.sizeGripFrame.setMinimumSize(QSize(20, 20))
        self.sizeGripFrame.setMaximumSize(QSize(20, 20))
        self.sizeGripFrame.setStyleSheet(u"QSizeGrip{\n"
"	background: transparent;\n"
"	border: none;\n"
"}")
        self.sizeGripFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sizeGripFrame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.sizeGripFrame)


        self.verticalLayout.addWidget(self.footerFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainBodyStackedWidget.setCurrentIndex(1)
        self.homePageStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.navigationButton.setText("")
        self.tittleLabel.setText(QCoreApplication.translate("MainWindow", u"VortexUI", None))
        self.minimizeButton.setText("")
        self.maximizeButton.setText("")
        self.exitButton.setText("")
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.cameraButton.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.ocrButton.setText(QCoreApplication.translate("MainWindow", u"OCR", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.mainHomePageTopLeftCameraLabel.setText("")
        self.mainHomePageTopLeftCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.mainHomePageTopRightCameraLabel.setText("")
        self.mainHomePageTopRightCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.mainHomePageBottomLeftCameraLabel.setText("")
        self.mainHomePageBottomLeftCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.mainHomePageBottomRightCameraLabel.setText("")
        self.mainHomePageBottomRightCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.secondaryHomePageTopLeftCameraLabel.setText("")
        self.secondaryHomePageTopLeftCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.secondaryHomePageTopRightCameraLabel.setText("")
        self.secondaryHomePageTopRightCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.secondaryHomePageBottomLeftCameraLabel.setText("")
        self.secondaryHomePageBottomLeftCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.secondaryHomePageBottomRightCameraLabel.setText("")
        self.secondaryHomePageBottomRightCamerasNumberLabel.setText(QCoreApplication.translate("MainWindow", u"Camera8", None))
        self.fourThrustersLabel.setText("")
        self.upDownThrustersLabel.setText("")
        self.servoLabel.setText("")
        self.armingLabel.setText(QCoreApplication.translate("MainWindow", u"Armed", None))
        self.ledLabel.setText(QCoreApplication.translate("MainWindow", u"Led", None))
        self.gripperLabel.setText(QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.leftGripperLabel.setText(QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.fluidSuctionLabel.setText(QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.floatingDebrisLabel.setText(QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.altitudeHoldLabel.setText(QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.stabilizeFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.rollLabel.setText(QCoreApplication.translate("MainWindow", u"Roll", None))
        self.rollReadingLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pitchLabel.setText(QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.pitchReadingLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.gainLabel.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.gainReadingLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.phLael.setText(QCoreApplication.translate("MainWindow", u"PH", None))
        self.phSensorReadingLabel.setText(QCoreApplication.translate("MainWindow", u"7.1", None))
        self.headingLabel.setText(QCoreApplication.translate("MainWindow", u"Heading", None))
        self.headingReadingLabel.setText(QCoreApplication.translate("MainWindow", u"300", None))
        self.depthLabel.setText(QCoreApplication.translate("MainWindow", u"Depth", None))
        self.depthReadingLabel.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.ocrResults.setText("")
        self.ocrTextSubmitButton.setText(QCoreApplication.translate("MainWindow", u"Submit Text", None))
        self.OAKCameraLocationLabel.setText(QCoreApplication.translate("MainWindow", u"OAKCameraLocation", None))
        self.OAKCameraLocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.OAKCameraLocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.OAKCameraLocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.OAKCameraLocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.OAKCameraLocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.OAKCameraLocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.OAKCameraLocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.OAKCameraLocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA1LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera1Location", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA1LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA2LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera2Location", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA2LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA3LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera3Location", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA3LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA4LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera4Location", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA4LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA5LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera5Location", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA5LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA6LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera6Location", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA6LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA7LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera7Location", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA7LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA8LocationLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera8Location", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Camera1", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Camera2", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Camera3", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Camera4", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Camera5", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Camera6", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Camera7", None))
        self.RTSPCAMERA8LocationComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Camera8", None))

        self.RTSPCAMERA1SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera1Source                   ", None))
        self.lineEditRTSPCAMERA1SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA2SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera2Source                   ", None))
        self.lineEditRTSPCAMERA2SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA3SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera3Source                   ", None))
        self.lineEditRTSPCAMERA3SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA4SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera4Source                   ", None))
        self.lineEditRTSPCAMERA4SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA5SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera5Source                   ", None))
        self.lineEditRTSPCAMERA5SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA6SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera6Source                   ", None))
        self.lineEditRTSPCAMERA6SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA7SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera7Source                   ", None))
        self.lineEditRTSPCAMERA7SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.RTSPCAMERA8SourceLabel.setText(QCoreApplication.translate("MainWindow", u"RTSPCamera8Source                   ", None))
        self.lineEditRTSPCAMERA8SourceText.setText(QCoreApplication.translate("MainWindow", u"None", None))
        self.saveCameraSettingButton.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.controllerSettingsButton.setText("")
        self.cameraSettingsButton.setText(QCoreApplication.translate("MainWindow", u"Camera Settings", None))
        self.generalSettingsButton.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.AButtonLabel.setText("")
        self.AButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.AButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.AButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.AButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.AButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.AButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.AButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.AButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.AButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.AButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.AButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.BButtonLabel.setText("")
        self.BButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.BButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.BButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.BButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.BButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.BButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.BButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.BButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.BButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.BButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.BButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.YButtonLabel.setText("")
        self.YButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.YButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.YButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.YButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.YButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.YButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.YButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.YButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.YButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.YButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.YButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.XButtonLabel.setText("")
        self.XButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Led", None))
        self.XButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.XButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.XButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.XButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.XButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.XButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.XButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.XButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.XButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.XButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.LBButtonLabel.setText("")
        self.LBButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.LBButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.LBButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.LBButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.LBButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.LBButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.LBButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.LBButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.LBButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.LBButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.LBButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.RBButtonLabel.setText("")
        self.RBButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.RBButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.RBButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.RBButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.RBButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.RBButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.RBButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.RBButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.RBButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.RBButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.RBButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.STARTButtonLabel.setText("")
        self.STARTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.STARTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.STARTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.STARTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.STARTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.STARTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.STARTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.STARTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.STARTButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.STARTButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.STARTButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.BACKButtonLabel.setText("")
        self.BACKButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.BACKButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.BACKButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.BACKButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.BACKButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.BACKButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.BACKButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.BACKButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.BACKButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.BACKButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.BACKButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.RIGHTPADButtonLabel.setText("")
        self.RIGHTPADButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.RIGHTPADButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.RIGHTPADButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.RIGHTPADButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.RIGHTPADButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.RIGHTPADButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.RIGHTPADButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.RIGHTPADButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.RIGHTPADButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.RIGHTPADButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.RIGHTPADButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.LEFTPADButtonLabel.setText("")
        self.LEFTPADButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.LEFTPADButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.LEFTPADButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.LEFTPADButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.LEFTPADButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Led", None))
        self.LEFTPADButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.LEFTPADButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.LEFTPADButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.LEFTPADButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.LEFTPADButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.LEFTPADButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"None", None))

        self.HOMEButtonLabel.setText("")
        self.HOMEButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.HOMEButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.HOMEButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.HOMEButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.HOMEButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.HOMEButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.HOMEButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.HOMEButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.HOMEButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.HOMEButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.HOMEButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.PADUPButtonLabel.setText("")
        self.PADUPButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADUPButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADUPButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADUPButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADUPButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADUPButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADUPButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADUPButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADUPButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADUPButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Arming", None))
        self.PADUPButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Stabilize", None))

        self.PADDOWNButtonLabel.setText("")
        self.PADDOWNButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADDOWNButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADDOWNButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADDOWNButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADDOWNButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADDOWNButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADDOWNButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADDOWNButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADDOWNButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADDOWNButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.PADDOWNButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Arming", None))

        self.PADRIGHTButtonLabel.setText("")
        self.PADRIGHTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADRIGHTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADRIGHTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADRIGHTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADRIGHTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADRIGHTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADRIGHTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADRIGHTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADRIGHTButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADRIGHTButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.PADRIGHTButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Arming", None))

        self.PADLEFTButtonLabel.setText("")
        self.PADLEFTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.PADLEFTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"AltitudeHold", None))
        self.PADLEFTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"CameraSwitch", None))
        self.PADLEFTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"FloatingDebris", None))
        self.PADLEFTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"FluidSuction", None))
        self.PADLEFTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Led", None))
        self.PADLEFTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"LeftGripper", None))
        self.PADLEFTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Gain", None))
        self.PADLEFTButtonComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"RightGripper", None))
        self.PADLEFTButtonComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Stabilize", None))
        self.PADLEFTButtonComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Arming", None))

        self.RIGHTVERTICALAXISLabel.setText("")
        self.RIGHTVERTICALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.RIGHTVERTICALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.RIGHTHORIZONTALAXISLabel.setText("")
        self.RIGHTHORIZONTALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.RIGHTHORIZONTALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.LEFTVERTICALAXISLabel.setText("")
        self.LEFTVERTICALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.LEFTVERTICALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.LEFTVERTICALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.LEFTVERTICALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.LEFTVERTICALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.LEFTVERTICALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.LEFTVERTICALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.LEFTVERTICALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.LEFTHORIZONTALAXISLabel.setText("")
        self.LEFTHORIZONTALAXISComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.LEFTHORIZONTALAXISComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.RTButtonLabel.setText("")
        self.RTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.RTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.RTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.RTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.RTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.RTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.RTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.RTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.LTButtonLabel.setText("")
        self.LTButtonComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Servo", None))
        self.LTButtonComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Heave", None))
        self.LTButtonComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Pitch", None))
        self.LTButtonComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Roll", None))
        self.LTButtonComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Surge", None))
        self.LTButtonComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Sway", None))
        self.LTButtonComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Yaw", None))
        self.LTButtonComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"None", None))

        self.saveControllerSettingButton.setText(QCoreApplication.translate("MainWindow", u"Save Settings", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"v1.0", None))
    # retranslateUi

