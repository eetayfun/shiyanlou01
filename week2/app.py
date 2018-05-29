#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template
import os 
import json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
file_lists = []

@app.route('/')
def index():
    try:
        path = os.getcwd() + '/' + 'files'
        lists = os.listdir(path)
        for i in lists:
            file_lists.append(os.path.join(path,i))
        with open(file_lists[0],"r") as f:
            aa = json.load(f)
        with open(file_lists[1],"r") as f:
            bb = json.load(f)
        return  '{}    {} '.format(aa['title'],bb['title']) 
    except:
        return render_template('404.html')
