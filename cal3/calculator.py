#!/usr/bin/env python3
import sys
import csv


class Args:
    def __init__(self):
        l = sys.argv[1:]
        self.c = l[l.index('-c')+1]
        self.d = l[l.index('-d')+1]
        self.o = l[l.index('-o')+1]

class Userdata(object):
   
    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        userdata = []
        with open(file_d) as file:
            for line in file:
                temp = line.strip().split(',')
                id = int(temp[0])
                gz = int(temp[1])
                userdata.append((id,gz))
        self.usr = userdata


class Incometax(object):

    def calc_for_all_userdata(self):
     #   print(usr)
        str_income = ''
        suilv = c['Yanglao']+c['Yiliao'] +c['Shiye']+c['Gongshang']+c['Shengyu']+c['Gongjijin']
   #     print(suilv)
        for gz in usr:
            if gz[1] <= c['Jishul']:
                shebao1 = c['Jishul'] * suilv
                val = gz[1] - shebao1
                tax1 = self.calcu(val)   
                income1 = gz[1] - shebao1 -tax1
                shebao  = format(shebao1,".2f") 
                tax  = format(tax1,".2f") 
                income  = format(income1,".2f") 
                str_income = str_income +  str(gz[0])+','+str(gz[1])+','+str(shebao)+','+str(tax)+','+str(income)+'\n'
            elif gz[1] >= c['Jishuh']:
                shebao1 = c['Jishuh'] * suilv
                val = gz[1] - shebao1
                tax1 = self.calcu(val)   
                income1 = gz[1] - shebao1 -tax1
                shebao  = format(shebao1,".2f") 
                tax  = format(tax1,".2f") 
                income  = format(income1,".2f") 
                str_income = str_income +  str(gz[0])+','+str(gz[1])+','+str(shebao)+','+str(tax)+','+str(income)+'\n'
            elif gz[1] <= c['Jishuh'] and gz[1] >= c['Jishul']:
                shebao1 = gz[1] * suilv
                val = gz[1] - shebao1
                tax1 = self.calcu(val)   
                income1 = gz[1] - shebao1 -tax1
                shebao  = format(shebao1,".2f") 
                tax  = format(tax1,".2f") 
                income  = format(income1,".2f") 
                str_income = str_income +  str(gz[0])+','+str(gz[1])+','+str(shebao)+','+str(tax)+','+str(income)+'\n'
            else:
               raise ValueError
        print(str_income)

    def calcu(self,val):
        num = val - 3500 
        if num <= 1500 and num >= 0:
            return   num*0.03
        elif num >1500 and num<=4500:
            return val*0.835 -  num*0.10 + 105
        elif num > 4500 and num <= 9000:
            return  num*0.20 + 555
        elif num > 9000 and num <= 35000:
            return  num*0.25 + 1005
        elif num > 35000 and num <= 55000:
            return  num*0.30 + 2755
        elif num > 55000 and num <= 80000:
            return  num*0.35 + 5505
        elif num > 80000:
            return  num*0.45 + 13505
        elif num >= -3500 and num < 0:
            return 0
        else:
            print("Parameter Error")
            return
      #  val2  = format(val,".2f") 
      #  print("{}:{:.2f}".format(key,val))
      #  print(key1,val1)


class Config(object):
   

    def __init__(self):    
        self.config = self._read_config()

    def _read_config(self):
        config = {}
        with open(file_c) as file:
            for line in file:
                str = line.replace(' ','').strip().split('=')
#                print(str)
                config[str[0]] = float(str[1])
        self.cfg = config

args = Args()
file_c = args.c
file_d = args.d
# file_con = '/home/shiyanlou/shiyanlou01/cal3/test.cfg'
cfg = Config()
c=cfg.cfg
usr_1 = Userdata()
usr = usr_1.usr
print(c)
i = Incometax()
i.calc_for_all_userdata()

"""
if __name__  == '__main__':
    try:

        indatadict = {}
        for arg in sys.argv[1:]:
            str_key = arg.split(':')
            a = int(str_key[0])
            b = int(str_key[1])
    #        print(a,b)
            indatadict[a] = b
     #       print(indatadict)
      #  for key,val in indatadict.items():
       #     print(key,val)
         calcu(indatadict)
        file_con = '/home/shiyanlou/shiyanlou01/cal3/test.cfg'
        cfg = Config(file_con)
  #      cfg._read_config()        
    except ValueError:
        print("Parameter Error")
"""
