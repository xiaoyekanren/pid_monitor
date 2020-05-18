import csv
import pandas as pd
import matplotlib.pyplot as plt

time = []
cpu = []
mem = []
with open('pid.csv')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        if len(row): # 判断是不是空行，csv中隔一行记录运行的信息
            time.append(row[3])
            cpu.append(float(row[2]))
            mem.append(float(row[1]))
        else:
            continue

print(time)
print(cpu)
print(mem)

s_cpu = pd.Series(cpu)
s_mem = pd.Series(mem)
cpu_mean = s_cpu.mean()
mem_mean = s_mem.mean()
print('cpu利用率平均值是：%f' % cpu_mean)
print('内存利用率平均值是：%f' % mem_mean)

plt.plot(time, cpu, c='r')
plt.plot(time, mem, c='b')
plt.show()