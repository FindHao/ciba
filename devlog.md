## 2017-04-27 15:52:19
发现了类似的github项目[youdao-dict-for-ubuntu](https://github.com/idning/youdao-dict-for-ubuntu)
里面的思路不错，直接从xcopy找复制的文字
基础功能：
- [ ] 获得选词
- [ ] 抓取金山词霸或者有道的翻译
- [ ] 抓取发音
- [ ] 弹出窗口

http://nullege.com/codes/show/src%40p%40y%40pyqt5-HEAD%40examples%40tools%40customcompleter%40customcompleter.py/46/PyQt5.QtGui.QCursor/python 
这里面的textUnderCursor(self): 是真的指光标下面的文字吗？

## 2017-04-28 16:44:47

完成了突破。使用xlib模块，可以掌控窗口外的鼠标和键盘点击事件。