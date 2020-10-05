from PyQt5.QtWidgets import QWidget,QSizePolicy,QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import time
import random
import threading
from datetime import datetime
from matplotlib.dates import date2num,MinuteLocator,SecondLocator,DateFormatter
from scipy import interpolate
from getData import read_data



class MplCanvas(FigureCanvas):
    def __init__(self,title,valueName):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        self.title = title
        self.valueName = valueName
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.fig.suptitle(self.title)  #set title
        self.ax.set_xlabel("time")
        self.ax.set_ylabel(self.valueName)
        self.ax.legend()
        #self.ax.set_ylim(Y_MIN, Y_MAX)
        self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax.xaxis.set_minor_locator(SecondLocator([5, 10, 15, 20, 25]))  # every 10 second is a minor locator
        self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter
        self.curveObj = None  # draw object


    def plot(self, datax, datay):
        if self.curveObj is not None:
            self.fig.clf()
            self.ax = self.fig.add_subplot(111)
            self.fig.suptitle(self.title)  # set title
            self.ax.set_xlabel("time")
            self.ax.set_ylabel(self.valueName)
            self.ax.legend()
            # self.ax.set_ylim(Y_MIN, Y_MAX)
            self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
            self.ax.xaxis.set_minor_locator(SecondLocator([5, 10, 15, 20, 25]))  # every 10 second is a minor locator
            self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter

        self.curveObj, = self.ax.plot(np.array(datax), np.array(datay))
        self.ax.get_legend().remove()
        # else:
        #     # update data of draw object
        #     self.curveObj.set_data(np.array(datax), np.array(datay))
        #     # update limit of X axis,to make sure it can move
        #     self.ax.set_xlim(datax[0], datax[-1])
        ticklabels = self.ax.xaxis.get_ticklabels()
        for tick in ticklabels:
            tick.set_rotation(25)

        self.draw()
        print(self.title+'画了')



class MplCanvasWrapper(QWidget):
    def __init__(self, title, valueName,parent=None):
        QWidget.__init__(self, parent)
        self.Title = title
        self.canvas = MplCanvas(title,valueName)
        self.vbl = QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.dataX = []
        self.dataY = []
        self.setWindowTitle(self.Title)


    def run(self,new_data):
        #new_data = read_data()
        if new_data == None:
            pass
        #这里要有文字说明连接失败
        else:
            data = new_data["data"][self.Title]
            print(self.Title+'获取正常')
            data = data.values[1:]

            self.dataX = [x for x in range(len(data))]
            self.dataY = [float(y) for y in data]

            self.canvas.plot(self.dataX, self.dataY)



#下面暂时不用
    def generateData(self):
        counter = 0
        while (True):
            if self.__exit:
                break

            if self.__generating:
                # newData = [random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX)]  #add new data here
                # newTime = [date2num(datetime.now()),date2num(datetime.now())]
                # self.dataX.append(newTime)
                # self.dataY.append(newData)

                self.dataX=[1,2,3,4,5,6,7,8]
                self.dataY=[random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX),random.randint(Y_MIN, Y_MAX)]

                func = interpolate.interp1d(self.dataX,self.dataY,kind='cubic')
                xnew = np.arange(1,8,0.1)
                ynew = func(xnew)
                self.canvas.plot(xnew, ynew)
                self.__generating = False

