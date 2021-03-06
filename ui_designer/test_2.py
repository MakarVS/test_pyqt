# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1618, 950)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("backhround-color:rgb(156, 156, 156)")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.two_points = QtWidgets.QWidget()
        self.two_points.setObjectName("two_points")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.two_points)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.two_points_layout = QtWidgets.QVBoxLayout()
        self.two_points_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.two_points_layout.setObjectName("two_points_layout")
        self.layout_input_two_points = QtWidgets.QHBoxLayout()
        self.layout_input_two_points.setObjectName("layout_input_two_points")
        self.point_1 = QtWidgets.QVBoxLayout()
        self.point_1.setObjectName("point_1")
        self.label_point_1 = QtWidgets.QLabel(self.two_points)
        self.label_point_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_point_1.setObjectName("label_point_1")
        self.point_1.addWidget(self.label_point_1)
        self.x1_line = QtWidgets.QHBoxLayout()
        self.x1_line.setObjectName("x1_line")
        self.label_x1 = QtWidgets.QLabel(self.two_points)
        self.label_x1.setObjectName("label_x1")
        self.x1_line.addWidget(self.label_x1)
        self.lineEdit_x1 = QtWidgets.QLineEdit(self.two_points)
        self.lineEdit_x1.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_x1.setFrame(True)
        self.lineEdit_x1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_x1.setDragEnabled(False)
        self.lineEdit_x1.setPlaceholderText("")
        self.lineEdit_x1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_x1.setClearButtonEnabled(False)
        self.lineEdit_x1.setObjectName("lineEdit_x1")
        self.x1_line.addWidget(self.lineEdit_x1)
        self.point_1.addLayout(self.x1_line)
        self.y1_line = QtWidgets.QHBoxLayout()
        self.y1_line.setObjectName("y1_line")
        self.label_y1 = QtWidgets.QLabel(self.two_points)
        self.label_y1.setObjectName("label_y1")
        self.y1_line.addWidget(self.label_y1)
        self.lineEdit_y1 = QtWidgets.QLineEdit(self.two_points)
        self.lineEdit_y1.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_y1.setObjectName("lineEdit_y1")
        self.y1_line.addWidget(self.lineEdit_y1)
        self.point_1.addLayout(self.y1_line)
        self.point_1.setStretch(0, 1)
        self.point_1.setStretch(1, 4)
        self.point_1.setStretch(2, 4)
        self.layout_input_two_points.addLayout(self.point_1)
        self.line_between_points = QtWidgets.QFrame(self.two_points)
        self.line_between_points.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_between_points.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_between_points.setObjectName("line_between_points")
        self.layout_input_two_points.addWidget(self.line_between_points)
        self.point_2 = QtWidgets.QVBoxLayout()
        self.point_2.setObjectName("point_2")
        self.label_point_2 = QtWidgets.QLabel(self.two_points)
        self.label_point_2.setObjectName("label_point_2")
        self.point_2.addWidget(self.label_point_2)
        self.x2_line = QtWidgets.QHBoxLayout()
        self.x2_line.setObjectName("x2_line")
        self.label_x2 = QtWidgets.QLabel(self.two_points)
        self.label_x2.setObjectName("label_x2")
        self.x2_line.addWidget(self.label_x2)
        self.lineEdit_x2 = QtWidgets.QLineEdit(self.two_points)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_x2.sizePolicy().hasHeightForWidth())
        self.lineEdit_x2.setSizePolicy(sizePolicy)
        self.lineEdit_x2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_x2.setObjectName("lineEdit_x2")
        self.x2_line.addWidget(self.lineEdit_x2)
        self.point_2.addLayout(self.x2_line)
        self.y2_line = QtWidgets.QHBoxLayout()
        self.y2_line.setObjectName("y2_line")
        self.label_y2 = QtWidgets.QLabel(self.two_points)
        self.label_y2.setObjectName("label_y2")
        self.y2_line.addWidget(self.label_y2)
        self.lineEdit_y2 = QtWidgets.QLineEdit(self.two_points)
        self.lineEdit_y2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_y2.setObjectName("lineEdit_y2")
        self.y2_line.addWidget(self.lineEdit_y2)
        self.point_2.addLayout(self.y2_line)
        self.point_2.setStretch(0, 1)
        self.point_2.setStretch(1, 4)
        self.point_2.setStretch(2, 4)
        self.layout_input_two_points.addLayout(self.point_2)
        self.two_points_layout.addLayout(self.layout_input_two_points)
        self.layout_build_line = QtWidgets.QHBoxLayout()
        self.layout_build_line.setObjectName("layout_build_line")
        self.label_units = QtWidgets.QLabel(self.two_points)
        self.label_units.setObjectName("label_units")
        self.layout_build_line.addWidget(self.label_units)
        self.comboBox_units = QtWidgets.QComboBox(self.two_points)
        self.comboBox_units.setObjectName("comboBox_units")
        self.layout_build_line.addWidget(self.comboBox_units)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_build_line.addItem(spacerItem)
        self.button_line_2_p = QtWidgets.QPushButton(self.two_points)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_line_2_p.sizePolicy().hasHeightForWidth())
        self.button_line_2_p.setSizePolicy(sizePolicy)
        self.button_line_2_p.setObjectName("button_line_2_p")
        self.layout_build_line.addWidget(self.button_line_2_p)
        self.layout_build_line.setStretch(2, 3)
        self.layout_build_line.setStretch(3, 1)
        self.two_points_layout.addLayout(self.layout_build_line)
        self.label = QtWidgets.QLabel(self.two_points)
        self.label.setText("")
        self.label.setObjectName("label")
        self.two_points_layout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.two_points_layout.addItem(spacerItem1)
        self.layout_finally_geometry = QtWidgets.QHBoxLayout()
        self.layout_finally_geometry.setObjectName("layout_finally_geometry")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_finally_geometry.addItem(spacerItem2)
        self.button_finally_geometry = QtWidgets.QPushButton(self.two_points)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_finally_geometry.sizePolicy().hasHeightForWidth())
        self.button_finally_geometry.setSizePolicy(sizePolicy)
        self.button_finally_geometry.setObjectName("button_finally_geometry")
        self.layout_finally_geometry.addWidget(self.button_finally_geometry)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_finally_geometry.addItem(spacerItem3)
        self.layout_finally_geometry.setStretch(0, 1)
        self.layout_finally_geometry.setStretch(1, 1)
        self.layout_finally_geometry.setStretch(2, 1)
        self.two_points_layout.addLayout(self.layout_finally_geometry)
        self.two_points_layout.setStretch(0, 6)
        self.two_points_layout.setStretch(1, 2)
        self.two_points_layout.setStretch(2, 2)
        self.two_points_layout.setStretch(3, 10)
        self.two_points_layout.setStretch(4, 3)
        self.gridLayout_3.addLayout(self.two_points_layout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.two_points, "")
        self.line_angle = QtWidgets.QWidget()
        self.line_angle.setObjectName("line_angle")
        self.tabWidget.addTab(self.line_angle, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setDragDropOverwriteMode(False)
        self.treeWidget.setRootIsDecorated(True)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setExpandsOnDoubleClick(True)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.treeWidget.header().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.treeWidget)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1618, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_new_file = QtWidgets.QAction(MainWindow)
        self.action_new_file.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Vitaliy/.designer/icon/new_file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_new_file.setIcon(icon)
        self.action_new_file.setObjectName("action_new_file")
        self.action_geometry = QtWidgets.QAction(MainWindow)
        self.action_geometry.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/Vitaliy/.designer/icon/geometry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_geometry.setIcon(icon1)
        self.action_geometry.setObjectName("action_geometry")
        self.menu.addAction(self.action_new_file)
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.action_geometry)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_point_1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Введите координаты первой точки</span></p></body></html>"))
        self.label_x1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">x1</span></p></body></html>"))
        self.label_y1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">y1</span></p></body></html>"))
        self.label_point_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Введите координаты второй точки</span></p></body></html>"))
        self.label_x2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">x2</span></p></body></html>"))
        self.label_y2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">y2</span></p></body></html>"))
        self.label_units.setText(_translate("MainWindow", "Единицы измерения"))
        self.button_line_2_p.setText(_translate("MainWindow", "Построить линию"))
        self.button_finally_geometry.setText(_translate("MainWindow", "Завершить построение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.two_points), _translate("MainWindow", "Построение линии по двум точкам"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.line_angle), _translate("MainWindow", "Построение линии по длине и углу из последней точки"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Процесс"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Описание"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Геометрия"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "фыв"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Расчет"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "йцу"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.action_new_file.setText(_translate("MainWindow", "Новый расчет"))
        self.action_geometry.setText(_translate("MainWindow", "action_geometry"))
        self.action_geometry.setShortcut(_translate("MainWindow", "Ctrl+G"))
# import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
