# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : excel_os.py
@Time    : 2024/5/30 12:34
@Author  : Echo Wang
'''
import sys

from common.baseExcel import BaseExcel, show_time
import inspect
import time
from utils.handle_loguru import log


class Excel_OS(BaseExcel):
    def __init__(self):
        super().__init__()
        self.sh_os = self.wb[self.config[self.update_sheet]['sheetName']]
        self.os_update_info = self.config[self.update_sheet]['update_info']
        self.max_column = self.sh_os.max_column
        self.max_row = self.sh_os.max_row
        self.preset_head_value(self.os_update_info, self.sh_os, self.max_column)  # 预设列信息

    @show_time
    def update_datas_from_host(self):
        '''将主机表中独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)

    @show_time
    def update_datas_from_antivirus(self):
        '''将防病毒库中主机状态和独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)

    @show_time
    def update_datas_from_bastion(self):
        '''将堡垒机中独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)

    @show_time
    def update_datas_from_automation(self):
        '''将自动化中独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)

    @show_time
    def update_datas_from_titan(self):
        '''将青藤云中独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)

    @show_time
    def update_status_from_host(self):
        '''将ping状态数据更新到OS表中'''
        self.compare_status(self.sh_os)

    @show_time
    def update_status_from_ping(self):
        '''将ping状态数据更新到OS表中'''
        self.compare_status(self.sh_os)

    @show_time
    def update_status_from_recycle(self):
        '''将回收状态数据更新到OS表中'''
        self.compare_status(self.sh_os)

    @show_time
    def update_status_from_automation(self):
        '''将自动化状态数据更新到OS表中'''
        self.compare_status(self.sh_os)

    @show_time
    def update_status_from_titan(self):
        '''将青藤云主机状态数据更新到OS表中'''
        self.compare_status(self.sh_os)

    @show_time
    def update_status_from_antivirus(self):
        '''将防病毒状态数据更新到OS表中'''
        self.compare_status(self.sh_os)

    @show_time
    def update_status_from_bastion(self):
        '''将堡垒机状态数据更新到OS表中'''
        self.compare_status(self.sh_os)


if __name__ == '__main__':
    # with Excel_OS() as excel:
    #     excel.update_datas_from_host()
    # with Excel_OS() as excel:
    #     excel.update_datas_from_antivirus()
    # with Excel_OS() as excel:
    #     excel.update_datas_from_bastion()
    # with Excel_OS() as excel:
    #     excel.update_datas_from_titan()
    # with Excel_OS() as excel:
    #     excel.update_datas_from_automation()

    with Excel_OS() as excel:
        # excel.update_status_from_host()
        # excel.update_status_from_ping()
        # excel.update_status_from_antivirus()
        # excel.update_status_from_recycle()
        # excel.update_status_from_automation()
        excel.update_status_from_bastion()
