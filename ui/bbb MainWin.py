# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWin.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(False)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 220, 521, 80))
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 80))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 20, 501, 151))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 18))
        self.menubar.setDefaultUp(True)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPrepocess = QtWidgets.QMenu(self.menubar)
        self.menuPrepocess.setObjectName("menuPrepocess")
        self.menuTrain = QtWidgets.QMenu(self.menubar)
        self.menuTrain.setObjectName("menuTrain")
        self.menuClassify = QtWidgets.QMenu(self.menubar)
        self.menuClassify.setObjectName("menuClassify")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuSampleProduce = QtWidgets.QMenu(self.menubar)
        self.menuSampleProduce.setObjectName("menuSampleProduce")
        self.menuPostproc = QtWidgets.QMenu(self.menubar)
        self.menuPostproc.setObjectName("menuPostproc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_4 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_4.setEnabled(False)
        self.dockWidget_4.setObjectName("dockWidget_4")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_4)
        self.actionLabel_check = QtWidgets.QAction(MainWindow)
        self.actionLabel_check.setObjectName("actionLabel_check")
        self.actionImage_strech = QtWidgets.QAction(MainWindow)
        self.actionImage_strech.setObjectName("actionImage_strech")
        self.actionSampleGenCommon = QtWidgets.QAction(MainWindow)
        self.actionSampleGenCommon.setObjectName("actionSampleGenCommon")
        self.actionCombineSingleModelReults = QtWidgets.QAction(MainWindow)
        self.actionCombineSingleModelReults.setText("Combine multiclass")
        self.actionCombineSingleModelReults.setObjectName("actionCombineSingleModelReults")
        self.action_VoteMultiModelResults = QtWidgets.QAction(MainWindow)
        self.action_VoteMultiModelResults.setText("Vote Results")
        self.action_VoteMultiModelResults.setObjectName("action_VoteMultiModelResults")
        self.actionAccuracyEvaluation = QtWidgets.QAction(MainWindow)
        self.actionAccuracyEvaluation.setText("Accuracy Evaluate")
        self.actionAccuracyEvaluation.setObjectName("actionAccuracyEvaluation")
        self.actionSampleGenByCV2 = QtWidgets.QAction(MainWindow)
        self.actionSampleGenByCV2.setObjectName("actionSampleGenByCV2")
        self.actionImage_Clip = QtWidgets.QAction(MainWindow)
        self.actionImage_Clip.setObjectName("actionImage_Clip")
        self.actionMismatch_Analyze = QtWidgets.QAction(MainWindow)
        self.actionMismatch_Analyze.setObjectName("actionMismatch_Analyze")
        self.actionTrain_Binary_Jaccard = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_Jaccard.setObjectName("actionTrain_Binary_Jaccard")
        self.actionTrain_Binary_JaccCross = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_JaccCross.setObjectName("actionTrain_Binary_JaccCross")
        self.actionTrain_Binary_Cross_entropy = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_Cross_entropy.setObjectName("actionTrain_Binary_Cross_entropy")
        self.actionTrain_Multiclass = QtWidgets.QAction(MainWindow)
        self.actionTrain_Multiclass.setObjectName("actionTrain_Multiclass")
        self.actionTrain_Binary_Onehot_Cross = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_Onehot_Cross.setObjectName("actionTrain_Binary_Onehot_Cross")
        self.actionPredict_Binary_Single = QtWidgets.QAction(MainWindow)
        self.actionPredict_Binary_Single.setObjectName("actionPredict_Binary_Single")
        self.actionPredict_Multiclass_Single = QtWidgets.QAction(MainWindow)
        self.actionPredict_Multiclass_Single.setObjectName("actionPredict_Multiclass_Single")
        self.actionPredict_Binary_Batch = QtWidgets.QAction(MainWindow)
        self.actionPredict_Binary_Batch.setObjectName("actionPredict_Binary_Batch")
        self.actionPredict_Multiclass_Batch = QtWidgets.QAction(MainWindow)
        self.actionPredict_Multiclass_Batch.setObjectName("actionPredict_Multiclass_Batch")
        self.actionPredict_Multiclass = QtWidgets.QAction(MainWindow)
        self.actionPredict_Multiclass.setObjectName("actionPredict_Multiclass")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionTrain_Binary_new = QtWidgets.QAction(MainWindow)
        self.actionTrain_Binary_new.setObjectName("actionTrain_Binary_new")
        self.actionBinarization = QtWidgets.QAction(MainWindow)
        self.actionBinarization.setObjectName("actionBinarization")
        self.actionSample_gen_Self_adapt = QtWidgets.QAction(MainWindow)
        self.actionSample_gen_Self_adapt.setObjectName("actionSample_gen_Self_adapt")
        self.actionRasterToPolygon = QtWidgets.QAction(MainWindow)
        self.actionRasterToPolygon.setObjectName("actionRasterToPolygon")
        self.actionPredict = QtWidgets.QAction(MainWindow)
        self.actionPredict.setObjectName("actionPredict")
        self.action_Train = QtWidgets.QAction(MainWindow)
        self.action_Train.setObjectName("action_Train")
        self.actionconvert_8bit = QtWidgets.QAction(MainWindow)
        self.actionconvert_8bit.setObjectName("actionconvert_8bit")
        self.actionlabel_crop = QtWidgets.QAction(MainWindow)
        self.actionlabel_crop.setObjectName("actionlabel_crop")
        self.actionremove_small_object = QtWidgets.QAction(MainWindow)
        self.actionremove_small_object.setObjectName("actionremove_small_object")
        self.actionOpen_Vector = QtWidgets.QAction(MainWindow)
        self.actionOpen_Vector.setObjectName("actionOpen_Vector")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_Vector)
        self.menuFile.addAction(self.actionExit)
        self.menuPrepocess.addAction(self.actionLabel_check)
        self.menuPrepocess.addAction(self.actionImage_strech)
        self.menuPrepocess.addAction(self.actionImage_Clip)
        self.menuPrepocess.addSeparator()
        self.menuPrepocess.addAction(self.actionconvert_8bit)
        self.menuPrepocess.addAction(self.actionlabel_crop)
        self.menuTrain.addAction(self.action_Train)
        self.menuClassify.addAction(self.actionPredict)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSampleProduce.addAction(self.actionSampleGenCommon)
        self.menuSampleProduce.addAction(self.actionSample_gen_Self_adapt)
        self.menuPostproc.addAction(self.actionCombineSingleModelReults)
        self.menuPostproc.addAction(self.action_VoteMultiModelResults)
        self.menuPostproc.addAction(self.actionAccuracyEvaluation)
        self.menuPostproc.addAction(self.actionBinarization)
        self.menuPostproc.addAction(self.actionRasterToPolygon)
        self.menuPostproc.addAction(self.actionremove_small_object)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPrepocess.menuAction())
        self.menubar.addAction(self.menuSampleProduce.menuAction())
        self.menubar.addAction(self.menuTrain.menuAction())
        self.menubar.addAction(self.menuClassify.menuAction())
        self.menubar.addAction(self.menuPostproc.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionLabel_check.triggered.connect(MainWindow.for_action_label_check)
        self.actionImage_strech.triggered.connect(MainWindow.for_action_image_stretch)
        self.actionImage_Clip.triggered.connect(MainWindow.slot_actiong_image_clip)
        self.actionSampleGenCommon.triggered.connect(MainWindow.slot_action_sampleGenCommon)
        # self.actionTrain_Binary_Cross_entropy.triggered.connect(MainWindow.slot_action_trainBinaryCrossentropy)
        self.actionCombineSingleModelReults.triggered.connect(MainWindow.slot_action_combineMulticlassFromSingleModel)
        self.action_VoteMultiModelResults.triggered.connect(MainWindow.slot_action_VoteMultimodleResults)
        self.actionAccuracyEvaluation.triggered.connect(MainWindow.slot_action_accuracyEvaluate)
        self.actionOpen.triggered.connect(MainWindow.slot_open_show)
        self.actionAbout.triggered.connect(MainWindow.slot_action_about)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionBinarization.triggered.connect(MainWindow.slot_action_binarization)
        self.actionSample_gen_Self_adapt.triggered.connect(MainWindow.slot_action_sampleGenSelfAdapt)
        self.actionRasterToPolygon.triggered.connect(MainWindow.slot_action_rasterToPolygon)
        self.actionPredict.triggered.connect(MainWindow.slot_predict)
        self.action_Train.triggered.connect(MainWindow.slot_train)
        self.actionconvert_8bit.triggered.connect(MainWindow.slot_action_convert8bit)
        self.actionlabel_crop.triggered.connect(MainWindow.slot_action_samplecrop)
        self.actionremove_small_object.triggered.connect(MainWindow.slot_action_removesmallobject)
        self.actionOpen_Vector.triggered.connect(MainWindow.slot_action_openvector)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RS Imagery Deep Learning Process System"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Runtime message:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuPrepocess.setTitle(_translate("MainWindow", "PreProcess"))
        self.menuTrain.setTitle(_translate("MainWindow", "Train"))
        self.menuClassify.setTitle(_translate("MainWindow", "Classify"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuSampleProduce.setTitle(_translate("MainWindow", "Sample"))
        self.menuPostproc.setTitle(_translate("MainWindow", "Postprocess"))
        self.actionLabel_check.setText(_translate("MainWindow", "Label Check"))
        self.actionImage_strech.setText(_translate("MainWindow", "Image Stretch"))
        self.actionSampleGenCommon.setText(_translate("MainWindow", "Sample Generate"))
        self.actionSampleGenByCV2.setText(_translate("MainWindow", "SampleGenByCV2"))
        self.actionImage_Clip.setText(_translate("MainWindow", "Image Clip"))
        self.actionMismatch_Analyze.setText(_translate("MainWindow", "Mismatch Analyze"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open Raster"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        # self.actionTrain_Binary_new.setText(_translate("MainWindow", "Train Binary new"))
        self.actionBinarization.setText(_translate("MainWindow", "Binarization"))
        self.actionSample_gen_Self_adapt.setText(_translate("MainWindow", "Sample_gen Self_adapt"))
        self.actionRasterToPolygon.setText(_translate("MainWindow", "RasterToPolygon"))
        self.actionPredict.setText(_translate("MainWindow", "predict"))
        self.action_Train.setText(_translate("MainWindow", "train"))
        self.actionconvert_8bit.setText(_translate("MainWindow", "convert 8bit"))
        self.actionlabel_crop.setText(_translate("MainWindow", "label crop"))
        self.actionremove_small_object.setText(_translate("MainWindow", "Remove small object"))
        self.actionOpen_Vector.setText(_translate("MainWindow", "Open Vector"))
