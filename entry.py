from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5 import QtGui, QtCore
import PyQt5.uic
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from a_cat import Query
import sys

(class_ui, class_basic_class) = PyQt5.uic.loadUiType('widget.ui')

class MainFrame(class_basic_class, class_ui):
    def __init__(self):
        super(MainFrame, self).__init__()
        # 使用qt自带的监听系统剪贴板的功能
        self.clipboard = QtGui.QGuiApplication.clipboard()
        self.setupUi(self)
        self.connects()
        # 这里还没太理解，主要是解决了focusoutevent事件不响应的bug
        self.setFocus()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        # todo: 耦合性？？
        self.query = Query()

        self.player = QMediaPlayer()

    def connects(self):
        """信号槽的连接"""
        # 当选中文字变化的时候，抓取释义
        self.clipboard.selectionChanged.connect(self.selection_changed)
        pass

    def refresh_window(self):
        """更新翻译的显示"""
        # 设置位置和大小
        self.setFixedSize(400, 300)
        cur = QtGui.QCursor.pos()
        x = cur.x() + 20
        y = cur.y() + 20
        # 如果超出了屏幕边界，便显示在里面
        window_h = QDesktopWidget().screenGeometry().height()
        window_w = QDesktopWidget().screenGeometry().width()
        if x + 400 > window_h or y + 300 > window_w:
            x -= 20 + 400
            y -= 20 + 300
        self.move(x, y)

        self.setWindowTitle("search for: %s" % self.clipboard.text(QtGui.QClipboard.Selection))
        # todo: 如果没有显示结果，需要提示

        if len(self.query.word.voices) >= 2:
            self.voice_label1.setText(self.query.word.voices[0][0])
            self.voice_label2.setText(self.query.word.voices[1][0])
            self.voice_play1.clicked.connect(lambda: self.play_voice(self.query.word.voices[0][1]))
            self.voice_play2.clicked.connect(lambda: self.play_voice(self.query.word.voices[1][1]))
            self.play_voice(self.query.word.voices[1][1])
        elif len(self.query.word.voices) == 1:
            self.voice_label1.setText(self.query.word.voices[0][0])
            self.voice_play1.clicked.connect(lambda: self.play_voice(self.query.word.voices[0][1]))
            self.voice_label2.hide()
            self.voice_play2.hide()
            self.play_voice(self.query.word.voices[0][1])
        base_info = ''
        for x in self.query.word.props:
            base_info += x + self.query.word.props[x] + '\n'
        self.base_infor_label.setText(base_info)

    def selection_changed(self):
        """剪切板的数据有变化"""
        # todo: 将
        print(self.clipboard.text(QtGui.QClipboard.Selection))
        if self.clipboard.text(QtGui.QClipboard.Selection):
            self.query.get(self.clipboard.text(QtGui.QClipboard.Selection))
            self.setFocus()
            self.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.refresh_window()
            self.show()

    def play_voice(self, url):
        """播放音频"""
        content = QMediaContent(QtCore.QUrl(url))
        self.player.setMedia(content)
        print(url)
        self.player.play()

    def focusOutEvent(self, event):
        """窗口焦点不在当前的翻译窗口时，窗口隐藏起来"""
        self.hide()
        print(event)
        pass

    # 这种方法只适用于当前这个窗口内
    def mousePressEvent(self, event):
        pass

    def keyPressEvent(self, e):
        pass

    def closeEvent(self, e):
        """隐藏窗口到后台"""
        self.hide()
        e.ignore()


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        widget = MainFrame()
        widget.hide()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        sys.exit(app.exec_())
