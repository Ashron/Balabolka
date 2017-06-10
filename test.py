# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 13:33:40 2017

@author: KAA
"""

#print('test')
#
#from sharehelper import ShareHelper
#
#sh = ShareHelper()
#print(sh.get_code('MTLRP'))


share = "MTLRP"
info_share ='moex-classica/'+share.lower() 
        
from urllib.request import urlopen
finam_symbols = urlopen('http://www.finam.ru/cache/icharts/icharts.js').readlines()

#print(finam_symbols)
        
str_symbols = finam_symbols[8].decode("utf-8") 
start = str_symbols.find(info_share)+len(info_share)+3
end = str_symbols.find('": "', start)
         
#        code_share = str(str_symbols[start:end])
code_share = str_symbols[start:end]
#print(code_share)



#"moex-akcii/
#","
#":

#print(finam_symbols)

s = finam_symbols[8].decode("utf-8") 

print(s.count('"moex-akcii/?","'))

