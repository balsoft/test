import core,mainwindow
from PyQt4 import QtGui, QtCore
class window(QtGui.QMainWindow):
  def openFile(self):
    fileDialog = QtGui.QFileDialog()
    self.file = fileDialog.getOpenFileName(w,'dialog','~','*.pas')
    self.ui.lineEdit.setText(self.file)
  def runFile(self):
    core.runTest(self.file,self.ui.textEdit.toPlainText(),self.ui.textEdit_2.toPlainText())

  def __init__(self):
    super(window, self).__init__()
    self.ui = mainwindow.Ui_MainWindow()
    self.ui.setupUi(self)
    self.file = ''
    self.ui.pushButton.clicked.connect(self.openFile)
    self.ui.pushButton_2.clicked.connect(self.runFile)
  
app = QtGui.QApplication(sys.argv)
w = window()
w.show()
sys.exit(app.exec_())
