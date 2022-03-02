# BrainFxxk-Compiler

## 概述

简易的BF语言编译器。

## 使用

1. 前置要求: GCC, Python3

2. 将bf2c.py和要编译的bf语言代码放在同一目录

3. 运行`python3 bf2c.py your_filename`，注意终端提示

## 原理

程序会首先将bf语言翻译成c语言，再调用gcc进行编译，最后运行。

## 实例

1. helloworld.bf 打印helloworld

更多的实例可参考[link](https://http://www.matrix67.com/blog/archives/168)