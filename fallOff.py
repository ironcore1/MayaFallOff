from PySide2 import QtWidgets,QtUiTools,QtCore
import maya.OpenMayaUI as apiUI
import pymel.core as pm
import shiboken2
import maya.cmds as cmds


def getMayaWindow():
    # this gets Maya's main window as a QT object
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken2.wrapInstance(long(ptr), QtWidgets.QWidget)

class MyWidget(QtWidgets.QWidget):

    moveKeySettingsDic = {
        'constant': 'constant',
        'linear': 'linear',
        'exponetial': 'power'
    }

        # this is your own custom class object
    def __init__(self, parent):
        # keep your parent when you make it - i.e your object knows the maya main window
        self.myParent = parent
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile("C:\Users\jrobinson\Desktop\PythonUI\TomUI.ui")
        file.open(QtCore.QFile.ReadOnly)
        self.myWidget = loader.load(file, self.myParent)
        file.close()
        self.connectButtons()
        self.myWidget.show()

    def connectButtons(self):
        # hook up your buttons and gui stuff here
        self.myWidget.fallOff_ComboBox.currentIndexChanged.connect(self.setMoveFalloff)

    def whatFalloffAmI(self):
        myNewFalloff = self.moveKeySettingsDic[self.myWidget.fallOff_ComboBox.currentText ()]
        print "my falloff is =", myNewFalloff

    def setMoveFalloff(self):
        cmds.moveKeyCtx('moveKeyContext' , e=True, moveFunction=self.myWidget.whatFalloffAmI())


test = MyWidget(getMayaWindow())