import pandas as pd
import os
# Prenoms par départements par année
path_to_file = 'dpt2017.txt'
data = pd.read_csv(path_to_file,encoding='utf-8',sep='\t')
print(data.shape)
print(data['nombre'].min())

plot_data = data[data['preusuel'] == 'CARINE']
print(plot_data['nombre'].sum())