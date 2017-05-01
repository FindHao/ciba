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

# 安装和使用
`git clone`或者下载release的项目zip（推荐下载release，防止因我正在开发修改导致的bug），

安装依赖：

```shell
sudo apt-get install python3-pyqt5.qtmultimedia libqt5multimedia5-plugins
pip3 install -r requirements.txt
```
在项目目录下
```shell
python3 entry.py
```
# 常见问题
建议通过**双击**来划词。但是目前对标点符号不一定能准确处理，弹出窗口的标题栏有筛选出的结果，如果发现和所划单词不符，可以在文档里按住鼠标左键进行选中单词。
如有建议，请提issue。