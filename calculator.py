#!/usr/bin/env python3
import sys


def calcu(dict):
    tax = {}
    for key,val in dict.items():
        num = val - val*0.165 - 3500 
        if num <= 1500 and num >= 0:
            tax[key] = val*0.835 -  num*0.03
        elif num >1500 and num<=4500:
            tax[key] = val*0.835 -  num*0.10 + 105
        elif num > 4500 and num <= 9000:
            tax[key] = val*0.835 - num*0.20 + 555
        elif num > 9000 and num <= 35000:
            tax[key] = val*0.835 - num*0.25 + 1005
        elif num > 35000 and num <= 55000:
            tax[key] = val*0.835 - num*0.30 + 2755
        elif num > 55000 and num <= 80000:
            tax[key] = val*0.835 - num*0.35 + 5505
        elif num > 80000:
            tax[key] = val*0.835 - num*0.45 + 13505
        elif num >= -3500 and num < 0:
            tax[key] = val - val*0.165
        else:
            print("Parameter Error")
            return
    for key,val in tax.items():
      #  val2  = format(val,".2f") 
        print("{}:{:.2f}".format(key,val))
      #  print(key1,val1)

if __name__ == '__main__':
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
    except ValueError:
        print("Parameter Error")

