
# coding: utf-8

# In[1]:


import puzzlerepresentation as P


# In[2]:


import numpy as np


# In[3]:


def buildRandomChromosome(hole=None):
    C = np.random.randint(0, 7, size=(10,3))
    C[:,-1] = np.random.randint(0,4, size=10)
    if hole:
        C[-1] = [hole[0], hole[1], 0]
    return C


# In[4]:


pieces = P.pieces + [P.Piece('black',[[0,0]])]


# In[18]:


def score(C):
    A = np.zeros([7,7],dtype=int)
    pieces = P.pieces + [P.Piece('black',[[0,0]])]
    for i in range(10):
        for unit in pieces[i].rotate(C[i,2]).unit_list:
            x = C[i][0] + unit[0]
            y = C[i][1] + unit[1]
            if (min(x,y) < 0) or (max(x,y) > 6):
                return np.infty
            A[x][y] += 1
    print(np.abs(A-1).sum())
    print(A)
    return np.abs(A-1).sum()


# In[19]:


C_list = [buildRandomChromosome() for _ in range(1000)]


# In[26]:


for p in pieces:
    print(p.unit_list)


# In[25]:


for C in C_list:
    score(C)

