# -*- coding: utf-8 -*-
def detalhamento_cortante(Sec):
    import math
    #Escolha do diametro do estribo
    Bar = [(4.2, 0.109),(5.0, 0.154),(6.3, 0.245),(8.0, 0.395),(10.0, 0.617),
    (12.5, 0.963),(16.0, 1.578),(20.0, 2.466),(22.0, 2.984),(25.0, 3.853),
    (32.0, 6.313),(40.0, 9.865)]# Opções comerciais de diametro (mm) de barra

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
            Sec['St'] = ((Sec['bw']-(2*Sec['c']))/(ra-1))

    Sec['ra'] = ra

    Abw = ra*(math.pi)*((float(ot)/10)**2)/4 #Área dos ramos de um estribo em cm² *
    S = Abw/Sec["Asw"] # Espaçamento real entre os estribos
    Smin = Abw/Sec['Aswmin'] # Espaçamento no trecho onde V = Vsdmin
    S = round(S,1)
    Smin = round(Smin,1)
    if S > Smax:
        S = Smax
    if Smin > Smax:
        Smin = Smax
    Sec['Abw'] = Abw

    ne = ((Sec['l0']*100) + Sec['t1'] + Sec['t2'])/S
    ne = math.ceil(ne) #Número real de barras

#    if Sec['ganchot'] = 'a': # 9.4.6.1 Ganchos dos estribos
#        if  5 >= 5*(ot/10):
#            Sec['Anc_ot'] = 5*2 # Dois ganchos de 5 cm
#        else:
#            Sec['Anc_ot'] = 5*(ot/10)*2
#    elif Sec['ganchot'] = 'b':
#    if  7 >= 10*(ot/10):
#        Sec['Anc_ot'] = 7*2 # Dois ganchos de 7 cm
#    else:
#        Sec['Anc_ot'] = 10*(ot/10)*2

    Sec['S'] = S
    Sec['Smin'] = Smin
    Sec['ne'] = ne
    Sec['comp_ot'] = ((Sec['bw'] - (4*Sec['c']))*2) + (Sec['h']*ra) + 14 #  + Sec['Anc_ot'] Comprimento de um estribo (cm)

    for d in Bar:
        if d[0] == ot:
            Sec['ro_ot'] = d[1]
    Sec['peso_ot'] = Sec['ro_ot']*(Sec['comp_ot']/100)*ne # Peso total kg

    return(Sec)
