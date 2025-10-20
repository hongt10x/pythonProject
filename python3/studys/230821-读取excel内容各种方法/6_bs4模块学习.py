# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：6_bs4模块学习.py
@Date    ：2024/4/10 11:15 
'''
import pprint
import re

from bs4 import BeautifulSoup as BS
import requests

flag = 11
if flag == 1:
    ...

    url = 'https://www.baidu.com'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'}
    r1 = requests.get(url,headers=header)
    # r1.encoding = 'gbk'
    print(r1.text)
    # bs1 = BS(r1.content,'lxml',from_encoding='gb2312')
    # print(bs1)
    # print(bs1.text)
    # print(bs1.meta)
    # print(bs1.meta.string)

flag = 11
if flag == 1:
    ...
    from bs4 import BeautifulSoup as BS

    from bs4 import BeautifulSoup

    # 构造一个网页数据
    html_doc = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <p class="title">
                <b>The Dormouse's story</b>
                <b>The Dormouse's story.....</b>
            </p>
            <p id="title">
                <b>The Dormouse's story ....</b>
            </p>

            <p class="story">Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister1 sister2" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.</p>

            <p class="story">...</p>
        </body>
    </html>
    """
    res = BS(html_doc,'lxml')
    flag = 1
    if flag == 1:
        ...

        # 获取标签
        print(res.a)
        # 获取标签内文本
        print(res.a.text)
        # 获取标签内属性
        print(res.a.attrs)
        # 获取指定属性值
        print(res.a.get('href'))
        print(res.a.get('id'))
        print(res.a.get('class'))
        # 获取子节点
        for _ in res.p.children:
            print(_)

        # 获取标签内部所有的元素
        print(res.p.contents)

    flag = 11
    if flag == 1:
        ...

        # print(res.p.parent)

        for i in res.p.parents:
            print(i)

    flag = 11
    if flag == 1:
        ...
        # 查找指定标签名的标签,默认只找符合条件的第一个
        # print(res.find(name='p'))
        # 查找具有某个特定属性的标签
        # 默认只找符合条件的第一个
        # print(res.find(name='p', id='title'))
        # 了解决关键字冲突
        # 会加下划线区分
        # print(res.find(name='p', class_='title'))
        # 使用attrs参数
        # 直接避免冲突
        print(res.find(name='p', attrs={'class':'title'}))

    flag = 11
    if flag == 1:
        ...
        print(res.find_all(name='a'))

    flag = 11
    if flag == 1:
        ...
        # css选择器
        # class .
        # print(res.select('.title'))
        # id #
        # 查看标签内部所有的后代span
        print(res.select('#title b'))
        print(res.select('#title *'))

flag = 11
if flag == 1:
    ...
    def main():
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.37'}

        baseurl = "https://movie.douban.com/top250?start="
        # import io
        # import sys
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码


        # 如果File - Settings - File Encodings - Global Encoding == utf-8 ,控制台在解码时应该不会出问题;如果时GBK,就是默认用中文解码,必须io输出是gb18030,才不会出现乱码!!!
        res = requests.get(url=baseurl, headers=head)
        res.encoding = 'utf-8'
        connect = res.text
        # print(connect)
        res = BS(connect, 'lxml')

        video = res.select('.grid_view li')
        # print(video[0])
        str1 =str2 = ''
        for i in video:
            # print(i)
            for item in i.select('.title'):
                print(item.text)
                str1 += item.text.replace('\xa0',' ')
                str2 += item.text
            print(str1)
            print(str2)
            break
            # ...
            # for item in i.select('.other'):
            #     print(item)

            # for item in i.select('.bd p'):
            #     # print(item)
            #     obj = re.compile('\d{4}', re.S)
            #     result = obj.finditer(item.text)
            #     for year in result:
            #         print(year.group())

            # for item in i.select(".rating_num"):
            #     print(item.text)

            # res = i.select('.star span')[-1].text
            # print(res,type(res))
            # print(res.replace('人评价',''))
            # print(i.select(".star span")[-1].text.replace("人评价", ""))

    main()

flag = 12
if flag == 1:
    ...
    from bs4 import BeautifulSoup

    def main():

        head = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

        baseurl = "https://movie.douban.com/top250?start="

        res = requests.get(url=baseurl, headers=head)

        connect = res.text

        res = BeautifulSoup(connect, 'lxml')

        video = res.select('.grid_view li')

        list = []

        for i in video:

            vidow = {
                "title": "",
                "year": "",
                "score": 0,
                "num": 0
            }

            for item in i.select('.title'):
                vidow['title'] += item.text.replace("\xa0", " ")

            for item in i.select('.other'):
                vidow['title'] += item.text.replace("\xa0", " ")

            for item in i.select(".bd p"):
                obj = re.compile('\d{4}', re.S)
                result = obj.finditer(item.text)
                for year in result:
                    vidow['year'] = year.group()

            for item in i.select(".rating_num"):
                vidow['score'] = item.text

            vidow['num'] = i.select(".star span")[-1].text.replace("人评价", "")

            list.append(vidow)

        pprint.pprint(list)


    main()


flag = 11
if flag == 1:
    ...
    html_doc = """
    <html><head><title>"c语言中文网"</title></head>
    <body>
    <p class="title"><b>c.biancheng.net</b></p>
    <p class="website">一个学习编程的网站
    <a href="http://c.biancheng.net/python/" id="link1">python教程</a>
    <a href="http://c.biancheng.net/c/" id="link2">c语言教程</a>
    """
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_doc, 'html.parser')
    # prettify()用于格式化输出html/xml文档
    print(soup.prettify())


flag = 11
if flag == 1:
    ...
    url = 'test.html'
    from bs4 import BeautifulSoup as bs
    res = bs(open(url),'lxml')
    # print(res.text)
    # print(res.select('.title b'))
    # print(res.select('.title'))
    # print(res.select('html'))
    #
    # se = res.select('.story')
    # print(se,type(se))
    # se2 = res.p.b
    # print(se2,type(se2))

    # 限制查询返回的条目数量，limit
    # print(res.find_all('p',limit=3))

    # 查找标签返回tag对象
    # for ele in res.find_all('p'):
    #     # print(ele,type(ele))
    #     # print(ele.text)
    #     print(ele.attrs)

    # 查询带有属性为class='story的标签内容
    # r1 = res.find_all(attrs={'class':'story'})
    # print(r1,type(r1))

    # ！！！！多个筛选，标签和属性结合；对于class属性需要用'class_'表示
    # print(res.find_all('p',class_='title'))
    # print(res.find_all(class_='story'))

    # 查找多个标签:默认从标签-->class属性
    # r2 = res.find_all('p','title1234')[0]
    # print(r2,type(r2))


    # r3 = res.select('p')[0]
    # print(r3,type(r3))

    # print(res.select('html'))
    # print(res.select('#halou'))

    r4 = res.select('.title')[0]
    # print(r4,type(r4))
    # print(r4.prettify())
    # print(r4.select('b'))
    # print(r4.select('#bb')[0].text)


print('\033[0;30;43m测试\033[0m')
print('\033[0;31;42m测试\033[0m')

print('\033[0;32;40m测试')
print('测试\033[0m')