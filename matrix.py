#!/usr/bin/env python
# coding: utf-8

# In[3]:


#左右接続IDとコスト値のマトリクスを取得
#filename3='matrix.csv'
import csv
import pandas as pd

def matrix(filename3):

    with open(filename3, encoding='utf_8_sig') as m:
        reader = csv.reader(m)
        lm = [row for row in reader]
        df_lm = pd.DataFrame(lm, columns={"left":"0", "right":"1", "cost":"2"})
        return df_lm

