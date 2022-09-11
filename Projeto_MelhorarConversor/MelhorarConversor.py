import linecache
import re
from tkinter import N
import pandas as pd
import numpy as np

#Esse codigo conta a quantidade de linhas do arquivo
ContadorDeLinhas = 0 
for i in open("TLD_Resultado_TL.asc","r") .read().split("\n"): 
    if i: 
        ContadorDeLinhas += 1
NumeroLinhas = ContadorDeLinhas
print('Numero de linhas = ', NumeroLinhas) 

'''

'''

import linecache 
dict = {}
NomeAmostras_lista = []
ValorIntesidade_lista = []
Tupla=[]
i = 1
i2 = 3
while (i and i2 <= NumeroLinhas):
    global linhaEspecifica
    linhaEspecifica = linecache.getline('TLD_Resultado_TL.asc', i) 
    linhaEspecifica2 = linecache.getline('TLD_Resultado_TL.asc', i2)
    NomeAmostras_lista.append(linhaEspecifica)
    ValorIntesidade_lista.append(linhaEspecifica2)
    i = i + 3
    i2 = i2 + 3

    
'''
''' 

#Esse codigo lê o arquivo
arq = NomeAmostras_lista
linhas = NomeAmostras_lista
for Lerlinha1 in linhas:
    #Esse codigo exclui um simbolo ou letra
    characters = ',"'
    Lerlinha1 = ''.join( x for x in Lerlinha1 if x not in characters)
    PegueEstescharacters = "   "
    SubstituiPor = " /"
    Lerlinha1 = re.sub(PegueEstescharacters,SubstituiPor,Lerlinha1)
    print(Lerlinha1)





#Esse codigo lê o arquivo
arq = ValorIntesidade_lista
linhas = ValorIntesidade_lista
for Lerlinha in linhas:
    #Esse codigo exclui um simbolo ou letra
    characters = ',"'
    Lerlinha = ''.join( x for x in Lerlinha if x not in characters)
    PegueEstescharacters = "\t"
    SubstituiPor = ","
    Lerlinha = re.sub(PegueEstescharacters,SubstituiPor,Lerlinha)
    #print(Lerlinha)





#Codigo para converter 2 listas em 1 tupla
for i in range(3): #dict[ key ] = value
    dict[NomeAmostras_lista[i]] = ValorIntesidade_lista[i]

#Codigo para converter 1 tupla em 1 dicionario
#Dict = dict((x, y) for x, y in tupla)

#print(Dict)
df = pd.DataFrame((zip(Lerlinha1, Lerlinha)))
dfT = df.transpose()
#df = pd.DataFrame(data=dict, index=[0])
#print(dfT)
dfT.to_csv("MelhorarConversor.csv", index=True)
#Estude a documentação Pandas para tentar pegar esta string e converter em planilha com comentario


































'''

#Não apague este código. Este é um bom codigo. Trbalhe nele para fazer um dicionario
with open('TLD_Resultado_TL.asc', 'r') as arquivo:
    LinhasEspecificas = [0, 3, 6] 
    for x, l_num in enumerate(arquivo): 
        if x in LinhasEspecificas: 
            print(l_num) 


contador2 = 3
while (contador2 < NumeroLinhas + 1):
    linhaEspecifica2 = linecache.getline('TLD_Resultado_TL.asc', contador2) 
    contador2   = contador2 + 3
    dict[linhaEspecifica] = 'linhaEspecifica2'




for i in range(3):
   tupla=(NomeAmostras_lista[i],ValorIntesidade_lista[i])
   Tupla.append(tupla)


with open('TLD_Resultado_TL.asc', 'r') as arquivo:
    texto = arquivo.readline(2)
    while arquivo:
        print(arquivo)
        arquivo = arquivo.readline()
    arquivo.close()  



#Esse codigo lê o arquivo
arq = open("TLD_Resultado_TL.asc")
linhas = arq.readlines()
for Lerlinha in linhas:
    #Esse codigo exclui um simbolo ou letra
    characters = ',"'
    Lerlinha = ''.join( x for x in Lerlinha if x not in characters)
    PegueEstescharacters = "   "
    SubstituiPor = ""
    Lerlinha = re.sub(PegueEstescharacters,SubstituiPor,Lerlinha)
    #print(Lerlinha)





# Codigo lê o documento .asc
array= np.genfromtxt(Lerlinha, dtype=np.float64, skip_header=7, deletechars="!#$%&'()*+, -./:;<=>?@[\\]^{|}~", comments='"') #imputar a partir de arquivo .dat, .txt etc
rows, columns = array.shape
print( ), print("Este arquivo .asc têm: Colunas = ", rows, " e Linhas = ", columns), print( )
x = array[0,:]
y = array[1::2,:] #Busca linhas impares e ingnora as pares
arquivo=np.vstack((x,y))
arquivo=arquivo.T  


with open('TLD_Resultado_TL.asc', 'r') as arquivo:
    texto = arquivo.readline(9)
    print(texto)



data = linecache.getline('TLD_Resultado_TL.asc', 1).strip()
print(data)

arquivo = open('TLD_Resultado_TL.asc', 'r')
lista = arquivo.readlines() # readlinesssssss
print(lista)
arquivo.close()




arq = open("TLD_Resultado_TL.asc")
linhas = arq.readlines()
for linha in linhas:
    print(linha)
arq.close()
'''
