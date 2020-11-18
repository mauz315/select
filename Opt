import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


#Importo datos
file_name = "Contratos"
main_path = ("F:\\Inversiones\\VP_Inversiones\\SIM\\Research\\2. Top down\\Commodities\\Backtesting\\")
file_path = (file_name + ".xlsx")
sheet_name_oil = "Petr"
sheet_name_copper = "Cobre"
sheet_name_gold = "Oro"


df_oil = pd.read_excel(main_path + "\\" + file_path, sheet_name = sheet_name_oil, parse_dates = True, index_col = 0, header =1)
df_copper = pd.read_excel(main_path + "\\" + file_path, sheet_name = sheet_name_copper, parse_dates = True, index_col = 0, header =1)
df_gold = pd.read_excel(main_path + "\\" + file_path, sheet_name = sheet_name_gold, parse_dates = True, index_col = 0, header =1)

retorno_oil=df_oil.pct_change()
retorno_copper=df_copper.pct_change()
retorno_gold=df_gold.pct_change()

# i=random.choice(retorno_oil.columns)
# i=retorno_oil.columns.get_loc(i)
# l=i+1

# m=random.choice(retorno_copper.columns)
# m=retorno_copper.columns.get_loc(m)
# n=m+1

# p=random.choice(retorno_gold.columns)
# p=retorno_gold.columns.get_loc(p)
# o=p+1

col_oil=len(retorno_oil.columns)-1
col_copper=len(retorno_copper.columns)-1
col_gold=len(retorno_gold.columns)-1

for i in range(col_oil):
    temp=pd.DataFrame()
    l=i+1
    ret1=df_oil[df_oil.columns[l]]/df_oil[df_oil.columns[i]]-1
    ret1=ret1.dropna()
    ret1=pd.DataFrame(ret1)
    for m in range(col_copper):
        n=m+1
        ret2=df_copper[df_copper.columns[n]]/df_copper[df_copper.columns[m]]-1
        ret2=ret2.dropna()
        ret2=pd.DataFrame(ret2)
        for p in range(col_gold):
            o=p+1
            retorno_gold.columns[p]
            ret3=df_gold[df_gold.columns[o]]/df_gold[df_gold.columns[p]]-1
            ret3=ret3.dropna()
            ret3=pd.DataFrame(ret3)
            ret=ret1.append([ret2, ret3])
