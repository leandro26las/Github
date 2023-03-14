# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 22:15:48 2023

@author: leand
"""

import pandas as pd
import matplotlib.pyplot as plt
import glob

#fig, axs = plt.subplots(2, 1, sharex=True)

path = 'C:\\Users\\Doutorado\\Medidas\\medidas_10marco2023\\medida*_EIT*.csv'

for file in glob.iglob(path, recursive=True):
    print(file)

# ##############################################################################

# # Acesso ao arquivo da absorcao
# arq1 = pd.read_csv("C:/Users/leand/OneDrive/Área de Trabalho/Leandro/Doutorado/Medidas/medidas_10marco2023/medida0_EIT_media4pts.csv", sep= ',', header=20)

# #Plot da Absorcao Saturada
# axs[0].plot( arq1["TIME"], arq1["CH1"], color = "green" )
# axs[0].set(title = "EIA em amostra de $^{85,87}$Rb", yticks = [] )

# axs[0].set_ylabel( "Amplitude (u.a.)" )

# #Plot do EIA

# axs[1].plot( arq1["TIME"], arq1["CH2"], color = "black" )
# axs[1].set_xlabel("Tempo (s)")
# axs[1].set( yticks=[] )
# axs[1].set_ylabel("Amplitude (u.a.)")

# # Ajuste dos espacos entre os plots

# fig.subplots_adjust(hspace=.01)


# #############################################################################


# # Acesso ao arquivo do laser de fentosegundo (fs)
# arq2 = pd.read_csv("C:/Users/leand/OneDrive/Área de Trabalho/Leandro/Doutorado/Medidas/medidas_10marco2023/medida10_frep.CSV", header=17)

# # Selecao dos dados do fs
# dados2 = pd.DataFrame( { "freq" : arq2['Trace1 X'], "Amp" : arq2['Trace1 Y'] } )

# # Localizacao do indice correspondente ao maximo do pico de fs
# frep, amp = dados2.iloc[ dados2["Amp"].idxmax(axis=0, skipna=True) ] 

# # Ponto do maximo do pico 
# point = (frep, amp)

# #Plot do pico da frequencia de repeticao do Fentosegundo
# plot_interno = fig.add_axes([.64, .49, .25, .15])
# plot_interno.plot( dados2["freq"], dados2["Amp"], color = "blue" )
# plot_interno.set( title = 'f$_{rep}$ = ' + str(frep) + ' (Hz)' , xticks = [], yticks = [] )

# #############################################################################

# plt.show()