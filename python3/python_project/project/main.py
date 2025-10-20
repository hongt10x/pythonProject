# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : main.py
@Time    : 2024/6/5 14:31
@Author  : Echo Wang
'''

import sys


def help_info():
    print(
        """[旧线]数据比对，请执行：  python3 main.py 1
        [旧线]ping更新，请执行：  python3 main.py 2
        ---------------------------------------
        [新线]数据比对，请执行：  python3 main.py 3
        """
    )


try:
    from openpyxl import load_workbook
except:
    help_info()

from lib.excel_os import Excel_OS
from lib.excel_host import Excel_Host
from lib.excel_titan import Excel_Titan
from lib.excel_bastion import Excel_Bastion
from lib.excel_antivirus import Excel_Antivirus
from lib.excel_automation import Excel_Automation
from lib.excel_update_sheets import Excel_Update_SheetInfos
from lib.excel_newline import Excel_NewLine

if __name__ == '__main__':
    input_argv = int(sys.argv[1] if len(sys.argv) > 1 else 0)
    if input_argv == 1:
    # # 块儿执行顺序不能更改，否则可能引起数据异常；表格内部不要做筛选、冻结操作，会影响文件读取
    # # 对所有表进行数据校验，生成新的比对列数据
        with Excel_Update_SheetInfos() as excel:
            excel.update_excel_sheets()

        # # 将OS表中没有的数据更新到其他表--按表的量进行排序执行
        with Excel_Host() as excel:  # 主机表388
            excel.update_datas_from_os()
        with Excel_Automation() as excel:  # 自动化5401    3
            excel.update_datas_from_os()
        with Excel_Antivirus() as excel:  # 防病毒6320     4
            excel.update_datas_from_os()
        with Excel_Titan() as excel:  # 青藤云7747     2
            excel.update_datas_from_os()
        with Excel_Bastion() as excel:  # 堡垒机8461   1
            excel.update_datas_from_os()

        # # 将其他表比OS表多的数据更新到OS表，每个表更新完后立即保存，否则数据会覆盖
        with Excel_OS() as excel:
            excel.update_datas_from_host()
        with Excel_OS() as excel:
            excel.update_datas_from_automation()
        with Excel_OS() as excel:
            excel.update_datas_from_antivirus()
        with Excel_OS() as excel:
            excel.update_datas_from_titan()
        with Excel_OS() as excel:
            excel.update_datas_from_bastion()

        # # 将其他表中各种状态数据更新到OS表
        with Excel_OS() as excel:
            excel.update_status_from_host()
            excel.update_status_from_automation()
            excel.update_status_from_antivirus()
            excel.update_status_from_titan()
            excel.update_status_from_recycle()

    elif input_argv == 2:
        with Excel_OS() as excel:
            excel.update_status_from_ping()
    elif input_argv == 3:
        # 将输入信息传递到类中，便于识别执行方式
        with Excel_Update_SheetInfos(flag=input_argv) as excel:
            excel.update_excel_sheets()

        with Excel_NewLine() as excel:
            excel.update_datas_from_antivirus()
        with Excel_NewLine() as excel:
            excel.update_datas_from_titan()
        with Excel_NewLine() as excel:
            excel.update_datas_from_bastion()

        with Excel_NewLine() as excel:
            excel.update_status_from_antivirus()
            excel.update_status_from_titan()
            excel.update_status_from_bastion()
    else:
        help_info()
