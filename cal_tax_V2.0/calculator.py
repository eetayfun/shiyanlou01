#!/usr/bin/env python3
import sys
import csv


class Args:
    def __init__(self):
        if len(sys.argv) == 7:
            l = sys.argv[1:]
            self.c = l[l.index('-c')+1]
            self.d = l[l.index('-d')+1]
            self.o = l[l.index('-o')+1]
        else:
            raise ValueError

args = Args()

class Userdata(object):
    def __init__(self):
        with open(args.d) as f:
            data = list(csv.reader(f))
        self.userdata = data

userdata = Userdata().userdata

class Config:
    def __init__(self):    
        self.config = self._read_config()
    def _read_config(self):
        config = {'s': 0}
        with open(args.c) as file:
            for line in file.readlines():
                l = line.split('=')
                a, b = l[0].strip(), float(l[1])
                if b > 1:
                    config[a] = b
                else:
                    config['s'] += b
        return config

config = Config().config

def cal(a, b):
    try:
        salary = int(b)
    except ValueError:
        print('Parameter Error')
        exit()
    shebao = salary * config['s']
    if salary < config['JiShuL']:
        shebao = config['JiShuL'] * config['s']
    if salary > config['JiShuH']:
        shebao = config['JiShuH'] * config['s']
    cal_tax = salary - shebao - 3500
    if cal_tax <= 0:
        shuie = 0
    elif cal_tax <= 1500:
        shuie = cal_tax * 0.03
    elif cal_tax <= 4500:
        shuie = cal_tax *0.1 -105
    elif cal_tax <= 9000: 
        shuie = cal_tax * 0.2 -555
    elif cal_tax <= 35000:
        shuie = cal_tax * 0.25 - 1005
    elif cal_tax <= 55000:
        shuie = cal_tax * 0.30 - 2755
    elif cal_tax <= 80000:
        shuie = cal_tax * 0.35 - 5505
    else:
        shuie = cal_tax * 0.45 - 13505
    return [a, salary, format(shebao, '.2f'), format(shuie, '.2f'),
        format(salary-shebao-shuie, '.2f')]

with open(args.o, 'w') as f:
    for a, b in userdata:
        csv.writer(f).writerow(cal(a, b))
