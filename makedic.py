#!/usr/bin/env python
# coding: utf-8

# In[71]:


import csv
import pandas as pd
from list1 import k1
from list2 import k2
from matrix import matrix

df = pd.read_csv("test.csv",header=1,encoding='utf_8_sig')
df.to_csv('raw.csv', encoding='utf_8_sig', index=False, header=False)

x1 = k1('raw.csv', 'noun_id.csv')
x2 = k2('raw.csv', 'noun_id.csv')

#上で取得した左右接続IDをユーザー辞書に記入
df.insert(1,'左接続1',x1['0_y'], allow_duplicates=True)
df.insert(2,'右接続1',x2['0_y'], allow_duplicates=True)
del df['左接続']
del df['右接続']

#左接続IDと右接続IDのリストを取得…(1)
tolist2 = df.values.tolist()
left = []
right = []
for i in tolist2:
    left.append(i[1])
    right.append(i[2])
    df_l = pd.DataFrame({'left': left, 'right': right})

#左右接続IDとコスト値のマトリクスを取得…(2)
df_m = matrix('matrix.csv')

#(1)(2)を並べて配置→複合語のコスト値を取得
id_cost = pd.merge(df_l, df_m, on=['left','right'], how='left')
df.insert(3,'コスト1',id_cost['cost'], allow_duplicates=True)
del df['コスト']

#活用型、活用形を追加
df.insert(8, '活用型', '*')
df.insert(8, '活用形', '*')

print(df)
df.to_csv('dictionary.csv', encoding='utf_8_sig', index=False, header=False)

