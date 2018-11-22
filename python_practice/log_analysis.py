# !/usr/bin/python3
# -*- coding: UTF-8 -*-
import re


def get_log():
    action = []
    action_time = []
    log_file = 'D:\python\PYTHON_PRACTICE\case_log.txt'
    with open(log_file, 'r', encoding='utf8') as f:
        for line in f.readlines(100000):
            info = re.match(r'^[0-9\:\s\/\,]{21}ACTION\s\w{1,30}\s[finished][\w\:\s=]{1,50}\=([0-9\.]{1,10})sec', line)
            if info:
                action.append(info.group(1))
                action_time.append(info.group(2))
        return action, action_time

def cal_avg(action, action_time):
    




if __name__ == 'main':
    get_log()

