# ciba 词霸
基于python3 PyQt5写的一个简易划词翻译软件。

测试平台：Debian 9 x86_64

数据源取自金山词霸网页版。

# 功能
## 目前实现的功能

- 划词弹出翻译
- 翻译内容有音标和基本释义
- 弹出后自动发美音

## todo![](http://findicons.com/files/icons/2166/oxygen/32/kontact_todo.png)

- [ ] 更多内容的添加，比如例句等等
- [ ] 添加一个主界面
- [ ] 全局快捷键开启和关闭

# 安装和使用
`git clone`或者下载release的项目zip（推荐下载release，防止因我正在开发修改导致的bug），

安装依赖：

```shell
sudo apt-get install python3-pyqt5.qtmultimedia libqt5multimedia5-plugins
git clone git@github.com:FindHao/ciba.git
cd ciba/
# 建议使用虚拟环境，防止和外部环境冲突
virtualenv -p /usr/bin/python3 myenv
source myenv/bin/activate
pip3 install -r requirements.txt
```
在项目目录下
```shell
python3 entry.py
```

## 使用tips
 + 在弹出的释义窗口按下esc可以隐藏窗口，按下ctrl+c可以复制过滤了换行等特殊字符的字符串，ctrl+shift+c可以复制原生的字符串
 + 建议通过双击取词，在部分编辑器下，可能按住鼠标滑动取词有问题，如遇到，请提issue反馈
