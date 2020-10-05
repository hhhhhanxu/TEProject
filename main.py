from PyQt5 import QtGui
from PyQt5 import QtWidgets
from Qtdesign import Ui_MainWindow
from getData import read_data
from core.inference import infer

class my_ui(Ui_MainWindow):

    def __init__(self,parent=None):
        super(my_ui,self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.startPlot)
        pass

    def startPlot(self):
        new_data = read_data()
        if new_data == None:
            #通信失败
            self.label_5.setText("Network Connnetion is Failed")
        else:
            #设置时间
            time = new_data['time']
            font = QtGui.QFont()
            font.setFamily("黑体")
            font.setPointSize(9)
            self.Time.setFont(font)
            self.Time.setText(time)
            # 绘图
            self.plotAll(new_data)
            #调用pytorch推断
            print('准备推断')
            state = infer(filename=new_data['filename'])
            self.label_5.setText(state)


    def plotAll(self,new_data):
        self.position.run(new_data)
        self.force.run(new_data)
        self.speed.run(new_data)







if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = my_ui()
    ui.show()
    sys.exit(app.exec_())
