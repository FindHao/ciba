## 2017-04-27 15:52:19
发现了类似的github项目[youdao-dict-for-ubuntu](https://github.com/idning/youdao-dict-for-ubuntu)
里面的思路不错，直接从xcopy找复制的文字
基础功能：
- [x] 获得选词
- [x] 抓取金山词霸或者有道的翻译
- [x] 抓取发音
- [x] 弹出窗口

http://nullege.com/codes/show/src%40p%40y%40pyqt5-HEAD%40examples%40tools%40customcompleter%40customcompleter.py/46/PyQt5.QtGui.QCursor/python 
这里面的textUnderCursor(self): 是真的指光标下面的文字吗？

## 2017-04-28 16:44:47

完成了突破。使用xlib模块，可以掌控窗口外的鼠标和键盘点击事件。

## 2017-04-29 09:37:46

鼠标的点击事件如何触发窗口的hide呢？回调？在mainframe里写个回调函数？

也不用考虑通信了，本身那个进程就是来监听鼠标事件的。
## 2017-04-29 15:12:12
弃用xlib方式获得鼠标点击事件。改用focusoutevent事件。同时增加了空结果的判断。

界面设计准备先固定内容

## bug:如果是在编辑器中按住鼠标选中的单词，则有问题。

暂时不考虑多个屏幕的问题。
问题：还是焦点问题。貌似现在点击标题栏也会hide。
## 2017-04-30 09:06:28
播放出现的错误：
```
libva info: VA-API version 0.39.4 libva info: va_getDriverName() returns 0 libva info: Trying to open /usr/lib/x86_64-linux-gnu/dri/i965_drv_video.so libva info: Found init function __vaDriverInit_0_39 libva info: va_openDriver() returns 0
```
卸载`gstreamer1.0-vaapi`包解决了错误，但是还是无法播放。
##　修复播放bug，因为player不在main frame里。
用pipreqs生成的requirements.txt
## 2017-04-30 15:08:33
在获取pdf里特殊字符的时候，如果直接获得text，肯定是处理过了特殊字符，比如引号可能是^[ ， ^B之类，那么B还是会凑成字符，导致无法识别。
可以加一个悬浮窗，来专门查词。（直接做成金山词霸那样子？）
### 16:50:55
在typora里，只要输入就会自动选择。
选中大段内容的时候，也不应该翻译。(通过text长度限制解决)
选中如果有中文，也不翻译。

## 2017-05-01 09:22:21

todo:



- [x] 对句子的翻译
- [ ] 主界面的设置
- [ ] 快捷键



偶尔会出现焦点丢失问题。
fuzzy 单词只有英音显示，但是读音美音。

## 2017-05-01 14:37:21
v0.0.3 添加对句子的支持。
疯狂更新了一波版本号。。
todo:
- [ ] 最前和最后的字符选择性删除
## 2017-05-02 14:32:14
heterogeneous 发音出现了几次问题

## 2017-05-03 09:38:14

 - [x] 将显示的内容从标题移到mainframe里
 - [ ] 测试将窗口属性改成popup
 - [x] exploite 单词导致崩溃 operating voltage decreases 也导致崩溃。

 ## 2017年05月04日10:49:52
 - [ ] 经常会出现只显示英文音标的情况。怀疑是页面格式变换导致
 - [ ] esc键应该可以hide窗口
 - [ ] 如果是大写的，是否可以加入小写的释义
 
 idea：通过检测变化的频率，来判断延迟请求。针对编辑器里的bug。而且，不应该检测变化，而是检测selection_changed事件的触发时间。
 master pdf editor选中没有检测到剪贴板的变化
 是否new窗口而不是show会解决此问题？