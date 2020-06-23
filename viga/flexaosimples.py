# -*- coding: utf-8 -*-
import math

def flexaosimples(Dic):
    #Seção Transversal

        # CONVERSÃO DE UNIDADES
    if Dic['unitbw'] == 'm':
        Dic['bw'] = Dic['bw']*100
        Dic['unitbw'] = 'cm'

    if Dic['unith'] == 'm':
        Dic['h'] = Dic['h']*100
        Dic['unith'] = 'cm'

    CAA = Dic['CAA']

    #Escolha do cobrimento
    if CAA == 1:
        c = 2.5#cm
    elif CAA == 2:
        c = 3 #cm
    elif CAA == 3:
        c = 4 #cm
    elif CAA == 4:
        c = 5 #cm
    d1 = c+1
    d2 = d1

    #Materiais
    gc = Dic["gc"] #
    gf = gc # Coeficiente de Majoração do Esforço de Flexão
    gs = Dic["gs"]

    Es = Dic['Es'] #210 GPa
    unitEs = Dic['unitEs']
    if unitEs == 2:
        Es = Es/1000
    elif unitEs == 3:
        Es = Es/1000000
    elif unitEs == 4:
        Es = Es/100

    fck = Dic["fck"]
    unitfck = Dic['unitfck']
    if unitfck == 2:
        fck = fck*10
    elif unitfck == 3:
        fck = fck/1000

    fyk = Dic["fyk"]
    unitfyk = Dic['unitfyk']
    if unitfyk == 2:
        fyk = fyk*10
    elif unitfck == 3:
        fyk = fyk/1000

    Dmax = Dic["Dmax"]


    #Esforços
    Mk = Dic['Mk']
    unitMk = Dic['unitMk']
    if unitMk == 1:
        Mk = Mk*100
    elif unitMk == 3:
        Mk = (Mk*10)*100
    elif unitMk == 4:
        Mk = (Mk*10)
    elif unitMk == 5:
        Mk = ((Mk*10)*1000)*100
    elif unitMk == 6:
        Mk = (Mk*10)*1000
        
    # TRATAMENTO DE DADOS
    Msd = Mk*gf
    d = h - d1

    if Dmax == 0:
        Dmax = 0.95 #cm
    elif Dmax == 1:
        Dmax = 1.90 #cm
    elif Dmax == 2:
        Dmax = 2.50 #cm
    elif Dmax == 3:
        Dmax = 5.00 #cm

    fcd = fck/(gc*10) # kN/cm²
    fyd = fyk/(gs*10)# kN/cm²

    if fck <= 50:
        ac = 0.85
        nlim = 0.45
        y = 0.8 #lambda
        eu = 3.5/1000 # Deformação especifica do Concreto
    else: # Para Concreto de Alta Resistência
        ac = 0.85 - ((fck - 50)/200)
        nlim = 0.35
        y = 0.8 - ((fck - 50)/400)
        eu = 2.6 + 35*(((90 - fck)/100)**4)


    if fyk == 250:
        eyd = 1.04/1000 # Deformação especifica do Aço
    elif fyk == 500:
        eyd = 2.07/1000
    else:
        eyd = 2.48/1000

    # Modo de Ruptura
    x2lim = (eu/(eu+(10/1000)))*d
    x3lim = (eu/(eu+eyd))*d

    'Cálculo da Armadura'
    xlim = nlim*d
    Msdlim = y*ac*nlim*(d**2)*bw*fcd*(1-(0.4*nlim))
    if Msdlim >= Msd:
        #Armadura simples
        x = (d/y)*(1-((1-((2*Msd)/(bw*(d**2)*ac*fcd)))**(0.5))) # Linha Neutra
        As = Msd/(fyd*(d-(0.4*x)))
        Ass = 2*(math.pi)*((1.2)**2)/4
    else:
        #Armadura dupla
        x = xlim
        Md1 = Msdlim
        Md2 = Msd - Md1
        As1 = Md1/(fyd*(d-(0.4*x)))
        As2 = Msd/(fyd*(d-d2))
        es = ((xlim - d2)*eu)/xlim
        if es >= eyd:
            Dsd = fyd
        else:
            Dsd = es*(Es*100) #kN/cm²
        Ass = Md2/(Dsd*(d-d2))
        As = As1 + As2

    Sec["bw"] = bw
    Sec["h"] = h
    Sec["d"] = d
    Sec["d1"] = d1
    Sec["d2"] = d2

    Sec["CAA"] = CAA
    Sec["c"] = c
    Sec["Es"] = Es
    Sec["gc"] = gc
    Sec["gf"] = gf
    Sec["gs"] = gs

    Sec["Msd"] = Msd

    Sec["fck"] = fck
    Sec["fyk"] = fyk
    Sec["fcd"] = fcd
    Sec["fyd"] = fyd
    Sec['Dmax'] = Dmax
        #Armadura Minima
    if 0.0015*bw*d >= As:
        As = 0.0015*bw*d

        #Armadura Máxima
    if As + Ass >= 0.04*bw*h:
        print('Erro: Redimencionar Ac')
        print()
        print("SUGESTÃO: Aumentar a Altura")
        return flexaosimples()
    else:
        print('\n\nArmadura Longitudinal Positiva: As = %.2fcm²\nArmadura Longitudinal Negativa: Ass = %.2fcm²\n' %(As, Ass))
        Sec["As"] = As
        Sec["Ass"] = Ass

    x = round(x, 2)


    S = '''             DIMENSIONAMENTO


Momento fletor de cálculo:
        Md = γf.Mk = %.2f.%d = %d kN.cm

sendo γf o coeficiente de ponderação que majora
os esforços solicitantes.

Linha neutra:
        x = %.2f cm

Como x < 0,45.d = 0,45.%d = %.2f cm, segue-se
que o não há necessidade de armadura dupla.

De posse da posição da linha neutra e do momendo
fletor de dimensionamento, temos a Armadura
Longitudinal de Fleção.

Portanto,
        As = Md/[fyd.(d- 0.4*x)]
        As = %.2f cm²'''

    #print(S %(gf, Mk, Msd, x, d, (0.45*d), As))
    return(Sec)
