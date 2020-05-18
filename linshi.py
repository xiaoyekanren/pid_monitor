# coding=utf-8
import time
import csv
import psutil

aaa = psutil.pids()
for a in aaa:
    if psutil.Process(a).name() == 'wallpaper32.exe':
        print(a)
    # print(psutil.Process(a).name())
