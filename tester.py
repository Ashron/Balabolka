# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:04:30 2017

@author: KAA
"""

from getsharehistory import GetShareHistory

History = GetShareHistory()

url = History.get_url('MTLRP','01.01.2016','31.12.2016',7)
print(url[0])

