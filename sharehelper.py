# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:03:20 2017

@author: KAA
"""
class ShareHelper:
    
    def get_code(self, symbol):
        share = symbol.lower()
        info_share ='moex-classica/'+share 
        
        from urllib.request import urlopen
        finam_symbols = urlopen('http://www.finam.ru/cache/icharts/icharts.js').readlines()
        
        str_symbols = finam_symbols[8].decode("utf-8") 
        start = str_symbols.find(info_share)+len(info_share)+3
        end = str_symbols.find('": "', start)
         
#        code_share = str(str_symbols[start:end])
        code_share = str_symbols[start:end]
        return [code_share]
