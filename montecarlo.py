import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Importo datos
file_name = "Contratos"
# main_path = "F:\\Inversiones\\VP_Inversiones\\SIM\\Research\\2. Top down\\Commodities\\Backtesting\\"
main_path = "C:\\Users\\P900017\\Documents\\Python Scripts\\select"
file_path = (file_name + ".xlsx")
sheet_name_oil = "Petr"
sheet_name_copper = "Cobre"
sheet_name_gold = "Oro"
sheet_name_todo = "TODO"
df_oil = pd.read_excel(main_path + "\\" + file_path, sheet_name=sheet_name_oil, parse_dates=True, index_col=0, header=1)
df_copper = pd.read_excel(main_path + "\\" + file_path, sheet_name=sheet_name_copper, parse_dates=True, index_col=0,
                          header=1)
df_gold = pd.read_excel(main_path + "\\" + file_path, sheet_name=sheet_name_gold, parse_dates=True, index_col=0,
                        header=1)
df = pd.read_excel(main_path + "\\" + file_path, sheet_name=sheet_name_todo, parse_dates=True, index_col=0)
df = df.dropna(how="all")
df = df.groupby(pd.Grouper(freq='W')).last()
df_oil = df_oil.groupby(pd.Grouper(freq='W')).last()
df_copper = df_copper.groupby(pd.Grouper(freq='W')).last()
df_gold = df_gold.groupby(pd.Grouper(freq='W')).last()

sequence = ['CO1 COMB Comdty', 'HG1 COMB Comdty', 'GC1 COMB Comdty']
prices = df.filter(sequence)

# Selecciono los nodos curvas de los commodities
# selected_tickers = ['CO1 Comdty', 'CO2 Comdty', 'CO3 Comdty', 'CO4 Comdty', 'CO5 Comdty', 'HG1 COMB Comdty', 'HG2 COMB Comdty', 'HG3 COMB Comdty', 'HG4 COMB Comdty',
#                    'HG5 COMB Comdty', 'GC1 COMB Comdty', 'GC2 COMB Comdty', 'GC3 COMB Comdty', 'GC4 COMB Comdty', 'GC5 COMB Comdty']
# df = df.loc[:, selected_tickers].dropna()

retorno_oil = df_oil.pct_change()
retorno_copper = df_copper.pct_change()
retorno_gold = df_gold.pct_change()
col_oil = len(retorno_oil.columns) - 1
col_copper = len(retorno_copper.columns) - 1
col_gold = len(retorno_gold.columns) - 1

n_iter = 5000

best_alpha = 0
best_corr = 1
corr_obj = 0.2
drawdown_obj = 0.20
contratos = []
periods = 53
gap = 0.03

alpha_index = pd.DataFrame()
alpha_max = pd.DataFrame()
# prices = df.filter(like = '1') #Filtra los commodities que se vencen mas temprano (1)
# next_contracts = df.loc[:, ~df.columns.isin(prices.columns)] #Filtra por los contratos que se vencen despes (2,3,4)

print("Iniciando " + str(n_iter) + " iteraciones...")
perc = np.percentile(range(n_iter), (range(10, 110, 10))).astype(int)

