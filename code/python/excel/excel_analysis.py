#!/usr/bin/env python
from __future__ import division

import sys
import os
import xlrd

DEBUG = True
NORMAL = 'normal'
SUSPECT = 'suspect'
ABNORMAL = 'abnormal'

def load_data_from_excel(excel):
    book = xlrd.open_workbook(excel)
    sheet = book.sheet_by_index(0)

    # data[guid, access_time, request_refer]
    data = []
    for i in range(1, sheet.nrows):
        data.append([sheet.cell_value(i, col) for col in [0, 2, 7]])

    for i in data:
        frac = i[1] - int(i[1])
        seconds = int(round(frac * 86400))
        minutes = seconds / 60
        i[1] = minutes

    if DEBUG:
        for i in range(0, 10):
            print(data[i])
            # print(data[i][0], xlrd.xldate_as_tuple(data[i][1], 0), data[i][2])
            # import pdb; pdb.set_trace()

    return data

def load_data_from_another_resource(file):
    return 0

def judge_record_type(records, index):
    '''
    To a single guid.
    1. normal: in 5 minutes refer NULL.
    2. suspect: in 30 minutes refer NULL.
    3. abnormal: no refer NULL in 30 minutes.
    '''
    record_type = None

    current_index = index
    if records[index][2] is '':
        record_type = NORMAL
    else:
        while index > 0 and records[current_index][0] == records[index-1][0]:
            index -= 1
            diff_time = records[current_index][1] - records[index][1]
            if records[index][2] == '':
                if diff_time <= 5:
                    record_type = NORMAL
                    break
                elif 5 < diff_time <= 30:
                    record_type = SUSPECT
                    break

    if record_type is None:
        record_type = ABNORMAL

    return record_type

def main():
    data = load_data_from_excel('baidu.xlsx')
    stats = {NORMAL: 0, SUSPECT: 0, ABNORMAL: 0}
    for i in range(len(data)):
        record_type = judge_record_type(data, i)
        stats[record_type] += 1
        if DEBUG:
            if i > 0 and data[i][0] != data[i-1][0]:
                print()
            print(i, data[i], record_type)
    total = sum(stats.values())
    print()
    for key in stats:
        print(key, stats[key], round(100 * stats[key]/total, 2))
    return 0

if __name__ == '__main__':
    main()
