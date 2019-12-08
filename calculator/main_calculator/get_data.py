#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Simonmz"

from docx import Document


def r_format(result):
    # 除去岗位名称数据中的多余'/'
    for i in range(len(result)):
        for j in range(len(result[i])):
            # 分四次除去岗位列字符串中的"//"双斜杠
            result[i][j] = result[i][j].replace('//', '/')
            result[i][j] = result[i][j].replace('//', '/')
            result[i][j] = result[i][j].replace('//', '/')
            result[i][j] = result[i][j].replace('//', '/')
            # 去除岗位数据中末尾的'/'
            if result[i][j][-1] == '/':
                result[i][j] = result[i][j][:-1]
            # print(result[i][j])
    return result


def joint(result, t_column):
    for i in range(len(result)):
        str = '/'
        # 当岗位列为两列时
        if len(result[i]) == t_column + 1:
            result[i][0] = str.join([result[i][0], result[i][1]])
            del (result[i][1])
        # 当岗位列为三列时
        elif len(result[i]) == t_column + 2:
            result[i][0] = str.join([result[i][0], result[i][1], result[i][2]])
            del (result[i][2])
            del (result[i][1])
        # 当岗位列为四列时
        elif len(result[i]) == t_column + 3:
            result[i][0] = str.join([result[i][0], result[i][1], result[i][2], result[i][3]])
            del (result[i][3])
            del (result[i][2])
            del (result[i][1])
        # 当岗位列为五列时
        elif len(result[i]) == t_column + 4:
            result[i][0] = str.join([result[i][0], result[i][1], result[i][2], result[i][3], result[i][4]])
            del (result[i][4])
            del (result[i][3])
            del (result[i][3])
            del (result[i][1])
    return result


def get_data(w_path):
    # 获取word文件
    document = Document(w_path)
    # 获取word文件中的所有表格
    tables = document.tables
    # print(len(tables))
    # 获取化学因素检测表格
    result = []
    t_column = 0
    for table in tables:
        r_table = table.cell(1, -3)
        # 根据表格特点判断每个表格第一行倒数第三列是否为指定字符，可以判断是否为TWA化学因素表格
        if r_table.text in ['检测项目', '检测\n项目'] and len(table.columns) > 3:
            # 判断检测表格结果中是否含有日期
            if table.cell(1,-4).text in ['采样日期','采样\n日期','检测日期','检测\n日期']:
                t_column = 5
            else:
                t_column = 4
            # print('一共有{}列'.format(t_column))
            # 遍历所有行
            for row in table.rows[2:]:
                row_content = []
                # 每次循环都需要初始化tmp
                tmp = []
                # 遍历每行的所有单元格
                for cell in row.cells:
                    row_content.append(cell.text)
                # 取出每一行列表中的数据列的信息
                last_row = row_content[-(t_column-1):]
                # 去除岗位及危害因素列的重复数据
                for j in row_content[:-(t_column-1)]:
                    if j not in tmp:
                        tmp.append(j)
                # 将前面取出的数据列信息按项追加到每行的列表
                for k in last_row:
                    tmp.append(k)
                row_content = tmp
                # 将每行的整行列表追加到总数据列表，总数据列表为二位列表
                result.append(row_content)
            # 操作得到的数据，如果检测表中岗位列存在多列的情况，用“/”拼接成一个字符串
            result = joint(result, t_column)
    # 除去岗位名称数据中的多余'/'
    result = r_format(result)
    # 返回获得的数据和列数（用来判断是否含有检测时间列）
    return result, t_column
# get_data('C:/Users/simon/Desktop/ZJ[2019]046重庆长安汽车股份有限公司.docx')