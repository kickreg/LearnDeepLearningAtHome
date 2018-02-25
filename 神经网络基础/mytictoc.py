
# coding: utf-8

# In[3]:

import time

def tic():
    globals()['tt'] = time.time()
    
def toc():
    print ('\nElapsed time:%.8f ms\n' % (1000*(time.time()-globals()['tt'])))
    


# In[ ]:



