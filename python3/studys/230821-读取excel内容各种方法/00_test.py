# -*- coding: UTF-8 -*-
'''
@Project ：python3 
@File    ：00_test.py
@Date    ：2024/4/9 14:02 
'''


# import sys
#
# print(len(sys.argv))
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])


import win32com.client as win32

def openWorkbook(xlapp, xlfile):
    try:
        xlwb = xlapp.Workbooks(xlfile)
    except Exception as e:
        # pass
        # xlwb = None
        try:
            xlwb = xlapp.Workbooks.Open(xlfile)
        except Exception as e:
            print(e)
            xlwb = None
    return(xlwb)

try:
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    wb = openWorkbook(excel, r'D:\PythonStudy\python3\230821-读取excel内容各种方法/t1.xlsx')
    ws = wb.Worksheets('Sheet1')
    # excel.Visible = True

except Exception as e:
    print(e)

finally:
    # RELEASES RESOURCES
    ws = None
    wb = None
    excel = None

if __name__ == '__main__':
    import re
    s = '\xa0/\xa0\xa0\xa0 The Shawshank Redemption '
    # print(s)
    # s.replace(u'\xa0','')
    # print(s)

    d1 = {'k1':'中国人','k2':'chinese'}
    import json
    print(json.dumps(d1))
    print(json.dumps(d1,ensure_ascii=False))


    class User:
        info: str

        @property
        def data(self) -> dict:
            print("data")
            ...

        def get_record(self):
            print("get_record")
            ...
        def set_record(self,value):
            print("set_record: %s" % value)
            ...

        use2 = property(fget=get_record, fset=set_record)
    user = User()
    user.data
    user.use2
    user.use2 = "xx"


