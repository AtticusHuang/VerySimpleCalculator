import sys
from PyQt4 import QtCore, QtGui, uic

#前端

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(691, 888)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("./icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(128, 128))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.one = QtGui.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(10, 610, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.one.setFont(font)
        self.one.setObjectName(_fromUtf8("one"))
        self.two = QtGui.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(180, 610, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.two.setFont(font)
        self.two.setObjectName(_fromUtf8("two"))
        self.three = QtGui.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(350, 610, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.three.setFont(font)
        self.three.setObjectName(_fromUtf8("three"))
        self.four = QtGui.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(10, 500, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.four.setFont(font)
        self.four.setObjectName(_fromUtf8("four"))
        self.five = QtGui.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(180, 500, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.five.setFont(font)
        self.five.setObjectName(_fromUtf8("five"))
        self.six = QtGui.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(350, 500, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.six.setFont(font)
        self.six.setObjectName(_fromUtf8("six"))
        self.seven = QtGui.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(10, 390, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.seven.setFont(font)
        self.seven.setObjectName(_fromUtf8("seven"))
        self.eight = QtGui.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(180, 390, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eight.setFont(font)
        self.eight.setObjectName(_fromUtf8("eight"))
        self.nine = QtGui.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(350, 390, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nine.setFont(font)
        self.nine.setObjectName(_fromUtf8("nine"))
        self.zero = QtGui.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(10, 720, 331, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.zero.setFont(font)
        self.zero.setObjectName(_fromUtf8("zero"))
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(520, 500, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back.setFont(font)
        self.back.setObjectName(_fromUtf8("back"))
        self.clear = QtGui.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(520, 610, 161, 211))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.clear.setFont(font)
        self.clear.setObjectName(_fromUtf8("clear"))
        self.plus = QtGui.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(520, 280, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.plus.setFont(font)
        self.plus.setObjectName(_fromUtf8("plus"))
        self.minus = QtGui.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(350, 280, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus.setFont(font)
        self.minus.setObjectName(_fromUtf8("minus"))
        self.times = QtGui.QPushButton(self.centralwidget)
        self.times.setGeometry(QtCore.QRect(180, 280, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.times.setFont(font)
        self.times.setObjectName(_fromUtf8("times"))
        self.divided = QtGui.QPushButton(self.centralwidget)
        self.divided.setGeometry(QtCore.QRect(10, 280, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.divided.setFont(font)
        self.divided.setObjectName(_fromUtf8("divided"))
        self.equal = QtGui.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(520, 390, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equal.setFont(font)
        self.equal.setObjectName(_fromUtf8("equal"))
        self.displayProcess = QtGui.QLabel(self.centralwidget)
        self.displayProcess.setGeometry(QtCore.QRect(10, 30, 671, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(38)
        self.displayProcess.setFont(font)
        self.displayProcess.setObjectName(_fromUtf8("displayProcess"))
        self.dot = QtGui.QPushButton(self.centralwidget)
        self.dot.setGeometry(QtCore.QRect(350, 720, 161, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dot.setFont(font)
        self.dot.setObjectName(_fromUtf8("dot"))
        self.displayResults = QtGui.QLabel(self.centralwidget)
        self.displayResults.setGeometry(QtCore.QRect(10, 150, 671, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft YaHei UI"))
        font.setPointSize(38)
        self.displayResults.setFont(font)
        self.displayResults.setObjectName(_fromUtf8("displayResults"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 691, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.num_1 = QtGui.QAction(MainWindow)
        self.num_1.setObjectName(_fromUtf8("num_1"))
        self.num_2 = QtGui.QAction(MainWindow)
        self.num_2.setObjectName(_fromUtf8("num_2"))
        self.num_3 = QtGui.QAction(MainWindow)
        self.num_3.setObjectName(_fromUtf8("num_3"))
        self.num_4 = QtGui.QAction(MainWindow)
        self.num_4.setObjectName(_fromUtf8("num_4"))
        self.num_5 = QtGui.QAction(MainWindow)
        self.num_5.setObjectName(_fromUtf8("num_5"))
        self.num_6 = QtGui.QAction(MainWindow)
        self.num_6.setObjectName(_fromUtf8("num_6"))
        self.num_7 = QtGui.QAction(MainWindow)
        self.num_7.setObjectName(_fromUtf8("num_7"))
        self.num_8 = QtGui.QAction(MainWindow)
        self.num_8.setObjectName(_fromUtf8("num_8"))
        self.num_9 = QtGui.QAction(MainWindow)
        self.num_9.setObjectName(_fromUtf8("num_9"))
        self.num_0 = QtGui.QAction(MainWindow)
        self.num_0.setObjectName(_fromUtf8("num_0"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.dot_shortcut = QtGui.QAction(MainWindow)
        self.dot_shortcut.setObjectName(_fromUtf8("dot_shortcut"))
        self.equal_shortcut = QtGui.QAction(MainWindow)
        self.equal_shortcut.setObjectName(_fromUtf8("equal_shortcut"))
        self.plus_shortcut = QtGui.QAction(MainWindow)
        self.plus_shortcut.setObjectName(_fromUtf8("plus_shortcut"))
        self.minus_shortcut = QtGui.QAction(MainWindow)
        self.minus_shortcut.setObjectName(_fromUtf8("minus_shortcut"))
        self.times_shortcut = QtGui.QAction(MainWindow)
        self.times_shortcut.setObjectName(_fromUtf8("times_shortcut"))
        self.divided_shortcut = QtGui.QAction(MainWindow)
        self.divided_shortcut.setObjectName(_fromUtf8("divided_shortcut"))
        self.back_shortcut = QtGui.QAction(MainWindow)
        self.back_shortcut.setObjectName(_fromUtf8("back_shortcut"))
        self.clear_shortcut = QtGui.QAction(MainWindow)
        self.clear_shortcut.setObjectName(_fromUtf8("clear_shortcut"))
        self.menu.addAction(self.num_1)
        self.menu.addAction(self.num_2)
        self.menu.addAction(self.num_3)
        self.menu.addAction(self.num_4)
        self.menu.addAction(self.num_5)
        self.menu.addAction(self.num_6)
        self.menu.addAction(self.num_7)
        self.menu.addAction(self.num_8)
        self.menu.addAction(self.num_9)
        self.menu.addAction(self.num_0)
        self.menu.addSeparator()
        self.menu_2.addAction(self.dot_shortcut)
        self.menu_3.addAction(self.equal_shortcut)
        self.menu_3.addAction(self.plus_shortcut)
        self.menu_3.addAction(self.minus_shortcut)
        self.menu_3.addAction(self.times_shortcut)
        self.menu_3.addAction(self.divided_shortcut)
        self.menu_3.addAction(self.back_shortcut)
        self.menu_3.addAction(self.clear_shortcut)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "计算器", None))
        self.one.setText(_translate("MainWindow", "1", None))
        self.two.setText(_translate("MainWindow", "2", None))
        self.three.setText(_translate("MainWindow", "3", None))
        self.four.setText(_translate("MainWindow", "4", None))
        self.five.setText(_translate("MainWindow", "5", None))
        self.six.setText(_translate("MainWindow", "6", None))
        self.seven.setText(_translate("MainWindow", "7", None))
        self.eight.setText(_translate("MainWindow", "8", None))
        self.nine.setText(_translate("MainWindow", "9", None))
        self.zero.setText(_translate("MainWindow", "0", None))
        self.back.setText(_translate("MainWindow", "<--", None))
        self.clear.setText(_translate("MainWindow", "CE", None))
        self.plus.setText(_translate("MainWindow", "＋", None))
        self.minus.setText(_translate("MainWindow", "－", None))
        self.times.setText(_translate("MainWindow", "×", None))
        self.divided.setText(_translate("MainWindow", "÷", None))
        self.equal.setText(_translate("MainWindow", "＝", None))
        self.displayProcess.setText(_translate("MainWindow", "0", None))
        self.dot.setText(_translate("MainWindow", "·", None))
        self.displayResults.setText(_translate("MainWindow", "0", None))
        self.label.setText(_translate("MainWindow", "算式", None))
        self.label_2.setText(_translate("MainWindow", "结果", None))
        self.menu.setTitle(_translate("MainWindow", "数字", None))
        self.menu_2.setTitle(_translate("MainWindow", "符号", None))
        self.menu_3.setTitle(_translate("MainWindow", "操作", None))
        self.num_1.setText(_translate("MainWindow", "1", None))
        self.num_1.setShortcut(_translate("MainWindow", "1", None))
        self.num_2.setText(_translate("MainWindow", "2", None))
        self.num_2.setShortcut(_translate("MainWindow", "2", None))
        self.num_3.setText(_translate("MainWindow", "3", None))
        self.num_3.setShortcut(_translate("MainWindow", "3", None))
        self.num_4.setText(_translate("MainWindow", "4", None))
        self.num_4.setShortcut(_translate("MainWindow", "4", None))
        self.num_5.setText(_translate("MainWindow", "5", None))
        self.num_5.setShortcut(_translate("MainWindow", "5", None))
        self.num_6.setText(_translate("MainWindow", "6", None))
        self.num_6.setShortcut(_translate("MainWindow", "6", None))
        self.num_7.setText(_translate("MainWindow", "7", None))
        self.num_7.setShortcut(_translate("MainWindow", "7", None))
        self.num_8.setText(_translate("MainWindow", "8", None))
        self.num_8.setShortcut(_translate("MainWindow", "8", None))
        self.num_9.setText(_translate("MainWindow", "9", None))
        self.num_9.setShortcut(_translate("MainWindow", "9", None))
        self.num_0.setText(_translate("MainWindow", "0", None))
        self.num_0.setShortcut(_translate("MainWindow", "0", None))
        self.action_2.setText(_translate("MainWindow", "数字", None))
        self.dot_shortcut.setText(_translate("MainWindow", "点", None))
        self.dot_shortcut.setShortcut(_translate("MainWindow", ".", None))
        self.equal_shortcut.setText(_translate("MainWindow", "等于", None))
        self.equal_shortcut.setShortcut(_translate("MainWindow", "Return", None))
        self.plus_shortcut.setText(_translate("MainWindow", "加", None))
        self.plus_shortcut.setShortcut(_translate("MainWindow", "+", None))
        self.minus_shortcut.setText(_translate("MainWindow", "减", None))
        self.minus_shortcut.setShortcut(_translate("MainWindow", "-", None))
        self.times_shortcut.setText(_translate("MainWindow", "乘", None))
        self.times_shortcut.setShortcut(_translate("MainWindow", "*", None))
        self.divided_shortcut.setText(_translate("MainWindow", "除", None))
        self.divided_shortcut.setShortcut(_translate("MainWindow", "/", None))
        self.back_shortcut.setText(_translate("MainWindow", "退格", None))
        self.back_shortcut.setShortcut(_translate("MainWindow", "Backspace", None))
        self.clear_shortcut.setText(_translate("MainWindow", "清除", None))
        self.clear_shortcut.setShortcut(_translate("MainWindow", "Del", None))


#后端


displayList=[]#已输入的东西全部转换为字符串的形式
numbers=[]#所有输入了的数
symbols=[]#输入的数之中的符号
nowNumber=-1#现在要输入第几个数
nowSymbol=-1#现在要输入第几个符号
nowResult=0#当前的结果
lastHappen=""
decimalLength=0#当前数是小数时记录小数点后面有多少位数

# 123    +    123    -   123
#  ↑     ↑     ↑     ↑    ↑
# 数字0 符号0 数字1 符号1 数字2

class MyWindowClass(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        #按钮
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
        self.clear.clicked.connect(self.clear_c)
        self.plus.clicked.connect(self.plus_c)
        self.minus.clicked.connect(self.minus_c)
        self.times.clicked.connect(self.times_c)
        self.divided.clicked.connect(self.divided_c)
        self.equal.clicked.connect(self.equal_c)
        self.dot.clicked.connect(self.dot_c)

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
        self.clear_shortcut.triggered.connect(self.clear_c)
        self.plus_shortcut.triggered.connect(self.plus_c)
        self.minus_shortcut.triggered.connect(self.minus_c)
        self.times_shortcut.triggered.connect(self.times_c)
        self.divided_shortcut.triggered.connect(self.divided_c)
        self.equal_shortcut.triggered.connect(self.equal_c)
        self.dot_shortcut.triggered.connect(self.dot_c)
        
    def display(self,happend):
        global displayList,nowNumber,nowSymbol,nowResult,numbers,symbols,lastHappen
        lastHappen=happend
        j=0
        displayList=[]
        for i in range(0,nowNumber+1):
            displayList.append(str(numbers[i]))
            try:
                displayList.append(symbols[j])
            except:
                pass
            j+=1
        if(happend!="."):
            self.displayProcess.setText("".join(displayList))
        elif(happend=="." and nowNumber>nowSymbol):
            displayList.append(".")
            self.displayProcess.setText("".join(displayList))
        elif(nowNumber==nowSymbol):
            numbers.append(0)
            nowNumber+=1
            displayList.append("0")
            displayList.append(".")
            self.displayProcess.setText("".join(displayList))

        if(happend=="+" or happend=="-" or happend=="×" or happend=="÷" or happend=="."):
            pass#如果是加减乘除就不用改结果了
        else:
            if(nowNumber==0):
                nowResult=numbers[nowNumber]
                self.displayResults.setText(str(nowResult))#如果是第一个数就直接显示为第一个数
            else:
                nowResult=numbers[0]
                j=0
                for i in range(1,nowNumber+1):
                    if(symbols[j]=="+"):
                        nowResult+=numbers[i]
                    elif(symbols[j]=="-"):
                        nowResult-=numbers[i]
                    elif(symbols[j]=="×"):
                        nowResult*=numbers[i]
                    elif(symbols[j]=="÷"):
                        nowResult/=numbers[i]
                    j+=1
                if(nowResult==int(nowResult)):
                    self.displayResults.setText(str(int(nowResult)))
                else:
                    self.displayResults.setText(str(nowResult))
    
    def numberClicks(self,number):
        global nowNumber,numbers
        if(lastHappen=="+" or lastHappen=="-" or lastHappen=="×" or lastHappen=="÷" or lastHappen==""):
            numbers.append(number)
            nowNumber+=1
        if(lastHappen!="."):
            try:
                nowRealNumber=numbers[nowNumber]
            except:
                nowRealNumber=1
            if(lastHappen!="+" and lastHappen!="-" and lastHappen!="×" and lastHappen!="÷" and lastHappen!="" and nowRealNumber==int(nowRealNumber)):
                numbers[nowNumber]=numbers[nowNumber]*10+number
            elif(nowRealNumber==int(nowRealNumber)):
                pass
            else:
                numbers[nowNumber]+=number/(10**decimalLength)
        elif(numbers[nowNumber]==int(numbers[nowNumber])):
            numbers[nowNumber]+=number/10
        else:
            QtGui.QMessageBox.warning(self,"警告","一个数中不能有两个小数点!")
        self.display(str(number))
    def symbolClicks(self,symbol):
        global symbols,nowSymbol
        if(lastHappen!="+" and lastHappen!="-" and lastHappen!="×" and lastHappen!="÷" and lastHappen!=""):
            symbols.append(symbol)
            nowSymbol+=1
            self.display(symbol)
        elif(lastHappen==""):
            global numbers,nowNumber
            numbers.append(0)
            nowNumber+=1
            symbols.append(symbol)
            nowSymbol+=1
            self.display(symbol)
        else:
            symbols[nowSymbol]=symbol
            self.display(symbol)
    def one_c(self):
        self.numberClicks(1)
    def two_c(self):
        self.numberClicks(2)
    def three_c(self):
        self.numberClicks(3)
    def four_c(self):
        self.numberClicks(4)
    def five_c(self):
        self.numberClicks(5)
    def six_c(self):
        self.numberClicks(6)
    def seven_c(self):
        self.numberClicks(7)
    def eight_c(self):
        self.numberClicks(8)
    def nine_c(self):
        self.numberClicks(9)
    def zero_c(self):
        try:
            nowRealSymbols=symbols[nowSymbol]
        except:
            nowRealSymbols="1"
        if(nowRealSymbols!="÷"):
            self.numberClicks(0)
        else:
            QtGui.QMessageBox.warning(self,"警告","除数不能为零!\n如果需要输入小数,请先按.键")
    def back_c(self):
        global numbers,nowNumber,symbols,nowSymbol,lastHappen
        if(lastHappen=="+" or lastHappen=="-" or lastHappen=="×" or lastHappen=="÷"):
            del symbols[nowSymbol]
            nowSymbol-=1
            lastHappen=numbers[nowNumber]%10
        elif(lastHappen!="" and lastHappen!="."):
            numbers[nowNumber]=int(numbers[nowNumber]/10)
            if(numbers[nowNumber]%10!=0):
                lastHappen=numbers[nowNumber]%10
            else:
                lastHappen=symbols[nowSymbol]
                del numbers[nowNumber]
                nowNumber-=1
        elif(lastHappen=="."):
            lastHappen=numbers[nowNumber]%10
        self.display(lastHappen)
    def clear_c(self):
        global numbers,nowNumber,symbols,nowSymbol,lastHappen
        numbers=[]
        nowNumber=-1
        symbols=[]
        nowSymbol=-1
        lastHappen=""
        self.displayResults.setText("0")
        self.displayProcess.setText("0")
    def plus_c(self):
        self.symbolClicks("+")
    def minus_c(self):
        self.symbolClicks("-")
    def times_c(self):
        self.symbolClicks("×")
    def divided_c(self):
        self.symbolClicks("÷")
    def equal_c(self):
        global numbers,nowNumber,symbols,nowSymbol
        if(lastHappen=="+" or lastHappen=="-" or lastHappen=="×" or lastHappen=="÷"):
            nowResult=numbers[0]
            j=0
            for i in range(1,nowNumber+1):
                if(symbols[j]=="+"):
                    nowResult+=numbers[i]
                elif(symbols[j]=="-"):
                    nowResult-=numbers[i]
                elif(symbols[j]=="×"):
                    nowResult*=numbers[i]
                elif(symbols[j]=="÷"):
                    nowResult/=numbers[i]
                j+=1
            if(nowResult==int(nowResult)):
                numbers=[int(nowResult)]
                nowNumber=0
            else:
                numbers=[nowResult]
                nowNumber=0
            symbols=[lastHappen]
            nowSymbol=0
        elif(lastHappen!="" and lastHappen!="."):
            nowResult=numbers[0]
            j=0
            for i in range(1,nowNumber+1):
                if(symbols[j]=="+"):
                    nowResult+=numbers[i]
                elif(symbols[j]=="-"):
                    nowResult-=numbers[i]
                elif(symbols[j]=="×"):
                    nowResult*=numbers[i]
                elif(symbols[j]=="÷"):
                    nowResult/=numbers[i]
                j+=1
            if(nowResult==int(nowResult)):
                numbers=[int(nowResult)]
                nowNumber=0
            else:
                numbers=[nowResult]
                nowNumber=0
            symbols=[]
            nowSymbol=-1
        elif(lastHappen=="."):
            QtGui.QMessageBox.warning(self,"警告","请先把当前的数输入完")
        self.display(lastHappen)
    def dot_c(self):
        if(lastHappen==""):
            global numbers,nowNumber
            numbers.append(0)
            nowNumber+=1
        self.display(".")
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()