# coding=utf8
import time
import csv
import psutil
import argparse

p = argparse.ArgumentParser(description='monitor by pid')
p.add_argument('-P', '--pid', dest='pid', type=int, help='input a pid')
pid = p.parse_args().pid

proc = psutil.Process(int(pid))
f = open('pid.csv', 'w')
f.truncate()
f_csv = csv.writer(f)
flag = 1

while flag < 10:
    row = []
    row = [pid, '%.2f' %(proc.memory_percent()), '%.2f' % (proc.cpu_percent()), time.strftime("%H:%M:%S", time.localtime()), proc.name(), proc.exe()]
    f_csv.writerow(row)
    flag += 1
    time.sleep(1)
