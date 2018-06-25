
# coding: utf-8

# In[13]:


import tushare as ts
import os
print(ts.__version__)
info = ts.get_stock_basics()
#info.to_csv('info_stk.csv')
#df = ts.get_k_data('002743', ktype = '30', autype = 'qfq', start = '2018-01-01', end = '2018-06-20')
#df1 = ts.get_k_data('002743', ktype = 'D', autype = 'qfq', start = '2018-01-01', end = '2018-06-20')


# In[14]:



if os.path.exists('002743_30.csv'):
        df.to_csv('002743_30.csv', mode='a', header=None)
else:
        df.to_csv('002743_30.csv')
if os.path.exists('002743_d.csv'):
        df1.to_csv('002743_d.csv', mode='a', header=None)
else:
        df1.to_csv('002743_d.csv')


# In[ ]:


#info = ts.get_stock_basics()


