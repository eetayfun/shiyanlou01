#!/usr/bin/env python3
import sys


def calcu(num2):
    num = num2 - 3500
#    print(num)
    if num <= 1500 and num >= 0:
        tax =num*0.03
    elif num >1500 and num<=4500:
        tax = num*0.10 - 105
    elif num > 4500 and num <= 9000:
        tax = num*0.20 - 555
    elif num > 9000 and num <= 35000:
        tax = num*0.25 - 1005
    elif num > 35000 and num <= 55000:
        tax = num*0.30 - 2755
    elif num > 55000 and num <= 80000:
        tax = num*0.35 - 5505
    elif num > 80000:
        tax = num*0.45 - 13505
    else:
        print("Parameter Error")
        return
    tax1 = format(tax,".2f")
    print(tax1)

if __name__ == '__main__':
    try:
        num1 = int(sys.argv[1])
    #    print(num1)
        calcu(num1)
   #     print(tax)
    except ValueError:
        print("Parameter Error")
