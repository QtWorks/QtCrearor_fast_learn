#!/usr/bin/env python
#coding=utf-8

#include <QApplication>
#include "mainwindow.h"
#include <QTextCodec>

# int main(int argc, char *argv[])
import sys

from PyQt4.QtCore import QTextCodec
from PyQt4.QtGui import QApplication
from mainwindow import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    QTextCodec.setCodecForCStrings(QTextCodec.codecForName("UTF-8"))

    win = MainWindow()
    win.show()
    app.exec_()

