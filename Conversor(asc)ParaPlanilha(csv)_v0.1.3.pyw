from time import strftime        #Biblioteca de tempo
print('Log de Eventos')
print(' ')
print(' ')
print("--> Programa Iniciado")
DIAS = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'] #Isto é chamado de Vetor onde cada dia da semana representa um número, logo você pode traduzir um proggraa  dessa forma.
Dia_Semana = DIAS[int(strftime('%w'))]
Data = strftime('%d/%m/%Y')
relogio = strftime('%H:%M:%S')
print(Dia_Semana)
print(Data)
print(' ')
print(' ')
print(' ')

from time import sleep
import numpy as np   # Biblioteca
import os
from PyQt5 import uic,QtWidgets                     #Biblioteca de Layout (Responsavel pela Janela do Programa
import os                                           #biblioteca para manipular arquivos
import wget
import sys


#GitHub = 'https://github.com/leoxsousa2/ConversorASCparaCSV-TLreader3500-Harshaw/archive/refs/heads/main.zip' #Exemplo
GitHub = 'http://www.futurecrew.com/skaven/song_files/mp3/razorback.mp3' #Exemplo

def Ativador_1(self):    #Selecionar Arquivo
    global CaminhodoArquivo   #Obs:Este comando faz com que a palavra "arquivo" seja visto pelo def Ativador_2(): e o resto do programa, ou seja, vira uma variável glogal.
    global SomenteNomedoArquivo
    CaminhodoArquivo = QtWidgets.QFileDialog.getOpenFileName(None, 'Selecione o arquivo TL', '', 'Tipo do arquivo (*.asc)')[0]
    #CaminhodoArquivo.setNameFilter('.asc')
    SomenteNomedoArquivo = os.path.basename(CaminhodoArquivo)
    tela_11.progressBar_2.setValue(30)
    sleep(1)
    tela_11.label_5.setText('Clique em converter!')
    tela_11.textBrowser.setText(SomenteNomedoArquivo)
    tela_11.progressBar_2.setValue(50)
    # Codigo lê o documento .asc
    array= np.genfromtxt(SomenteNomedoArquivo, dtype=np.float64, skip_header=7, deletechars="!#$%&'()*+, -./:;<=>?@[\\]^{|}~", comments='"') #imputar a partir de arquivo .dat, .txt etc
    rows, columns = array.shape
    Rows = str(rows)                    #Transformar para String
    Columns = str(columns)              #Transformar para String 
    print( ), print("Este arquivo .asc têm: Colunas = ", rows, " e Linhas = ", columns), print( )
    tela_11.label_5.setText('Clique em Converter!')
    tela_11.label_6.setText('Este arquivo .asc tem: Colunas = ' +Rows+' e Linhas = '+Columns) 
    return 




def Ativador_2():    #Selecionar Arquivo #Obs:O (arquivo) é uma variavél vinda do def Ativador_1():
    tela_11.progressBar_2.setValue(80)           #Ajustando a barra de progresso
    tela_11.label_5.setText('Por favor aguarde!')  
    # Codigo lê o documento .asc
    array= np.genfromtxt(SomenteNomedoArquivo, dtype=np.float64, skip_header=7, deletechars="!#$%&'()*+, -./:;<=>?@[\\]^{|}~", comments='"') #imputar a partir de arquivo .dat, .txt etc
    rows, columns = array.shape
    print( ), print("Este arquivo .asc têm: Colunas = ", rows, " e Linhas = ", columns), print( )
    x = array[0,:]
    y = array[1::2,:] #Busca linhas impares e ingnora as pares
    arquivo=np.vstack((x,y))
    arquivo=arquivo.T        
    np.savetxt('./convert-Resultado_TL.csv', arquivo, fmt='%.f', delimiter=';', header='')#10decimais
    tela_11.progressBar_2.setValue(0)
    #Comando for para criar o efeito de carregamento da barra de progresso
    for i in range(101):
        sleep(0.01)
        tela_11.progressBar_2.setValue(i)
    tela_11.label_5.setText(Dia_Semana+' - '+Data+' - Conversão feita com sucesso!')
    tela_11.label_6.setText('  ') 
    return 

def Ativador_Sobre():
    tela_11.frame_1.show()
    return

def Ativador_FecharFreme():
    tela_11.frame_1.close()
    tela_11.progressBar_2.setValue(0)
    return

def BarradeProgresso(current, total, width=80):  #Barra de progresso do atualizador
    "%d%% [%d / %d] bytes" % (current / total * 100, current, total)
    calculoPorcentagem = str(int(current / total * 100))
    totalMB = str(int(1/2))
    #tela_11.label_7.setText('Baixando arquivo: ' + calculoPorcentagem + '%')
    #sys.stdout.write("\r" + '---->  ' + 'Baixando arquivo: ' + calculoPorcentagem + '%' + ' --> Total(MB): ' + f'{totalMB}' + ' Megabytes')
    #sys.stdout.flush()

    tela_11.progressBar_2.setValue(int(calculoPorcentagem))
    #for i in range(101):
    #    sleep(0.01)
    #    tela_11.progressBar_2.setValue(i)
     


def Ativador_Atualizador():
    #Coloque um if para saber se tem conexão com internet // Else coloque mensagem que não tem internet
    #Tendo conexão, coloque if para verificar se a versão da internet é superior ao instalado // Else coloque mensagem que no momento não tem atualizações disponíveis para este programa.
    #Finalmente coloque para baixar a atualização 
    #Depois planejar automatização com arquivo python de subistituição de pastas e reinicialização do programa. Tudo automaticamente
    wget.download(GitHub, bar=BarradeProgresso) #Esse código vai chamar o def BarradeProgresso(current, total, width=80):

#urllib.error.HTTPError: HTTP Error 404: Not Found
    return



#wget.download(GitHub, bar=Ativador_Atualizador)
#print('\n' + '\n' + 'Download completo. Pegue o arquivo na pasta onde está o arquivo.py') 



#-----Layout (Janelas do Programa)

app = QtWidgets.QApplication([])
tela_11=uic.loadUi("tela_1.ui")

tela_11.frame_1.close()
tela_11.pushButton_1.clicked.connect(Ativador_1)  #Seleciona o Arquivo
tela_11.pushButton_2.clicked.connect(Ativador_2)  #Envia o E-mail
tela_11.pushButton_3.clicked.connect(Ativador_Sobre)  #Envia o E-mail
tela_11.pushButton_4.clicked.connect(Ativador_FecharFreme)  #Envia o E-mail
tela_11.pushButton_5.clicked.connect(Ativador_Atualizador)  #Envia o E-mail


#-----Ativadoes Automáticos (Acesso Iniciando Programa)

tela_11.show()

app.exec()


#-----Fim_do_Código




#Comentários sobre o programa

# case1=array[::2,:]    #odd rows Busca linhas pares e ingnora as ímppares
# case2=array[1::2,:]   #even rows Busca linhas impares e ingnora as pares
# case3=array[:,::2]    #odd cols Busca Colunas pares e ingnora as ímppares
# case4=array[:,1::2]   #even cols Busca Colunas impares e ingnora as pares


# Converter arquivo python para programa .exe ((abra o cmd e coloque este codigo))
# pyinstaller Conversor-asc-paraPlanilha-csv_v0.1.3.pyw --onefile --noconsole
# pyinstaller Conversor-asc-paraPlanilha-csv_v0.1.3.pyw --onefile



# Codigo verifica os arquivos .asc dentro da pasta
#for file in os.listdir("./"):
#    if file.endswith(".asc"):
#        print('Seu arquivo está com o nome:', os.path.join(file))