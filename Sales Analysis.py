
# In[49]:


import pandas as pd
d = pd.read_csv("C:\\Users\APU\sales_data.csv")
print(d)


# In[35]:


import pandas as pd
d = pd.read_csv("C:\\Users\APU\sales_data.csv")
new_d = d.copy()
del new_d['Day']
min_df = new_d.copy()
min_df['Total Sales'] = [sum(min_df.iloc[i]) for i in range(7)]
min_df['Min Sales'] = min_df.idxmin(axis=1)
new_d['Max Sales'] = new_d.idxmax(axis=1)
new_d['Min Sales'] = min_df['Min Sales']
new_d['Total Sales'] = min_df['Total Sales']
print(new_d)


# In[43]:


import pandas as pd
d = pd.read_csv("C:\\Users\APU\sales_data.csv")
del d['Day']
min_sal = []
max_sal = []
avg_sal = []
tot_sal = []
for i in d.columns.values.tolist():
    min_sal.append(d[i].min())
    max_sal.append(d[i].max())
    avg_sal.append(d[i].mean())
    tot_sal.append(d[i].sum())
df = pd.DataFrame({'Min Sales': min_sal, 'Max Sales': max_sal, 'Avg. Sales': avg_sal, 'Total Sales': tot_sal}, index=d.columns.values.tolist())
print(df)


# In[46]:


print('Sales Report')
print(new_d)
print('Sales Statistics')
print(df)


# In[66]:


import pandas as pd
import matplotlib.pyplot as plt
d = pd.read_csv("C:\\Users\APU\sales_data.csv")
d.index = d['Day']
del d['Day']
for a in d.columns.values.tolist():
    plt.plot(d[a], label=a)
plt.xlabel('Days')
plt.ylabel('Sales')
plt.legend()
plt.show()

