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

periods=53
gap=0.3
for i in col_oil:
    temp_oil=pd.DataFrame()
    l=i+1
    l2=i+2
    l3=i+3
    ret1=df_oil[df_oil.columns[l]]/df_oil[df_oil.columns[i]]-1
    ret12=df_oil[df_oil.columns[l3]]/df_oil[df_oil.columns[l2]]-1
    temp_oil["OIL"]=ret1.rolling(window = periods).apply(lambda x: np.prod(1 + x) - 1) - ret12.rolling(window = periods).apply(lambda x: np.prod(1 + x) - 1)

#     ret1=ret1.dropna()
#     ret12=ret12.dropna()
    temp_oil=temp_oil.dropna()
#     ret1=pd.DataFrame(ret1)
    for m in range(col_copper):
        temp_copper=pd.DataFrame()
        n=m+1
        n2=m+2
        n3=m+3
        ret2=df_copper[df_copper.columns[n]]/df_copper[df_copper.columns[m]]-1
        ret22=df_copper[df_copper.columns[n3]]/df_copper[df_copper.columns[n2]]-1
        temp_copper["COPPER"]=ret2.rolling(window = periods).apply(lambda x: np.prod(1 + x) - 1) - ret22.rolling(window = periods).apply(lambda x: np.prod(1 + x) - 1)

#         ret2=ret2.dropna()
#         ret22=ret22.dropna()
#         ret2=pd.DataFrame(ret2)
        temp_copper=temp_copper.dropna()
        for p in range(col_gold):
            temp_gold=pd.DataFrame()
            o=p+1
            o2=p+2
            o3=p+3
            ret3=df_gold[df_gold.columns[o]]/df_gold[df_gold.columns[p]]-1
            ret32=df_gold[df_gold.columns[o3]]/df_gold[df_gold.columns[o2]]-1
            temp_gold["GOLD"]=ret3.rolling(window = periods).apply(lambda x: np.prod(1 + x) - 1) - ret32.rolling(window = periods).apply(lambda x: np.prod(1 + x) - 1)

#             ret3=ret3.dropna()
#             ret32=ret32.dropna()
            temp_gold=temp_gold.dropna()
            df_name= retorno_oil.columns[i]+ " " + retorno_copper.columns[m]+ " " +retorno_gold.columns[p] + ".csv"
#             df_name= i + m + p
#             ret3=pd.DataFrame(ret3)
            basis=pd.concat([temp_oil,temp_copper,temp_gold], axis=1, join_axes=[temp_oil.index])
            basis=basis.dropna()
            basis.to_csv('F:\\Inversiones\\VP_Inversiones\\SIM\\Research\\2. Top down\\Commodities\\Backtesting\\Optimizacion\\'+ df_name)
           
     
