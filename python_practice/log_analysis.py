# !/usr/bin/python2
# -*- coding: UTF-8 -*-
import os
import re
import xlwt


def get_data(file_name):
    action = []
    action_time = []
    with open(file_name, 'r', encoding='utf-8') as file_name:
        lines = file_name.readlines()
        for line in lines:
            info = re.match(
                r'^[0-9\:\s\/\,]{21}ACTION\s(\w{1,50})\s\[finished\][\w\:\s\=]{1,50}\=([0-9\.]{1,10})sec', line)
            if info:
                action.append(info.group(1))
                action_time.append(info.group(2))
        print(action, action_time)
        return action, action_time


def cal_time(action, action_time):
    # 查找集合中的重复元素
    all_action = set(action)
    action_data = [['run_num', 'action_name', 'avg_time']]
    for action_name in all_action:
        i = 0
        run_num = 0
        avg_time = 0
        for a in action:
            if a == action_name:
                run_num = run_num + 1
                avg_time = avg_time + float(action_time[i])
            i = i + 1
        avg_time = float('%.2f' % float(avg_time/run_num))
        action_data.append([run_num, action_name, avg_time])
    action_data = action_data[0:1] + sorted(action_data[1:len(action_data)])
    return action_data


def write_to_excel(sheet_name, action_info, excel_name):
    excel = xlwt.Workbook(encoding="ascii")
    table = excel.add_sheet(sheet_name, True)
    row = 0
    for item in action_info:
        column = 0
        while column < len(item):
            if row == 0:
                style = xlwt.easyxf('font:name Times New Roman,color-index red,bold on', num_format_str='#,##0.00')
                table.write(row, column, item[column], style)
            elif isinstance(item[column], float) and item[column] > 2:
                style = xlwt.easyxf('font:name Times New Roman,color-index blue,bold on', num_format_str='#,##0.00')
                table.write(row, column, item[column], style)
            else:
                style = xlwt.easyxf('font:name Times New Roman,color-index black,bold on', num_format_str='#,##0.00')
                table.write(row, column, item[column], style)
            column = column + 1
        row = row + 1
    excel.save(excel_name)


if __name__ == '__main__':
    path = os.getcwd()
    file_name = path + '\case_log.txt'
    sheet_name = 'action_avg_time'
    excel_name = path + '\ action_log.xls'
    action, action_time = get_data(file_name)
    action_info = cal_time(action, action_time)
    write_to_excel(sheet_name, action_info, excel_name)



