# coding=utf8
import time
import csv
import psutil
import argparse

p = argparse.ArgumentParser(description='monitor by pid')
p.add_argument('-P', '--pid', dest='pid', type=int, help='input a pid')
pid = p.parse_args().pid
p.add_argument('-i', '--interval', dest='interval', type=int)
interval = p.parse_args().interval

if not interval:
    interval = 1
if not pid:
    print('please input a pid to monitor')
    exit()

proc = psutil.Process(int(pid))
f = open('pid.csv', 'w')
f.truncate()
f_csv = csv.writer(f)

while True:
    row = []
    row = [pid, time.strftime("%Y-%m-%d %H:%M:%S"), proc.memory_percent(), proc.cpu_percent(), psutil.net_io_counters().bytes_recv, psutil.net_io_counters().bytes_sent, psutil.net_io_counters().packets_recv, psutil.net_io_counters().packets_sent]
    f_csv.writerow(row)
    if not psutil.pid_exists(pid):
        f.close()
        exit(0)
    time.sleep(0.01)
f.close()




