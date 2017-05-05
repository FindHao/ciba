# coding: utf8
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5 import QtGui, QtCore
import PyQt5.uic
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from a_cat import Query
import sys
import signal
import re
import string

reg = re.compile('[' + string.punctuation + ' ]')
signal.signal(signal.SIGINT, signal.SIG_DFL)
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
        # self.setWindowFlags(QtCore.Qt.Desktop)
        self.player = QMediaPlayer()
        # 快捷键开启是否划词
        self.open = True

    def connects(self):
        """信号槽的连接"""
        # 当选中文字变化的时候，抓取释义
        self.clipboard.selectionChanged.connect(self.selection_changed)
        pass

    def refresh_window(self, text):
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

        self.setWindowTitle("search for:")
        self.search_words.setText(text)
        # 暂时先隐藏图标
        self.voice_play2.hide()
        self.voice_play1.hide()
        if len(self.query.word.voices) >= 2:
            self.voice_label1.setText(self.query.word.voices[0][0])
            self.voice_label2.setText(self.query.word.voices[1][0])
            # self.voice_play1.clicked.connect(lambda: self.play_voice(self.query.word.voices[0][1]))
            # self.voice_play2.clicked.connect(lambda: self.play_voice(self.query.word.voices[1][1]))
            self.play_voice(self.query.word.voices[1][1])
        elif len(self.query.word.voices) == 1:
            self.voice_label1.setText(self.query.word.voices[0][0])
            self.voice_play1.clicked.connect(lambda: self.play_voice(self.query.word.voices[0][1]))
            self.voice_label2.hide()
            self.play_voice(self.query.word.voices[0][1])
        else:
            self.voice_label1.setText("No voices found.")
            self.voice_label2.hide()
        base_info = ''
        for x in self.query.word.props:
            base_info += x + self.query.word.props[x] + '\n'
        self.base_infor_label.setText(base_info)

    def selection_changed(self):
        """剪切板的数据有变化"""
        # if not self.open:
        #     return False
        text = self.clipboard.text(QtGui.QClipboard.Selection)
        print(text.encode('utf8'))
        # 一个单词被切割成两行
        text = text.replace('- ', '')
        text = text.replace('-\n', '')
        text = text.replace('\n', ' ')
        # text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", " ", text)
        text2 = ''
        # 性能问题和不优雅问题
        for char in text:
            if '\u0020' <= char <= '\u007e':
                text2 += char
        text = text2
        # 增加对单词的判断
        ans = re.split(reg, text)
        ans2 = []
        for x in ans:
            if x != '':
                ans2.append(x)
        if len(ans2) == 1:
            text = ans2[0]
        print(text.encode('utf8'))
        if text:
            # todo:检查为什么不生效
            self.query.word.text = text
            self.query.get(text)
            self.setFocus()
            self.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.refresh_window(text)
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
        keyEvent = QKeyEvent(e)
        if keyEvent.key() == QtCore.Qt.Key_Escape:
            self.hide()

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
