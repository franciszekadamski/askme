#!/usr/bin/python3

import pandas as pd 
import numpy as np 
import os 

lines_ = []

with open('raw_data.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    row = line[:-1].split('\t')
    if row[5] != '' and row[4] != '':
        lines_.append([row[1], row[4], row[5]])
    

df = pd.DataFrame(lines_, columns=['ch', 'py', 'en'])
df.to_csv('ch_py_en.csv')
