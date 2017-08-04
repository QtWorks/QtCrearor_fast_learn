#################
16. 模型/视图编程
#################

16.1 模型/视图架构
==================

16.1.1 组成部分
---------------

1). 模型
^^^^^^^^
2). 视图
^^^^^^^^
3). 委托
^^^^^^^^

16.1.2 简单的例子
-----------------

.. literalinclude:: ../../../src/16/16-1/modelView1/main.cpp
    :language: cpp
    :encoding: utf-8



16.2 模型类
===========

16.2.1 基本概念
---------------

.. literalinclude:: ../../../src/16/16-2/modelView1/main.cpp
    :language: cpp
    :encoding: utf-8


16.2.2 创建新的模型
-------------------


1.   
^^^^^^^^^^^^^^


.. literalinclude:: ../../../src/16/16-3/myModel/stringlistmodel.cpp
    :language: cpp
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-3/myModel/main.cpp
    :language: cpp
    :encoding: utf-8

2.   
^^^^^^^^^^^^^^


.. literalinclude:: ../../../src/16/16-4/myModel/stringlistmodel.cpp
    :language: cpp
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-4/myModel/main.cpp
    :language: cpp
    :encoding: utf-8

3.   
^^^^^^^^^^^^^^

.. literalinclude:: ../../../src/16/16-5/myModel/stringlistmodel.cpp
    :language: cpp
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-5/myModel/main.cpp
    :language: cpp
    :encoding: utf-8


16.3 视图类
===========

16.3.1 基本概念
---------------

16.3.2 处理项目选择
-------------------


.. literalinclude:: ../../../src/16/16-6/mySelection/mainwindow.cpp
    :language: cpp
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-6/mySelection/main.cpp
    :language: cpp
    :encoding: utf-8



**QTiemSelectionModel::Toggle**

.. literalinclude:: ../../../src/16/16-7/mySelection/mainwindow.cpp
    :language: cpp
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-7/mySelection/main.cpp
    :language: cpp
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-8/mySelection/mainwindow.cpp
    :language: cpp
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-8/mySelection/main.cpp
    :language: cpp
    :encoding: utf-8



16.4 委托类
===========

16.4.1 基本概念
---------------

16.4.2 自定义委托
-----------------

.. literalinclude:: ../../../src/16/16-9/mySelection/mainwindow.cpp
    :language: cpp
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-9/mySelection/spinboxdelegate.cpp
    :language: cpp
    :encoding: utf-8


.. literalinclude:: ../../../src/16/16-9/mySelection/main.cpp
    :language: cpp
    :encoding: utf-8


16.5 项目视图的便捷类
=====================

16.5.1 QListWidget
------------------

16.5.2 QTreeWidget
------------------

16.5.3 QTableWidget
-------------------

16.6 在项目视图中启用拖放
=========================

16.6.1 在便捷类中启用拖放
-------------------------

.. literalinclude:: ../../../src/16/16-11/modelView2/main.cpp
    :language: cpp
    :encoding: utf-8


16.6.2 在模型/视图类中启用拖放
------------------------------

.. literalinclude:: ../../../src/16/16-12/myModel/main.cpp
    :language: cpp
    :encoding: utf-8


16.7 其他内容
=============

16.7.1 代理模型
---------------

.. literalinclude:: ../../../src/16/16-13/myProxyModel/mainwindow.cpp
    :language: cpp
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-13/myProxyModel/main.cpp
    :language: cpp
    :encoding: utf-8

16.7.2 数据-窗口映射器
----------------------

.. literalinclude:: ../../../src/16/16-14/myMapper/mainwindow.cpp
    :language: cpp
    :encoding: utf-8

.. literalinclude:: ../../../src/16/16-14/myMapper/main.cpp
    :language: cpp
    :encoding: utf-8

16.8 小结
=========

