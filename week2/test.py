#!/usr/bin/env python3
import os
import json

file_lists = []

if __name__ == "__main__":
    path = os.getcwd() + '/' + 'files'
    lists = os.listdir(path)
    for i in lists:
        file_lists.append(os.path.join(path,i))
    print(file_lists)
    for l in file_lists: 
        with open(l,"r") as f:
            bb = json.load(f)
            print(bb['title'])
