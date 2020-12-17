﻿# SCRAPY爬虫实验

## mingyan2

mingyan2主要爬取 http://lab.scrapyd.cn 里面的两个页面并保存为html格式，其实就是一个下载的过程，目的很单纯，主要是让诸位理解scrapy是怎样爬起来的，里面需要神马内脏，大家可以下了运行试试！

## simpleStartUrl

scrapy初始url的两种写法

## itemSpider

此项目爬取 http://lab.scrapyd.cn 里面的一条名言里的：名言内容、作者、标签，注意只是一条数据，然后保存为txt文档，这个练习，主要是学习scrapy css选择器的基本用法，然后结合scrapy shell 进行相应调试

## listSpider

此项目爬取 http://lab.scrapyd.cn 首页的所有名言，也就是列表爬取，主要学习如何使用：
```
for …… in ……

```
这个循环方式进行递归爬取，快试试吧！

## nextSpider

如果只能用scrpay爬取一页数据，其实和Ctrl+c、Ctrl+v没神马区别，真正拉开差距的是让scrapy自动的爬取多页，本项目寥寥几行代码，就能爬完整个网站，或许到这里你才能对它产生相见恨晚的赶脚！

## argSpider

此实例给大伙展示了Scrapy的灵活之处，我们可以在爬取的时候给蜘蛛喂不同的料，然后爬取不同的数据，比如不同的时间段、不同的标签、不同的域名……这些都是通过Scrapy的arguments实现，详情移步：[scrapy参数灵活应用](http://www.scrapyd.cn/doc/165.html)
