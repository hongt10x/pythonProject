# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : excel_bastion.py
@Time    : 2024/6/5 15:39
@Author  : Echo Wang
'''
from common.baseExcel import BaseExcel, show_time


class Excel_Bastion(BaseExcel):
    def __init__(self):
        super().__init__()
        self.update_sh = self.wb[self.config[self.update_sheet]['sheetName']]
        self.update_info = self.config[self.update_sheet]['update_info']
        self.max_column = self.update_sh.max_column
        self.preset_head_value(self.update_info, self.update_sh, self.max_column)  # 预设列信息

    @show_time
    def update_datas_from_os(self):
        self.compare_datas_other(self.update_sh)


if __name__ == '__main__':
    with Excel_Bastion() as excel:
        excel.update_datas_from_os()
