# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 23:33:58 2017

@author: KAA
"""

from urllib.request import urlopen # Импортировали библиотеку для работы с адресами 
                                    # и запросами Internet.
url = "http://export.finam.ru/MTLRP_170101_171231.txt?market=1&em=80745&code=MTLRP&apply=0&df=1&mf=0&yf=2017&from=01.01.2017&dt=31&mt=11&yt=2017&to=31.12.2017&p=7&f=MTLRP_170101_171231&e=.txt&cn=MTLRP&dtf=1&tmf=1&MSOR=1&mstime=on&mstimever=1&sep=3&sep2=1&datf=5&at=1"
f = urlopen(url)   # Открыли соединение.
data1 = f.read()   # Прочитали данные.
print(data1)
f.close() 