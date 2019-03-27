#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import os
import codecs
import json

proDir = os.path.dirname(__file__)
configPath = os.path.join(proDir, "config/config.ini")

class ReadConfig:

    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        """remove BOM：BOM签名的意思就是告诉编辑器当前文件采用何种编码，方便编辑器识别，
        但是BOM虽然在编辑器中不显示，但是会输出空行。开头的字节流就知道是否是UTF-8编码。
        bom_utf8比utf8多了3个字节前缀"""
        if data[:3] == codecs.BOM_UTF8:  # data[:3]列表数据切片，省略起始位置、步长，结束位置为3
            data = data[3:]  # 从文件的前3个来判断是否为BOM_UTF8，如果是，则从第3个开始取数
            file = codecs.open(configPath, "w")
            file.write(data)  # 如果是BOM编码，则去年前3个字节前缀后，重写文件"config.ini"
            file.close()
        fd.close()

        self.config = configparser.ConfigParser()  # 实例化读取ini文件的类
        self.config.read(configPath)

    def get_url(self, name):
        value = self.config.get("URL", name)  # ini文件读取操作
        return value

    def get_userinfo(self, name):
        value = self.config.get("LOGIN", name)  # ini文件读取操作
        return value

    def get_token(self):  # 获取线上Token
        value = self.config.get("TOKEN", "manage_access_token")
        return value

    def get_day(self):
        value = self.config.get("TOKEN", "day")
        return value

    def update_token(self, name, value):   # 修改线上token值
        self.config.set("TOKEN", name, value)
        with open(configPath, "w+") as f:
            self.config.write(f)



