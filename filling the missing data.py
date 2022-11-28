#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
#from pandasql import sqldf

df=pd.read_csv('https://raw.githubusercontent.com/tarikkranda/pi_datasets/main/country_vaccination_stats.csv')


#4question

#df['daily_vaccinations'] = df['daily_vaccinations'].replace(np.nan, 0)

dff=df['daily_vaccinations'].fillna(df['daily_vaccinations'].min())
#df=df.query('daily_vaccinations != 0')
print(dff)


# In[ ]:





# In[ ]:




