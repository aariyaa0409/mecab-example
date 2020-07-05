#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import pandas as pd

#左端単語と品詞情報のリストを取得
def k1(filename1, filename2):

    with open(filename1, encoding='utf_8_sig') as h:
        readerh = csv.reader(h)
        lh = [row for row in readerh]
        
    hukugougo = []
    for i in range(len(lh)):
        hukugougo.append(lh[i][11:16])
    
    with open(filename2, encoding='utf_8_sig') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        
    df_h = pd.DataFrame(hukugougo)
    df_l = pd.DataFrame(l)
    k1 = pd.merge(df_h, df_l, on=[1,2,3,4], how='left')
    return k1


# In[ ]:




