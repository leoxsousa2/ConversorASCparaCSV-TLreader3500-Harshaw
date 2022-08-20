
	# -*- coding: utf-8 -*-
print('')
print(' **************************************************************************************************************')
print(' ')
print('                                           REGISTRO DO PROGRAMA')
print('')
print('   NOME: Conversor de .asc para .csv')
print('   AUTOR: Leo Sousa')
print('   CONTRIBUIÇÕES: Jaelsson e Vinicius')
print('   VERSÃO: 0.1.3')
print('   LINGUAGEM: Python3.10.6')
print('   Formato: .py e .exe')
print('   Editor: Spider-python, Jupiter e GoogleColab')
print('   Propósito: Converter arquivo de dados do TL Reader UFS para formato compatível com OriginLab')
print('   E-mail: leoxsousa2@gmail.com')
print('   https://github.com/leoxsousa2/ConversorASCparaCSV-TLreader3500-Harshaw')
print('')
print(' **************************************************************************************************************')
print(' ')
print(' ')


import numpy as np   # Biblioteca
import os



# Codigo verifica os arquivos .asc dentro da pasta
for file in os.listdir("./"):
    if file.endswith(".asc"):
        print('Seu arquivo está com o nome:', os.path.join(file))
        

# Codigo lê o documento .asc
array= np.genfromtxt(os.path.join(file), dtype=np.float64, skip_header=7, deletechars="!#$%&'()*+, -./:;<=>?@[\\]^{|}~", comments='"') #imputar a partir de arquivo .dat, .txt etc
rows, columns = array.shape
print( ), print("Este arquivo .asc têm: Colunas = ", rows, " e Linhas = ", columns), print( )

Fim = input('Este programa vai gerar um arquivo chamado "convert-Resultado_TL.csv". Clique "Enter" para continuar ... ') # Este input é para segurar o cmd aberto até apertar enter


x = array[0,:]
y = array[1::2,:] #Busca linhas impares e ingnora as pares
arquivo=np.vstack((x,y))
arquivo=arquivo.T        

np.savetxt('./convert-Resultado_TL.csv', arquivo, fmt='%.f', delimiter=';', header='')#10decimais



#Comentários sobre o programa

# case1=array[::2,:]    #odd rows Busca linhas pares e ingnora as ímppares
# case2=array[1::2,:]   #even rows Busca linhas impares e ingnora as pares
# case3=array[:,::2]    #odd cols Busca Colunas pares e ingnora as ímppares
# case4=array[:,1::2]   #even cols Busca Colunas impares e ingnora as pares


# Converter arquivo python para programa .exe ((abra o cmd e coloque este codigo))
# pyinstaller ConversorParaPlanilha.py --onefile --noconsole
# pyinstaller ConversorParaPlanilha.py --onefile
