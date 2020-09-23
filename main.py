from PyQt5 import QtCore
from PyQt5 import QtWidgets
from qtdesign import Ui_MainWindow

class my_ui(Ui_MainWindow):

    def __init__(self,parent=None):
        super(my_ui,self).__init__(parent)

        self.setupUi(self)
        self.Begin.clicked.connect(self.startPlot)
        self.Pause.clicked.connect(self.pausePlot)
        pass

    def startPlot(self):
        self.widget.startPlot()
        self.widget_2.startPlot()
        self.state.setText("Begin")
        pass

    def pausePlot(self):
        self.widget.pausePlot()
        self.widget_2.pausePlot()
        self.error.setText('Pause')
        self.state.setText("Everything is OK")
        pass




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = my_ui()
    ui.show()
sys.exit(app.exec_())