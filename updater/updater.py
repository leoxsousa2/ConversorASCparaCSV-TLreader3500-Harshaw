import wget
import sys




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



    #Coloque um if para saber se tem conexão com internet // Else coloque mensagem que não tem internet
    #Tendo conexão, coloque if para verificar se a versão da internet é superior ao instalado // Else coloque mensagem que no momento não tem atualizações disponíveis para este programa.
    #Finalmente coloque para baixar a atualização 
    #Depois planejar automatização com arquivo python de subistituição de pastas e reinicialização do programa. Tudo automaticamente
    wget.download(GitHub, bar=BarradeProgresso) #Esse código vai chamar o def BarradeProgresso(current, total, width=80):

#urllib.error.HTTPError: HTTP Error 404: Not Found