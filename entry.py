from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtGui
import PyQt5.uic
from a_cat import Query

(class_ui, class_basic_class) = PyQt5.uic.loadUiType('widget.ui')


class MainFrame(class_basic_class, class_ui):
    def __init__(self):
        super(MainFrame, self).__init__()
        # 使用qt自带的监听系统剪贴板的功能
        self.clipboard = QtGui.QGuiApplication.clipboard()
        self.setupUi(self)
        self.connects()
        # todo: 耦合性？？
        self.query = Query()

    def connects(self):
        """信号槽的连接"""
        # 当选中文字变化的时候，抓取释义
        self.clipboard.selectionChanged.connect(self.selection_changed)

        pass

    def selection_changed(self):
        """剪切板的数据有变化"""
        # todo: 将
        print(self.clipboard.text(QtGui.QClipboard.Selection))
        self.query.get(self.clipboard.text(QtGui.QClipboard.Selection))
        print(str(self.query.word))
        self.show()
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    widget = MainFrame()
    widget.hide()
    sys.exit(app.exec_())
