# coding: utf8
# 读取excel文件内容.py
# 2023/6/2

import xlrd
import os
import sys
from common.base_path import config_path, data_path
from utils.handle_yml import get_yml_data

class Read_Excel_Data:
    def __init__(self):
        self.excel_conf = get_yml_data(os.path.join(config_path, 'excel_config.yml'))
        print(self.excel_conf,type(self.excel_conf))
        self.file_path = os.path.join(data_path, self.excel_conf["filename"])
        self.col_names = self.excel_conf.get('col_names')
        self.sheet_names = self.excel_conf.get('sheet_names')
        self.wb = xlrd.open_workbook(self.file_path, formatting_info=True)


    def read_excel_data(self):
        run_sheet_names = {}
        if self.sheet_names:
            all_sheets = self.sheet_names.get('All')
            if all_sheets:
                col_names = all_sheets['col_names']
                self.sheet_names = run_sheet_names.fromkeys(self.wb.sheet_names(), {'col_names': col_names})
        else:
            # print('配置文件里，未正确配置Sheet页信息，请检查')
            raise "配置文件里，未正确配置Sheet页信息，请检查"


        for sheet_name, col_nums in self.sheet_names.items():
            sh = self.wb.sheet_by_name(sheet_name)
            for col_num in col_nums['col_nums']:
                list_col_nums = []
                sep_tip = '-'
                if sep_tip in col_num:
                    start, end = col_num.split(sep_tip)
                    for num in range(int(start),int(end)+1):
                        list_col_nums.append(num)
                else:
                    for num in col_num:
                        list_col_nums.append(int(num))
                print(list_col_nums)
            for one in list_col_nums:
                print(sh.col_values(one))


if __name__ == '__main__':
    obj = Read_Excel_Data()
    obj.read_excel_data()
