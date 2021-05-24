#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib_venn import venn2,venn2_circles

import matplotlib as mpl
mpl.rcParams['font.serif'] = 'Arial'
mpl.rcParams['pdf.fonttype'] = 42


# # compare lists

# In[2]:


list_a = ['a','b']
list_b = ['b','c','d']


# In[3]:


f, ax = plt.subplots(figsize=(5, 5))
g = venn2([set(list_a), set(list_b)],
          ax=ax,
          set_colors=['white', 'white'],
          set_labels=['a', 'b'])
v = venn2_circles(
    [set(list_a), set(list_b)],
    ax=ax,
)
v[0].set_edgecolor('r')
v[1].set_edgecolor('b')

# plt.savefig('./venn.pdf') # VennDiagram does not have the method savefig


# # assign subsets manully

# In[ ]:




