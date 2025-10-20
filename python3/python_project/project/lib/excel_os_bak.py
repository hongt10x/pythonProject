# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : excel_os.py
@Time    : 2024/5/30 12:34
@Author  : Echo Wang
'''
import sys

from common.baseExcel import BaseExcel
import inspect
import time


class Excel_OS(BaseExcel):
    def __init__(self):
        super().__init__()
        self.sh_os = self.wb[self.config[self.update_sheet]['sheetName']]
        self.os_update_info = self.config[self.update_sheet]['update_info']
        self.max_column = self.sh_os.max_column
        self.max_row = self.sh_os.max_row
        self.preset_head_value(self.os_update_info, self.sh_os, self.max_column)  # 预设列信息

    def compare_datas1(self):
        # 获取被调用函数名,表等
        # print(inspect.stack()[1][3])
        sheet_info = inspect.stack()[1][3].split("_")[-1]
        sh = self.wb[self.config[sheet_info]['sheetName']]
        pattern = self.config[sheet_info]['pattern']
        if sheet_info == "antivirus":
            # 只拿这部分数据 [ "主机", "操作系统" ]
            pattern = self.config[sheet_info]['pattern'][3:]
        update_info = self.config[sheet_info]['update_info']
        # print(f"update_info: {update_info}")
        print(">>>开始将{!r}中的数据更新到{!r}中".format(sh.title, self.sh_os.title))
        # 获取索引
        pattern_indexs = self.get_index_list(pattern, sh)
        update_indexs = self.get_index_list(update_info, self.sh_os)
        print(f"  查询{sh.title}表中列项数据:{pattern}<-->列项索引:{pattern_indexs}")
        print(f"  更新{self.sh_os.title}表中列项数据:{update_info}<-->列项索引:{update_indexs}")
        # 获取比对列数据--目前设定为第一个元素
        sh_texts = self.get_col_values(pattern_indexs[0], pattern[0], sh)
        # 获取OS表第一、二列比对数据
        os_texts = self.get_col_values(self.os_indexs[0], self.os_pattern[0], self.sh_os)
        os_texts2 = self.get_col_values(self.os_indexs[1], self.os_pattern[1], self.sh_os)
        # print(f"os_texts: {os_texts}")
        # print(f"os_texts2: {os_texts2}")
        # print(f"sh_texts: {sh_texts}")
        # 将防病毒库中独有的数据更新到OS表中
        record_line = 1
        for num, value in enumerate(sh_texts):
            if value not in os_texts:
                # 如果未查到数据则获取第二列数据进行比对
                if value not in os_texts2:
                    for i, update_index in enumerate(update_indexs):
                        if update_index == update_indexs[-1]:
                            # 最后一列更新数据注明数据来源，行往后追加
                            self.sh_os.cell(row=self.max_row + record_line, column=update_index, value=sh.title)
                            break
                        #     从第2行开始取值
                        update_value = self.get_cell_value(row=num + 2, col=pattern_indexs[i], sh=sh)
                        # print(f"update_value1: {update_value}")
                        if sheet_info == 'host' and i == 2 and update_value:  # 对主机表的操作系统数据拼接
                            update_value = f"{update_value} {self.get_cell_value(row=num + 2, col=pattern_indexs[i + 1], sh=sh)}"
                        if sheet_info == 'automation' and i == 1 and update_value:  # 对自动化表的主机名数据拆分
                            update_value = f'{update_value.split("_")[0]}'
                        # print(f"update_value2: {update_value}")
                        self.sh_os.cell(row=self.max_row + record_line, column=update_indexs[i], value=update_value)
                    # 如果写入一行数据，行号hang向下移动一位
                    record_line += 1

        print("<<<表{!r}更新完毕".format(self.sh_os.title))

    def show_time(func):
        '''时间装饰器函数'''

        def inner(*args, **kwargs):
            start_time = time.monotonic()
            print(f"主体函数执行开始的时间: %.2f秒秒\n" % start_time)
            ret = func(*args, **kwargs)
            end_time = time.monotonic()
            print(f"主体函数执行结束的时间: %.2f秒秒\n" % start_time)
            print(f"  -->函数{func.__name__}调用后，执行总耗时：%.2f秒\n" % (end_time - start_time))
            return ret

        return inner

    def compare_match_datas(self):
        # 获取被调用函数名,表等
        # print(inspect.stack()[1][3])
        sheet_info = inspect.stack()[1][3].split("_")[-1]
        sh = self.wb[self.config[sheet_info]['sheetName']]
        pattern = self.config[sheet_info]['pattern']
        if sheet_info == "antivirus":
            # 只拿这部分数据 [ "主机", "操作系统" ]
            pattern = self.config[sheet_info]['pattern'][3:]
        update_info = self.config[sheet_info]['update_info']
        # print(f"update_info: {update_info}")
        print(">>>开始将{!r}中的数据更新到{!r}中".format(sh.title, self.sh_os.title))
        # 获取索引
        pattern_indexs = self.get_index_list(pattern, sh)
        update_indexs = self.get_index_list(update_info, self.sh_os)
        print(f"  查询{sh.title}表中列项数据:{pattern}<-->列项索引:{pattern_indexs}")
        print(f"  更新{self.sh_os.title}表中列项数据:{update_info}<-->列项索引:{update_indexs}")
        # 获取比对列数据--目前设定为第一个元素
        sh_texts = self.get_col_values(pattern_indexs[0], pattern[0], sh)
        # 获取OS表第一、二列比对数据
        os_texts = self.get_col_values(self.os_indexs[0], self.os_pattern[0], self.sh_os)
        os_texts2 = self.get_col_values(self.os_indexs[1], self.os_pattern[1], self.sh_os)
        # print(f"os_texts: {os_texts}")
        # print(f"os_texts2: {os_texts2}")
        # print(f"sh_texts: {sh_texts}")
        # 将防病毒库中独有的数据更新到OS表中
        record_line = 1
        for num, value in enumerate(sh_texts):
            if value not in os_texts:
                # 如果未查到数据则获取第二列数据进行比对
                if value not in os_texts2:
                    for i, update_index in enumerate(update_indexs):
                        if update_index == update_indexs[-1]:
                            # 最后一列更新数据注明数据来源，行往后追加
                            self.sh_os.cell(row=self.max_row + record_line, column=update_index, value=sh.title)
                            break
                        #     从第2行开始取值
                        update_value = self.get_cell_value(row=num + 2, col=pattern_indexs[i], sh=sh)
                        # print(f"update_value1: {update_value}")
                        if sheet_info == 'host' and i == 2 and update_value:  # 对主机表的操作系统数据拼接
                            update_value = f"{update_value} {self.get_cell_value(row=num + 2, col=pattern_indexs[i + 1], sh=sh)}"
                        if sheet_info == 'automation' and i == 1 and update_value:  # 对自动化表的主机名数据拆分
                            update_value = f'{update_value.split("_")[0]}'
                        # print(f"update_value2: {update_value}")
                        self.sh_os.cell(row=self.max_row + record_line, column=update_indexs[i], value=update_value)
                    # 如果写入一行数据，行号hang向下移动一位
                    record_line += 1

        print("<<<表{!r}更新完毕".format(self.sh_os.title))

    def update_datas_from_host(self):
        '''将主机表中独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)
    @show_time
    def update_datas_from_antivirus(self):
        '''将防病毒库中主机状态和独有的数据更新到OS表中'''
        self.compare_datas(self.sh_os, self.max_row)

    def update_datas_from_antivirus_bak(self):
        '''将防病毒库中主机状态和独有的数据更新到OS表中'''
        sheet_info = inspect.stack()[0][3].split("_")[-1]
        sh_antivirus = self.wb[self.config[sheet_info]['sheetName']]
        antivirus_pattern = self.config[sheet_info]['pattern']
        print(">>>开始将{!r}关联数据更新到{!r}中".format(sh_antivirus.title, self.sh_os.title))
        os_indexs = self.get_index_list(self.os_pattern, self.sh_os)  # 获取关键列索引
        antivirus_indexs = self.get_index_list(antivirus_pattern, sh_antivirus)  # 获取关键列索引
        # print(f"antivirus_indexs:{antivirus_indexs}")
        # 清理os目录已有关联防病毒的数据 ["防护状态", "版本信息" ]
        relate_antivirus_pattern = antivirus_pattern[1:3]
        clean_indexs = self.get_index_list(relate_antivirus_pattern, self.sh_os)
        self.clean_col_values(clean_indexs, relate_antivirus_pattern, self.sh_os)

        for num in range(len(antivirus_indexs)):
            if num > 0:
                break  # 只对一列进行匹配，仅循环一次
            #  拿到防病毒"IP地址"列数据
            anti_texts = self.get_col_values(antivirus_indexs[num], antivirus_pattern[num], sh_antivirus)
            # 重组列表数据，将一个单元格多值分开存储为独立元素，便于过滤
            new_anti_texts = self.recombine_texts(anti_texts, antivirus_pattern, sh_antivirus)
            # print(f"new_anti_texts:{new_anti_texts}")
            # 获取os某列全数据
            os_texts = self.get_col_values(os_indexs[num], self.os_pattern[num], self.sh_os)
            # print(f"os_texts:{os_texts}")
            # sys.exit(1)
            for num1, os_ip in enumerate(os_texts):
                # 将防病毒库中主机状态
                # print(f"old_ip:{os_ip}")
                if os_ip not in new_anti_texts.keys():
                    # 如果OS页的第一个ip不在防病毒页里，将ip置为第二个值进行重新赋值
                    os_ip = self.get_cell_value(row=num1 + 2, col=os_indexs[num + 1], sh=self.sh_os)
                    # print(f"new_ip:{os_ip}")
                if os_ip in new_anti_texts.keys():
                    # 如果OS页的第二个值在防病毒页进行比对更新
                    anti_value = new_anti_texts.get(os_ip)
                    # print(f"anti_value:{anti_value}")
                    # 更新数据
                    for idx in range(len(relate_antivirus_pattern)):
                        value = self.get_cell_value(row=anti_value, col=antivirus_indexs[idx + 1],
                                                    sh=sh_antivirus)
                        # print(f"value-{idx}-{anti_value}:{value}")
                        if value in self.os_update_info:
                            continue
                        # 匹配到后，立即更新单元格数据
                        self.sh_os.cell(row=num1 + 2, column=clean_indexs[idx], value=value)
        print("<<<表{!r}更新完毕".format(self.sh_os.title))
        # 将该表中存在但OS表没有的数据迁移到OS表中
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
        self.compare_status(self.sh_os, self.max_row)
    @show_time
    def update_status_from_ping(self):
        '''将ping状态数据更新到OS表中'''
        self.compare_status(self.sh_os, self.max_row)
    @show_time
    def update_status_from_recycle(self):
        '''将回收状态数据更新到OS表中'''
        self.compare_status(self.sh_os, self.max_row)
    @show_time
    def update_status_from_automation(self):
        '''将自动化状态数据更新到OS表中'''
        self.compare_status(self.sh_os, self.max_row)
    @show_time
    def update_status_from_titan(self):
        '''将青藤云主机状态数据更新到OS表中'''
        self.compare_status(self.sh_os, self.max_row)
    @show_time
    def update_status_from_antivirus(self):
        '''将防病毒状态数据更新到OS表中'''
        self.compare_status(self.sh_os, self.max_row)


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
        excel.update_status_from_host()
        excel.update_status_from_ping()
        excel.update_status_from_antivirus()
        excel.update_status_from_recycle()
        excel.update_status_from_automation()
