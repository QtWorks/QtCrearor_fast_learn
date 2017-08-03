#!/usr/bin/env python
# coding=utf-8

from PyQt4 import uic
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import QFile
from PyQt4.QtCore import QIODevice
from PyQt4.QtCore import QString
from PyQt4.QtCore import QTextStream
from PyQt4.QtGui import QDialog
from PyQt4.QtXml import QDomDocument
from PyQt4.QtXml import QDomProcessingInstruction
from PyQt4.QtXml import QDomText


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__(None)
        uic.loadUi("./mainwindow.ui",self)

        doc = QDomDocument()
        # 添加处理指令即XML说明
        instruction = QDomProcessingInstruction()
        instruction = doc.createProcessingInstruction("xml", "version=\"1.0\" encoding=\"UTF-8\"")
        doc.appendChild(instruction)

        # 添加根元素
        root = doc.createElement(QString("书库"))
        doc.appendChild(root)         # 添加根元素

        # 添加第一个图书元素及其子元素
        book = doc.createElement(QString("图书"))
        id = doc.createAttribute(QString("编号"))
        title = doc.createElement(QString("书名"))
        author = doc.createElement(QString("作者"))
        text = QDomText()

        id.setValue(QString("1"))
        book.setAttributeNode(id)
        text = doc.createTextNode(QString("Qt"))
        title.appendChild(text)
        text = doc.createTextNode(QString("shiming"))
        author.appendChild(text)
        book.appendChild(title)   # 图书元素 添加 书名元素
        book.appendChild(author)  # 图书元素 添加 作者元素
        root.appendChild(book)  # 根元素 添加 图书元素

        # 添加第二个图书元素及其子元素
        book = doc.createElement(QString("图书"))
        id = doc.createAttribute(QString("编号"))
        title = doc.createElement(QString("书名"))
        author = doc.createElement(QString("作者"))

        id.setValue(QString("2"))
        book.setAttributeNode(id)
        text = doc.createTextNode(QString("Linux"))
        title.appendChild(text)
        text = doc.createTextNode(QString("yafei"))
        author.appendChild(text)
        book.appendChild(title)
        book.appendChild(author)
        root.appendChild(book)

        file = QFile("my.xml")
        if (not file.open(QIODevice.WriteOnly | QIODevice.Truncate)):
            raise Exception("open my.xml Err")
        out = QTextStream(file)
        doc.save(out, 4)  # 将文档保存到文件，4为子元素缩进字符数
        file.close()

    # # MainWindow::~MainWindow()
    #
    #     delete ui
    #

    # /* 显示全部按钮 */
    def on_pushButton_5_clicked(self):

        self.listWidget.clear()  # 先清空显示

        file = QFile("my.xml")
        if (not file.open(QIODevice.ReadOnly)):
            raise Exception("open my.xml Err")
        doc = QDomDocument()
        status, rrorMsg, errorLine, errorColumn = doc.setContent(file)
        if (not status):
            file.close()
            raise Exception(str(rrorMsg))
        file.close()

        docElem = doc.documentElement()  # 返回根元素

        n = docElem.firstChild()
        while (not n.isNull()):
            if (n.isElement()):
                e = n.toElement()
                self.listWidget.addItem(e.tagName() + e.attribute(QString("编号")))
                list = e.childNodes()
                for i in range(list.count()):
                    node = list.at(i)
                    if (node.isElement()):
                        self.listWidget.addItem("   " + node.toElement().tagName()
                                                + " : " + node.toElement().text())
            n = n.nextSibling()

    # 添加按钮
    def on_pushButton_4_clicked(self):

        # 我们先清空显示，然后显示“无法添加！”，这样如果添加失败则会显示“无法添加！”
        self.listWidget.clear()
        self.listWidget.addItem(QString("无法添加！"))
        file = QFile("my.xml")
        if (not file.open(QIODevice.ReadOnly)):
            raise Exception("open my.xml Err")
        doc = QDomDocument()

        status, rrorMsg, errorLine, errorColumn = doc.setContent(file)
        if not status:
            file.close()
            raise Exception(str(rrorMsg))

        file.close()
        root = doc.documentElement()  # 获取根元素
        book = doc.createElement(QString("图书"))
        id = doc.createAttribute(QString("编号"))
        title = doc.createElement(QString("书名"))
        author = doc.createElement(QString("作者"))
        text = QDomText()

        # 我们获得了最后一个孩子结点的编号，然后加1，便是新的编号
        num = root.lastChild().toElement().attribute(QString("编号"))
        count = num.toInt() + 1
        id.setValue(QString.number(count))

        book.setAttributeNode(id)
        text = doc.createTextNode(self.lineEdit_2.text())
        title.appendChild(text)
        text = doc.createTextNode(self.lineEdit_3.text())
        author.appendChild(text)
        book.appendChild(title)
        book.appendChild(author)
        root.appendChild(book)

        if (not file.open(QIODevice.WriteOnly | QIODevice.Truncate)):
            raise Exception("file open Err")

        out = QTextStream(file)
        doc.save(out, 4)
        file.close()
        # 最后更改显示为“添加成功！”
        self.listWidget.clear()
        self.listWidget.addItem(QString("添加成功！"))

    # 对XML文档进行查找、更新和删除操作
    def doXml(self, operate):

        self.listWidget.clear()
        self.listWidget.addItem(QString("没有找到相关内容！"))
        file = QFile("my.xml")
        if (not file.open(QIODevice.ReadOnly)):
            raise Exception("open file Err")
        doc = QDomDocument()
        status, rrorMsg, errorLine, errorColumn = doc.setContent(file)
        if (not status):
            file.close()
            raise Exception(str(rrorMsg))
        file.close()

        # 以标签名进行查找
        list = doc.elementsByTagName(QString("图书"))  # 获取所有图书元素的列表

        for i in range(list.count()):
            e = list.at(i).toElement()
            if (e.attribute(QString("编号")) == self.lineEdit.text()):
                # 如果元素的“编号”属性值与我们所查的相同
                if (operate == "delete"):  # 如果是删除操作
                    root = doc.documentElement()
                    # 从根节点上删除该节点
                    root.removeChild(list.at(i))
                    file = QFile("my.xml")
                    if (not file.open(QIODevice.WriteOnly | QIODevice.Truncate)):
                        raise Exception("open file Err")
                    out = QTextStream(file)
                    doc.save(out, 4)
                    file.close()
                    self.listWidget.clear()
                    self.listWidget.addItem(QString("删除成功！"))
                elif operate is "update":
                    # 如果是更新操作
                    child = list.at(i).childNodes()
                    # 将它子节点的首个子节点（就是文本节点）的内容更新
                    child.at(0).toElement().firstChild().setNodeValue(self.lineEdit_2.text())
                    child.at(1).toElement().firstChild().setNodeValue(self.lineEdit_3.text())
                    file = QFile("my.xml")
                    if (not file.open(QIODevice.WriteOnly | QIODevice.Truncate)):
                        raise Exception("Open file Err")
                    out = QTextStream(file)
                    doc.save(out, 4)
                    file.close()
                    self.listWidget.clear()
                    self.listWidget.addItem(QString("更新成功！"))
                elif operate is "find":
                    # 如果是查找操作
                    self.listWidget.clear()
                    self.listWidget.addItem(e.tagName() + e.attribute(QString("编号")))
                    list = e.childNodes()
                    for i in range(list.count()):

                        node = list.at(i)
                        if (node.isElement()):
                            self.listWidget.addItem("   "
                                                    + node.toElement().tagName() + " : "
                                                    + node.toElement().text())
    # 查找按钮
    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.doXml("find")

    # 删除按钮
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        self.fdoXml("delete")

    # 更新按钮
    @pyqtSlot()
    def on_pushButton_3_clicked(self):
        self.doXml("update")