# for i in range(n_iter):
for itera in range(n_iter):

    if n_iter >= 10 and itera in perc:
        print("Iteración #" + str(itera))
    # escogiendo contratos
    oil_ct4 = random.randint(5, col_oil)  # mayor a 5
    oil_ct3 = random.randint(4, oil_ct4 - 1)
    oil_ct2 = random.randint(3, oil_ct3)
    oil_ct1 = random.randint(2, oil_ct2 - 1)  # mayor a 1

    copper_ct4 = random.randint(5, col_copper)  # mayor a 5
    copper_ct3 = random.randint(4, copper_ct4 - 1)
    copper_ct2 = random.randint(3, copper_ct3)
    copper_ct1 = random.randint(2, copper_ct2 - 1)  # mayor a 1

    gold_ct4 = random.randint(5, col_gold)  # mayor a 5
    gold_ct3 = random.randint(4, gold_ct4 - 1)
    gold_ct2 = random.randint(3, gold_ct3)
    gold_ct1 = random.randint(2, gold_ct2 - 1)  # mayor a 1

    # copper_ct1 = int(np.random.randn() * col_copper)
    # copper_ct2 = int(np.random.randn() * col_copper)
    # while copper_ct2 >= copper_ct1:
    #     copper_ct2 = int(np.random.randn() * col_copper)

    # creando retornos
    oil_ret1 = df_oil[df_oil.columns[oil_ct2 - 1]] / df_oil[df_oil.columns[oil_ct1 - 1]] - 1
    oil_ret1 = oil_ret1.dropna().sort_index()
    oil_ret2 = df_oil[df_oil.columns[oil_ct4 - 1]] / df_oil[df_oil.columns[oil_ct3 - 1]] - 1
    oil_ret2 = oil_ret2.dropna().sort_index()
    copper_ret1 = df_copper[df_copper.columns[copper_ct2 - 1]] / df_copper[df_copper.columns[copper_ct1 - 1]] - 1
    copper_ret1 = copper_ret1.dropna().sort_index()
    copper_ret2 = df_copper[df_copper.columns[copper_ct4 - 1]] / df_copper[df_copper.columns[copper_ct3 - 1]] - 1
    copper_ret2 = copper_ret2.dropna().sort_index()
    gold_ret1 = df_gold[df_gold.columns[gold_ct2 - 1]] / df_gold[df_gold.columns[gold_ct1 - 1]] - 1
    gold_ret1 = gold_ret1.dropna().sort_index()
    gold_ret2 = df_gold[df_gold.columns[gold_ct4 - 1]] / df_gold[df_gold.columns[gold_ct3 - 1]] - 1
    gold_ret2 = gold_ret2.dropna().sort_index()

    oil_contracts = "Oil " + str(oil_ct2) + "/" + str(oil_ct1) + " & " + str(oil_ct4) + "/" + str(oil_ct3)
    copper_contracts = "Copper " + str(copper_ct2) + "/" + str(copper_ct1) + " & " + str(copper_ct4) + "/" + str(
        copper_ct3)
    gold_contracts = "Gold " + str(gold_ct2) + "/" + str(gold_ct1) + " & " + str(gold_ct4) + "/" + str(gold_ct3)
    # print("Contratos " + oil_contracts)
    # print("Contratos " + copper_contracts)
    # print("Contratos " + gold_contracts)

    temp_oil = pd.DataFrame(index=df_oil.index)
    temp_oil[oil_contracts] = oil_ret1.rolling(window=periods).apply(lambda x: np.prod(1 + x) - 1) - oil_ret2.rolling(
        window=periods).apply(lambda x: np.prod(1 + x) - 1)
    temp_copper = pd.DataFrame(index=df_copper.index)
    temp_copper[copper_contracts] = copper_ret1.rolling(window=periods).apply(
        lambda x: np.prod(1 + x) - 1) - copper_ret2.rolling(
        window=periods).apply(lambda x: np.prod(1 + x) - 1)
    temp_gold = pd.DataFrame(index=df_gold.index)
    temp_gold[gold_contracts] = gold_ret1.rolling(window=periods).apply(
        lambda x: np.prod(1 + x) - 1) - gold_ret2.rolling(
        window=periods).apply(lambda x: np.prod(1 + x) - 1)

    basis = pd.concat([temp_oil, temp_copper, temp_gold], axis=1)
    basis = basis.dropna()
    # basis.to_csv('F:\\Inversiones\\VP_Inversiones\\SIM\\Research\\2. Top down\\Commodities\\Backtesting\\Optimizacion\\' + df_name)

    # Aquí modelo ML # POR REVISAR AUN
    ranking = basis.rank(axis=1)  # hago un ranking 1 siendo menor y 3 siendo el mayor, por fila
    weights = ranking
    # le pongo peso a cada uno, si es 1 es 1/3-gap, si es dos es 1/3 y si es 3, 1/3+gap
    weights[oil_contracts] = weights[oil_contracts].map({1: (1 / 3) + gap, 2: (1 / 3), 3: (1 / 3) - gap})
    weights[copper_contracts] = weights[copper_contracts].map({1: (1 / 3) + gap, 2: (1 / 3), 3: (1 / 3) - gap})
    weights[gold_contracts] = weights[gold_contracts].map({1: (1 / 3) + gap, 2: (1 / 3), 3: (1 / 3) - gap})

    weights = ranking.shift(1).dropna()  # elimino la primera fecha nose porque
    prices1 = prices.pct_change(1).loc[weights.index[0]:,
              :]  # saco los retornos de la primera parte de la curva, cambio el indice.
    returns = prices1.filter(weights.index, axis=0)  # saco precios con el indice de weights

    results = pd.DataFrame(returns.mean(axis=1))  # saco promedio por fila
    results.columns = ['Benchmark return']  # retorno del benchmark
    results['Portfolio return'] = (returns.values * weights.values).sum(axis=1)  # saco el retorno del portafolio
    results = results.dropna()

    i = 0
    portfolio_index = [100]
    benchmark_index = [100]
    alpha = []
    # creo los retornos en base 100 y calculo el alfa
    for date in results.index:
        portfolio_index.append(portfolio_index[i] * (1 + results.loc[date, "Portfolio return"]))
        benchmark_index.append(benchmark_index[i] * (1 + results.loc[date, "Benchmark return"]))
        alpha.append((portfolio_index[i] / portfolio_index[0] - 1) - (benchmark_index[i] / benchmark_index[0] - 1))
        i += 1
    # junto los resultados.

    results_final = pd.DataFrame({'Alpha': alpha, 'Benchmark': benchmark_index[1:], 'Portfolio': portfolio_index[1:]},
                                 index=results.index)

    # Aquí termina optimización y modelo ML

    alfa_diario = pd.DataFrame(results["Portfolio return"] - results["Benchmark return"])
    alfa_diario.rename(columns={alfa_diario.columns[0]: "Alpha Diario"}, inplace=True)
    retornos_ = pd.concat([results, alfa_diario], axis=1)
    coco = pd.DataFrame(results_final["Alpha"].tail(1))
    alpha = coco.iloc[0, 0]


    # alpha_index['Alpha'] = results_final['Alpha'] + 100

    if alpha >= best_alpha:
        corr = abs(retornos_["Benchmark return"].corr(retornos_["Alpha Diario"], method="pearson"))
        if corr < corr_obj:
            alpha_max['Alpha'] = results_final['Alpha'].rolling(window=53).max()
            max_drawdown = results_final['Alpha'] / alpha_max['Alpha'] - 1.0
            max_drawdown = abs(min(max_drawdown.dropna()))
            if max_drawdown < drawdown_obj:
                best_alpha = alpha
                best_corr = corr
                contratos = [oil_contracts, copper_contracts, gold_contracts]
                print("Nueva combinación de contratos escogidos")
                print(str(contratos))
                print("Alpha: " + str(best_alpha))
                print("Drawdown: " + str(best_alpha))

print("El mejor modelo es: " + str(contratos))
print("Alpha: " + str(best_alpha))
print("R2: " + str(best_corr))
