# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:33:40 2017

@author: KAA
"""

share = "MTLRP"
info_share ='moex-classica/'+share.lower() 
        
from urllib.request import urlopen
finam_symbols = urlopen('http://www.finam.ru/cache/icharts/icharts.js').readlines()

#print(finam_symbols[8])

moexakcii = finam_symbols[8].decode("utf-8")
print(moexakcii)

#print(len('": "moex-akcii/'))
#print(len('","'))
#print(len('": "moex-akcii/'))

s = 0
start = '": "moex-akcii/'
s_len = len(start)
m_1 = 0
m_2 = 0
midle = '","'
m_len = len(midle)
e = 0
end = '": "'
e_len = len(end)

n = 0
print(moexakcii.count(start))
while n < moexakcii.count(start) :
    s = moexakcii.find(start,s,len(moexakcii))+s_len
    m_1 = moexakcii.find(midle,s,len(moexakcii))
    m_2 = m_1 + m_len
    e = moexakcii.find(end,m_2,len(moexakcii))
    print(moexakcii[s:m_1],' : ',moexakcii[m_2:e])
    n = n+1
        

    