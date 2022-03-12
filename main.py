import sys
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("main.ui")[0]
first=[]
second=[]
fh=""
dzjt=3
    
class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #按钮单击
        self.one.clicked.connect(self.one_c)
        self.two.clicked.connect(self.two_c)
        self.three.clicked.connect(self.three_c)
        self.four.clicked.connect(self.four_c)
        self.five.clicked.connect(self.five_c)
        self.six.clicked.connect(self.six_c)
        self.seven.clicked.connect(self.seven_c)
        self.eight.clicked.connect(self.eight_c)
        self.nine.clicked.connect(self.nine_c)
        self.zero.clicked.connect(self.zero_c)
        self.back.clicked.connect(self.back_c)
        self.ce.clicked.connect(self.ce_c)
        self.jia.clicked.connect(self.jia_c)
        self.jian.clicked.connect(self.jian_c)
        self.cheng.clicked.connect(self.cheng_c)
        self.chu.clicked.connect(self.chu_c)
        self.equal.clicked.connect(self.equal_c)
        self.dian.clicked.connect(self.dian_c)
        #快捷键
        self.num_1.triggered.connect(self.one_c)
        self.num_2.triggered.connect(self.two_c)
        self.num_3.triggered.connect(self.three_c)
        self.num_4.triggered.connect(self.four_c)
        self.num_5.triggered.connect(self.five_c)
        self.num_6.triggered.connect(self.six_c)
        self.num_7.triggered.connect(self.seven_c)
        self.num_8.triggered.connect(self.eight_c)
        self.num_9.triggered.connect(self.nine_c)
        self.num_0.triggered.connect(self.zero_c)
        self.back_shortcut.triggered.connect(self.back_c)
        self.ce_shortcut.triggered.connect(self.ce_c)
        self.jia_shortcut.triggered.connect(self.jia_c)
        self.jian_shortcut.triggered.connect(self.jian_c)
        self.cheng_shortcut.triggered.connect(self.cheng_c)
        self.chu_shortcut.triggered.connect(self.chu_c)
        self.equal_shortcut.triggered.connect(self.equal_c)
        self.dian_shortcut.triggered.connect(self.dian_c)

    def addd(self,n):
        global fh,first,second
        if n!=0:
            if fh=="":
                first.append(n)
            else:
                second.append(n)
        else:
            if fh=="":
                if first!=[]:
                    first.append(n)
            else:
                if second!=[]:
                    first.append(n)

    def display(self):
        global fh
        lslb=[str(i) for i in first]
        lslbt=[str(i) for i in second]
        if fh=="":
            lslbth=lslb+lslbt
        else:
            lslb.append(fh)
            lslbth=lslb+lslbt
        lszf="".join(lslbth)
        self.dis.setText(lszf)
    
    #按扭单击以及快捷键按下反应

    def one_c(self):
        self.addd("1")
        self.display()
    def two_c(self):
        self.addd("2")
        self.display()
    def three_c(self):
        self.addd("3")
        self.display()
    def four_c(self):
        self.addd("4")
        self.display()
    def five_c(self):
        self.addd("5")
        self.display()
    def six_c(self):
        self.addd("6")
        self.display()
    def seven_c(self):
        self.addd("7")
        self.display()
    def eight_c(self):
        self.addd("8")
        self.display()
    def nine_c(self):
        self.addd("9")
        self.display()
    def zero_c(self):
        self.addd("0")
        self.display()
    def back_c(self):
        global fh,first,second
        if fh=="":
            dele=first.pop()
            times=0
            for quantity in first:
                times+=1
            if times==0:
                self.dis.setText("0")
        else:
            dele=second.pop()
            times=0
            for quantity in second:
                times+=1
            if times==0:
                self.dis.setText("0")
        self.display()
    def ce_c(self):
        global fh,first,second
        first=[]
        second=[]
        fh=""
        self.dis.setText("0")
    def jia_c(self):
        global fh
        fh="+"
        self.display()
    def jian_c(self):
        global fh
        fh="-"
        self.display()
    def cheng_c(self):
        global fh
        fh="*"
        self.display()
    def chu_c(self):
        global fh
        fh="/"
        self.display()
    def dian_c(self):
        self.addd(".")
        self.display()
    def equal_c(self):
        global fh,first,second

        if fh=="+":#符号是+
            disso="".join(first)
            try:
                disso=eval(disso)
            except:
                disso=0
            disst="".join(second)
            try:
                disst=eval(disst)
            except:
                disst=0
            diss=disso+disst
        
        elif fh=="-":#符号是-
            disso="".join(first)
            try:
                disso=eval(disso)
            except:
                disso=0
            disst="".join(second)
            try:
                disst=eval(disst)
            except:
                disst=0
            diss=disso-disst

        elif fh=="*":#符号是*
            disso="".join(first)
            try:
                disso=eval(disso)
            except:
                disso=0
            disst="".join(second)
            try:
                disst=eval(disst)
            except:
                disst=0
            diss=disso*disst

        elif fh=="/":#符号是/
            disso="".join(first)
            try:
                disso=eval(disso)
            except:
                disso=0
            disst="".join(second)
            try:
                disst=eval(disst)
            except:
                disst=0

            if disst!=0:#除数不为0
                diss=disso/disst
            
        else:
            diss=0

        if disst==0 and fh=="/":
            diss="0"
            self.ce_c()
            self.dis.setText("除数不能为零!")
        else:
            diss=str(diss)
            self.dis.setText(diss)
        first=[]
        second=[]
        if diss!="0":
            for i in diss:
                first.append(i)
        fh=""
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
