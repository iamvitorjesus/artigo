# -*- coding: utf-8 -*-
def detalhamento_cortante(Sec):
    import math
    '''Detalhamento da Seção Longitudinal'''
    #Escolha do diametro do estribo
    Barras = [4.2,5.0,6.3,8.0,10,12.5,16,20,22,25,32,40]# Opções comerciais de diametro (mm) de barra

    otmax = Sec['bw'] #mm
    ot = Sec['ot'] #Escolha inicial

    #Espaçamento máximo entre estribos
    if Sec['Vsd'] <= 0.67*Sec['Vrd2']:
        Smax = 0.6*Sec['d']
        if Smax > 30: # Descobri que esse teste é mais rapido
            Smax = 30 # que a função min()

    else:
        Smax = 0.3*Sec['d']
        if Smax > 20:
            Smax = 20
    Sec['Smax'] = Smax

    #Espaçamento máximo entre ramos
    if Sec['Vsd'] <= 0.2*Sec['Vrd2']:
        Stmax = Sec['d']
        if Stmax > 80:
            Stmax = 80
    else:
        Stmax = 0.6*Sec['d']
        if Stmax > 35:
            Stmax = 35
    Sec['Stmax'] = Stmax

    #Calculo do número de ramos
    ra = 2
    while True:
        if((Sec['bw']-(2*Sec['c']))/(ra-1)) < Stmax:
            break
        else:
            ra +=1
    #Menu de opções
    #M = {}
    #for di in Barras:
        #if di > otmax:
            #break
    A = ra*(math.pi)*((float(ot)/10)**2)/4 #Área dos ramos de um estribo em cm² *
    S = A/Sec["Asw"] #Espaçamento real entre os estribos
    Smin = A/Sec['Aswmin']
    S = round(S,1) #Número real de barras
    Smin = round(Smin,1)
    if S > Smax:
        S = Smax
    if Smin > Smax:
        Smin = Smax

    ne = (Sec['l0'] + Sec['t1'] + Sec['t2'])/S
    ne = math.ceil(ne)
    #di = float(di)
    #di = float(round((di/10),2))
    #M[di]= [S , Smin, ne] #Output
    #print(M)
    Sec['S'] = S
    Sec['Smin'] = Smin
    Sec['ne'] = ne

    return(Sec)
