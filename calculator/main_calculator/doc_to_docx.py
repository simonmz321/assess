#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Simonmz"

import os
from win32com import client


# w_path.split('.')[-1] == 'doc':
def doc_to_docx(w_path):
    str_path = os.path.splitext(w_path)[1]
    tmp_path = w_path
    # print(str_path)
    # print(w_path)
    if str_path == ".doc":
        word = client.Dispatch('Word.Application')
        w_path = w_path.replace("/", "\\")
        # print(w_path)
        doc = word.Documents.Open(w_path)  # 目标路径下的文件
        doc.SaveAs(os.path.splitext(w_path)[0] + ".docx", 16)  # 转化后路径下的文件
        doc.Close()
        word.Quit()
        w_path = '{}x'.format(tmp_path)
    else:
        w_path = tmp_path
    return w_path