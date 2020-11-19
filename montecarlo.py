import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importo datos
file_name = "Contratos"
# main_path = ("F:\\Inversiones\\VP_Inversiones\\SIM\\Research\\2. Top down\\Commodities\\Backtesting\\")
file_path = (file_name + ".xlsx")
sheet_name = "Datos Diarios BBG"

df = pd.read_excel(file_path, sheet_name = sheet_name, parse_dates = True, index_col = 0)

#Selecciono los nodos curvas de los commodities
selected_tickers = ['CO1 Comdty', 'CO2 Comdty', 'CO3 Comdty', 'CO4 Comdty', 'CO5 Comdty', 'HG1 COMB Comdty', 'HG2 COMB Comdty', 'HG3 COMB Comdty', 'HG4 COMB Comdty',
                   'HG5 COMB Comdty', 'GC1 COMB Comdty', 'GC2 COMB Comdty', 'GC3 COMB Comdty', 'GC4 COMB Comdty', 'GC5 COMB Comdty']
df = df.loc[:, selected_tickers].dropna()

retorno_oil=df_oil.pct_change()
retorno_copper=df_copper.pct_change()
retorno_gold=df_gold.pct_change()
col_oil=len(retorno_oil.columns)-1
col_copper=len(retorno_copper.columns)-1
col_gold=len(retorno_gold.columns)-1

n_iter = 10000

best_alpha = 0
best_corr = 1
corr_obj = 0.2
contratos = []

for i in range(n_iter):

    # escogiendo contratos
    oil_ct1 = int(np.random.randn()*col_oil)
    oil_ct2 = int(np.random.randn() * col_oil)
    while oil_ct2 >= oil_ct1:
        oil_ct2 = int(np.random.randn() * col_oil)

    copper_ct1 = int(np.random.randn() * col_copper)
    copper_ct2 = int(np.random.randn() * col_copper)
    while copper_ct2 >= copper_ct1:
        copper_ct2 = int(np.random.randn() * col_copper)

    gold_ct1 = int(np.random.randn() * col_gold)
    gold_ct2 = int(np.random.randn() * col_gold)
    while gold_ct2 >= gold_ct1:
        gold_ct2 = int(np.random.randn() * col_gold)

    # creando retornos
    oil_ret = df_oil[df_oil.columns[oil_ct1]]/df_oil[df_oil.columns[oil_ct1]]-1
    copper_ret = df_oil[df_oil.columns[copper_ct1]]/df_oil[df_oil.columns[copper_ct1]]-1
    gold_ret = df_oil[df_oil.columns[gold_ct1]]/df_oil[df_oil.columns[gold_ct2]]-1

    print("Contratos Oil " + str(oil_ct1) + "/" + str(oil_ct2))
    print("Contratos Copper " + str(copper_ct1) + "/" + str(copper_ct2))
    print("Contratos Gold " + str(gold_ct1) + "/" + str(gold_ct2))

    # Aquí optimización y modelo ML
    # Aquí optimización y modelo ML
    # Aquí optimización y modelo ML
    # Aquí optimización y modelo ML
    # Aquí optimización y modelo ML

    alpha = "resultado del modelo"
    corr = "correlacion de alpha con mkt"
    if alpha >= best_alpha and corr < corr_obj:
        best_alpha = alpha
        best_corr = corr
        contratos = [[str(oil_ct1) + "/" + str(oil_ct2)],
                     [str(copper_ct1) + "/" + str(copper_ct2)],
                     [str(gold_ct1) + "/" + str(gold_ct2)]]

print("El mejor modelo es: " + str(contratos))
print("Alpha: " + str(best_alpha))
print("R2: " + str(best_corr))
