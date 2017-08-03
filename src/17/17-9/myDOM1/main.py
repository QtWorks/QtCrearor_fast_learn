#/usr/bin/env python
#coding=utf-8
from PyQt4.QtCore import QFile, QIODevice
from PyQt4.QtGui import QApplication
from PyQt4.QtXml import QDomDocument
import sys

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # 新建QDomDocument类对象，它代表一个XML文档
    doc = QDomDocument()
    _file = QFile("../myDOM1/my.xml")
    if not _file.open(QIODevice.ReadOnly):
        raise Exception("err")

    # 将文件内容读到doc中
    status, rrorMsg, errorLine, errorColumn = doc.setContent(_file)
    if not status:
        _file.close()
        raise Exception("err")
    _file.close()

    # firstChild 获得doc的第一个结点，即XML说明
    firstNode = doc.firstChild()

    #  输出XML说明,nodeName()为“xml”,nodeValue()为版本和编码信息
    print   firstNode.nodeName(), ":  ", firstNode.nodeValue()


    docelement = doc.documentElement()  # 返回根元素

    n = docelement.firstChild()  # 返回根节点的第一个子结点

    while (not n.isNull()):           #  如果结点不为空，则转到下一个节点
        if (n.isElement()):           # 如果结点是元素
                e = n.toElement()     # 将其转换为元素
                                      # 返回元素标记和id属性的值
        print  e.tagName() ,",  ",e.attribute("id")
        list = e.childNodes()        # 获得元素e的所有子结点的列表

        for i in  range(list.count()):  # // 遍历该列表
            node = list.at(i)
            if (node.isElement()):
                print  "   " ,node.toElement().tagName(), "   ",node.toElement().text()
        n = n.nextSibling()  # // 转到下一个兄弟结点

