# # # from selenium import webdriver
# # # from selenium.webdriver.support.wait import WebDriverWait as WW
# # # from selenium.webdriver.support import expected_conditions as EC
# # #
# # # flag = 1
# # # if flag == 11:
# # #     ...
# # #
# # #     driver = webdriver.Chrome()
# # #     driver.get('https://lxmusic.toside.cn/desktop')
# # #     eles = driver.find_elements('xpath',"//*[contains(text(),'软件变化')]")
# # #     for ele in eles:
# # #         print(ele.text)
# # #
# # #
# # # class A:
# # #     def __init__(self):
# # #        print(self.__class__.__name__)
# # #
# # # class B(A):
# # #     pass
# # #
# # # class C(B):
# # #     pass
# # #
# # #
# # # c = C()
# # #
# # #
# # #
# # # # import openpyxl
# # # # openpyxl.load_workbook()
# # #
# # # import sys
# # #
# # # a = set()
# # # print(sys.version,type(sys.version))
# # # print(sys.version_info,type(sys.version_info))
# # # print(sys.version_info[0:3])
# # # if sys.version_info[0:3] > (3,9,0,):
# # #     print('need update python')
# # # else:
# # #     print('good boy')
# # #
# # # a1 = (1,3,[2,3,(2,3)],9,1)
# # # a2 = (1,3,[2,3,(2,3)],9)
# # #
# # # print('a1 == a2 ? ', a1==a2)
# # #
# # # b = 'abdcee'
# # # print(b[0:3])
# # # for i in range(3):
# # #     print(i,end=' ')
# # #
# # # print()
# # # t = True
# # # x = 'A' if t is True else 'B'
# # # print(x)
# #
# # a = {'b':100,'c1':200,'a':99}
# # for i,j in a.items():
# #     print(i,j)
# #
# # print('*'*40)
# # for i,j in sorted(a.items()):
# #     print(i,j)
# #
# # # print(a)
# # print(sorted(a.items()),type(sorted(a.items())))
# #
# #
# # for i in [('a', 99), ('b', 100), ('c1', 200)]:
# #     print(i)
# #
# # for i,j in [('a', 99), ('b', 100), ('c1', 200)]:
# #     print(i,j)
#
#
# # def f1(): pass
# #
# # print(callable(f1))
# #
# #
# # class A:
# #     # @property
# #     def f2(self):
# #         return 'f2'
# #
# # print(callable(A.f2))
# # print(A().f2)
#
# #
# # a = None
# #
# # if a == 1:
# #     print("xxx")
# # else:
# #     print("yyy")
#
# # a = [6,8,3,5,3,3,3]
# # print(a.index(3))
#
#
# flag = 11
# if flag == 1:
#     ...
#
#     from openpyxl import load_workbook
#
#     wb = load_workbook("天工主机+OS+新线表.xlsx", data_only=True)  # type: load_workbook
#
#     print(wb.sheetnames)
#     sh = wb["新线资产汇总"]
#     print("最大行号：", sh.max_row)
#     # print(sh.columns)
#     # print(tuple(sh.columns)[0])
#     # for i in tuple(sh.columns)[0]:
#     #     print(i.value)
#
# flag = 11
# if flag == 1:
#     ...
#     l1 = [3, 5, 7, 2, 0]
#     l2 = [44, 66, 77]
#     index = l1.index(5)
#     print(index)
#     l1.append(l2)
#     print(l1)
#
# flag = 11
# if flag == 1:
#     ...
#     import openpyxl
#
#     # 生成一个 Workbook 的实例化对象，wb即代表一个工作簿（一个 Excel 文件）
#     wb = openpyxl.Workbook()
#     # 获取活跃的工作表，ws代表wb(工作簿)的一个工作表
#     ws = wb.active
#     # 接下来我们对新建的工作表ws命名，并向里面填入数据。
#     # 更改工作表ws的title
#     ws.title = 'test_sheet1'
#     # 对ws的单个单元格传入数据
#     ws['A1'] = '国家'
#     ws['B1'] = '首都'
#     data = {
#         '中国': '北京',
#         '韩国': '首尔',
#         '日本': '东京',
#         '泰国': '曼谷',
#         '马来西亚': '吉隆坡',
#         '越南': '河内',
#         '朝鲜': '平壤',
#         '印度': '新德里'
#     }
#     data_excel = []
#     for each in data:
#         data_excel.append([each, data[each]])
#     print(data_excel)
#
#     for each in data_excel:
#         ws.append(each)
#         # ws.cell(each)
#
#     # 保存Excel表格
#     wb.save('test.xlsx')
#
# flag = 1
# if flag == 1:
#     ...
#     # a =5
#     # if a == 10:
#     #     print("10")
#     # else:
#     #     if a == 5:
#     #         print("5")
#     #     else:
#     #         print("else")
#
#     a = [3, 5, 6, 8, 9]
#     b = [4, 7, '', 15, 14]
#     print(len(a))
#     d = 13
#     print(int(d/5), d%5)
#     max_len = len(a) if d%5 else 30-4
#     print(max_len)
#     # a.extend(b)
#     # print(a)
#     # print(a.index(15) )
#     #
#     # print(a.index(4))
#
#






