# 如何使用html5slides来写Slides

David Xie

david.scriptfan@gmail.com

-------------------------------

### 安装

html5slides-markdown的安装非常简单, 跟普通的python包安装没有任何区别.

    python setup.py install

够了!

-------------------------------

### 书写Slides

一个完整的slides就是一个markdown文本, 具体的markdown语法, 请参考:
[Markdown Syntax](http://daringfireball.net/projects/markdown/syntax)

-------------------------------

### 如何翻页

1. 要开始新的一页, 只需要打上3个以上的'-'就可以了, 也就是html中的br标签
2. 每页的标题, 必须使用h3, 也就是只能用3个'#'

-------------------------------

### 代码高亮

这个也很简单, 使用markdown的code语法即可, 比如下面的代码:

    #!/usr/bin/env python
	#-*-coding:utf-8-*-
	if __name__ == '__main__':
	    print "hello, html5slides!"

-------------------------------

### 我需要一个例子

还是给我一个例子吧, 让我更清楚markdown怎么写

Markdown file: [example.md](https://raw.github.com/GDG-Xian/html5slides-markdown/master/example.md)

渲染后的结果: [example.html](http://gdg-xian.github.io/html5slides-markdown/example.html#1)

-------------------------------

### 我写好了markdown文本了, 下一步呢?

    givemeslides my.md > my.html

可以了, my.html就是你要的slides了, 用浏览器打开它吧!

--------------------------------

### 行动吧!

怎么样, 够简单, 够酷吧!

赶紧开始写Slides吧

--------------------------------

### 有问题怎么办?

1. 访问[html5slides](https://github.com/GDG-Xian/html5slides-markdown)来看文档
2. 如果遇到了bug, 请访问[Issues](https://github.com/GDG-Xian/html5slides-markdown/issues)
3. 给我发邮件, 地址: david.scriptfan@gmail.com

