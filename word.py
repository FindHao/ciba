# coding: utf8
class Word:
    def __init__(self):
        # 查询的是什么
        self.text = ''
        # 存储发音和对应的音频下载地址
        self.voices = []
        # 存储基本示意，包括形容词，动词等词性
        # 存储形式： props['n.'] = ''
        self.props = {}
        # 变形
        self.changes = {}

    def __repr__(self):
        return "voices %s \n props: %s " % (str(self.voices), str(self.props))
