from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtGui
import PyQt5.uic
from a_cat import Query
from record import *


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

    def refresh_window(self):
        """更新窗口的内容"""

        pass

    def selection_changed(self):
        """剪切板的数据有变化"""
        # todo: 将
        print(self.clipboard.text(QtGui.QClipboard.Selection))
        self.query.get(self.clipboard.text(QtGui.QClipboard.Selection))
        print(str(self.query.word))
        # self.show()
        pass

    # 这种方法只适用于当前这个窗口内
    def mousePressEvent(self, event):
        pass

    def keyPressEvent(self, e):
        pass


from multiprocessing import Process

def printf():
    print("在多进程下捕捉到了鼠标")
    record_dpy.record_enable_context(ctx, record_callback)

    # Finally free the context
    record_dpy.record_free_context(ctx)


if __name__ == '__main__':
    try:
        import sys
        p = Process(target=printf)
        p.start()

        app = QApplication(sys.argv)
        widget = MainFrame()
        widget.hide()
        p.join()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        p.terminate()
        sys.exit(app.exec_())


