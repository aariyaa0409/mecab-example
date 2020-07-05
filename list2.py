#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd

#右端単語と品詞情報のリスト
def k2(filename1, filename2):
    with open(filename1, encoding='utf_8_sig') as h:
        readerh = csv.reader(h)
        lh = [row for row in readerh]
        
    hukugougo2 = []
    for i in range(len(lh)):
        hukugougo2.append(lh[i][16:21])
        
    with open(filename2, encoding='utf_8_sig') as f:
        reader = csv.reader(f)
        l2 = [row for row in reader]
        
    df_h2 = pd.DataFrame(hukugougo2)
    df_l2 = pd.DataFrame(l2)
    k2 = pd.merge(df_h2, df_l2, on=[1,2,3,4], how='left')
    return k2

