# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import xlwt
import os
import csv


def csv_excel(csvfile, excel_name):
# 新建excel文件
    myexcel = xlwt.Workbook()
# 新建sheet页
    mysheet = myexcel.add_sheet('库存状态')
# 打开csv文件
    with open(csvfile, 'w', encoding='utf-8') as f:
# 读取文件信息
     data = csv.reader(f)
     row = 0
# 通过循环获取单行信息
    for line in data:
        column = 0
        while column < len(line):
            mysheet.write(row,column,line[column])
            if row == 0:
                style = fore_colour('aqua', 'on')
                mysheet.write(row, column, line[column], style)
            elif line[column] == '无货':
                style = fore_colour('yellow', 'off')
                mysheet.write(row, 1, line[1], style)
            elif len(line) < 4 or line[3] == '':
                style = fore_colour('red', 'off')
                mysheet.write(row, line[1], style)
            column = column + 1
        row = row + 1
# 最后保存到excel
    myexcel.save(excel_name)


def fore_colour(forecolour, bold):  # 可随意设置颜色，
    style = xlwt.easyxf(
        'pattern: pattern solid, fore_colour %s; font: bold %s;' % (
            forecolour, bold))
    return style


if __name__ == 'main':
    path = os.getcwd
    csvfile = path + '\excel.csv'
    excel_name = path + '\excel.xls'
    csv_excel()
    fore_colour()