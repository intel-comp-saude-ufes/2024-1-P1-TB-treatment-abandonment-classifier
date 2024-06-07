import numpy as np
import pandas as pd

df = pd.read_csv('data/tuberculose_imputed.csv')
# Otimização de memória
for column in df.columns:
    df[column] = df[column].astype(np.int8)
df.info()
# Codificação de variáveis categóricas
# reg_not (0 = Norte, 1 = Nordeste, 2 = Sul, 3 = Sudeste, 4 = Centro-Oeste)
# cs_sexo (0 = Feminino, 1 = Masculino)
# cs_raca (0 = Branco, 1 = Preto, Pardo, Amarelo, Indígena)
# cs_escol_n (0 = 5- anos, 1 = 5-8 anos, 2 = 9-11 anos, 3 = 12+ anos)
# tratamento (0 = Caso novo, 1 = Retratamento (recidivo ou reingresso após abandono))
# raiox_tora (0 = Normal, 1 = Suspeito, 2 = Não realizado)
# agravaids (0 = Não, 1 = Sim)
# agravalcoo (0 = Não, 1 = Sim)
# agravdiabe (0 = Não, 1 = Sim)
# agravdoenc (0 = Não, 1 = Sim)
# hiv (0 = Negativo, 1 = Positivo, 2 = Não realizado)
# tratsup_at (0 = Não, 1 = Sim)
# benef_gov (0 = Não, 1 = Sim)
# agravdroga (0 = Não, 1 = Sim)
# agravtabac (0 = Não, 1 = Sim)
# idade
# abandono (0 = Não, 1 = Sim)