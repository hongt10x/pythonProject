# -*- coding: utf-8 -*-
'''
@Software: PyCharm
@Project : python39
@File    : excel_update_sheets.py
@Time    : 2024/6/14 15:22
@Author  : Echo Wang
'''
import sys

from common.baseExcel import BaseExcel, show_time
from utils.handle_loguru import log
import ipaddress


class Excel_Update_SheetInfos(BaseExcel):
    def __init__(self, flag=None):
        super().__init__(config_yml='configSheetInfos.yml')
        self.update_pattern = self.config['update_pattern']
        self.flag = flag
        print("flag: ", flag)
        sys.exit(1)

    @show_time
    def update_excel_sheets(self):
        values = []
        for sheetinfo in self.config.keys():
            if sheetinfo == 'update_pattern':
                continue
            if self.flag == 3 and sheetinfo in ["os", "host", "automation"]:  # 适配新线资产数据，跳过不需要比对的表
                continue
            sh_name = self.wb[self.config[sheetinfo]['sheetName']]
            pattern = self.config[sheetinfo]['pattern']
            refer_index = self.config[sheetinfo].get('refer_index')
            max_column = sh_name.max_column
            max_row = sh_name.max_row
            # print(f"{sheetinfo}的最大行数为{max_row}")
            self.preset_head_value(self.update_pattern, sh_name, max_column)  # 预设列信息
            pattern_index = self.get_index_list(pattern, sh_name)
            update_pattern_index = self.get_index_list(self.update_pattern, sh_name)
            self.clean_col_values(update_pattern_index, self.update_pattern, sh_name)
            print(
                f"\n\n  开始更新'{sh_name.title}'表中列项数据:{self.update_pattern}<-->列项索引:{update_pattern_index}")
            log.info(
                f"\n\n  开始更新'{sh_name.title}'表中列项数据:{self.update_pattern}<-->列项索引:{update_pattern_index}")
            delete_rows = []
            for row in range(2, max_row + 1):  # 逐行更新
                # print("  当前表{!r}，正在重组第{}行数据...".format(sheetinfo, row))
                values.clear()
                hostname = ""
                for r_index, p_index in enumerate(pattern_index[:-1]):
                    value = self.get_cell_value(row, p_index, sh_name)
                    if refer_index and refer_index == r_index:
                        if "titan" == sheetinfo:
                            value = value.replace("(连接)", "")
                        elif "automation" == sheetinfo:  # 取IP
                            value = value.split("_")
                            hostname = value[0]
                            try:
                                if len(value) == 2:
                                    hostname = value[0].strip()
                                elif len(value) == 3:  # 有些主机名格式为： Kylin_dihs0016.novalocal_10.2.203.67
                                    hostname = value[1].strip()
                            except:
                                ...
                            if len(value) > 1:
                                value = value[-1]
                    if value and type(value) is str:
                        values.extend(value.split())
                    elif value:
                        values.extend(list(value))
                datas = list(set(filter(lambda ip: False if not ip.startswith('10.') else ip, values)))
                try:

                    datas.sort(key=lambda ip: ipaddress.ip_address(ip))
                except Exception as err:
                    datas.sort()
                    log.info(f"[异常数据] 第{row}行:{err}")
                if not datas:
                    delete_rows.append(row)
                    log.info(f"[无效数据] 第{row}行:{self.get_row_values(row - 1, sh_name)}")
                    continue
                for i, u_index in enumerate(update_pattern_index):
                    if u_index == update_pattern_index[-1]:
                        if "automation" == sheetinfo:  # 更新主机名
                            sh_name.cell(row=row, column=u_index, value=hostname)
                        else:
                            value = self.get_cell_value(row, pattern_index[-1], sh_name)
                            try:
                                value = value.strip()
                            except:
                                ...
                            finally:
                                sh_name.cell(row=row, column=u_index, value=value)
                        continue
                    try:
                        sh_name.cell(row=row, column=u_index, value=datas[i])
                    except:
                        ...

            for delete_row in delete_rows[::-1]:  # 逆序从后往前删除，否则引起行上移后删错数据
                sh_name.delete_rows(delete_row)


if __name__ == '__main__':
    with Excel_Update_SheetInfos() as excel:
        excel.update_excel_sheets()
