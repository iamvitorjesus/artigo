# -*- coding: utf-8 -*-
import math

def flexaosimples(Dic):
        # Seção Transversal
    h = Dic['h']
    bw = Dic['bw']

    c = Dic['c']

    d1 = c + 1
    Dic["d1"] = d1
    if Dic['parametrod_'] == 'on':
        Dic['d1'] = Dic['d_']

    Dic["d2"] = Dic['d1']

        # Materiais
    if Dic['carregamento'] == 1:
        Dic["gc"] = 1.40 # Coeficiente de Minoração da Resistência do Concreto
        Dic["gs"] = 1.15 # Coeficiente de Minoração da Resistência do Aço
    elif Dic['carregamento'] == 2:
        Dic["gc"] = 1.20
        Dic["gs"] = 1.15
    elif Dic['carregamento'] == 3:
        Dic["gc"] = 1.20
        Dic["gs"] = 1.00
    Dic["gf"] = Dic["gc"] # Coeficiente de Majoração do Esforço
    gc = Dic["gc"]
    gs = Dic["gs"]
    gf = Dic["gf"]

    Es = Dic['Es'] # GPa

    fck = Dic["fck"] # MPa
    fyk = Dic["fyk"] # MPa

        # Esforços
    Mk = Dic['Mk']
    if Mk < 0:
        Mk = (-1)*Mk

     # kN.cm
    # TRATAMENTO DE DADOS
    Msd = Mk*gf # kN.cm
    Dic["Msd"] = Msd
    d = h - Dic['d1'] # cm
    Dic["d"] = d

    fcd = fck/(gc*10) # kN/cm²
    Dic["fcd"] = fcd

    fyd = fyk/(gs*10) # kN/cm²
    Dic["fyd"] = fyd


    if fck <= 50:
        ac = 0.85
        nlim = 0.45
        y = 0.8 #lambda
        eu = 3.5/1000 # Deformação especifica do Concreto
    else: # Para Concreto de Alta Resistência
        ac = 0.85 - ((fck - 50)/200)
        nlim = 0.35
        y = 0.8 - ((fck - 50)/400)
        eu = (2.6 + 35*(((90 - fck)/100)**4))/1000
    Dic['ac'] = ac
    Dic['y'] = y
    Dic['eu'] = eu
    Dic['nlim'] = nlim

    if fyk == 250:
        eyd = 1.04/1000 # Deformação especifica do Aço
    elif fyk == 500:
        eyd = 2.07/1000
    else:
        eyd = 2.48/1000
    Dic['eyd'] = eyd

        # Modo de Ruptura
    x2lim = (eu/(eu+(10/1000)))*d
    x3lim = (eu/(eu+eyd))*d
    Dic['x2lim'] = x2lim
    Dic['x3lim'] = x3lim


    'Cálculo da Armadura'
    xlim = nlim*d
    Dic['xlim'] = xlim
    Msdlim = y*ac*nlim*(d**2)*bw*fcd*(1-(0.4*nlim))
    Dic['Msdlim'] = Msdlim
    cal = 0
    if Msdlim >= Msd:
        # Armadura simples
        x = (d/y)*(1-((1-((2*Msd)/(bw*(d**2)*ac*fcd)))**(0.5))) # Linha Neutra
        As = Msd/(fyd*(d-(0.4*x)))
        Dic['ols'] = 8.0
        Ass = 2*(math.pi)*((0.8)**2)/4 # Porta estribo
    else:
        # Armadura dupla
        cal = 1
        x = xlim
        Md1 = Msdlim
        Dic['Md1'] = Md1
        Md2 = Msd - Md1
        Dic['Md2'] = Md2
        As1 = Md1/(fyd*(d-(0.4*x)))
        As2 = Md2/(fyd*(d-d2))
        es = ((xlim - d2)*eu)/xlim # deformação sofrida pela armadura superior
        Dic['As1'] = As1
        Dic['As2'] = As2
        Dic['es'] = es
        if es >= eyd:
            Dsd = fyd
        else:
            Dsd = es*(Es*100) #kN/cm²
        Dic['Dsd'] = Dsd # Tensão proporcional a deformação sofrida pela armadura superior (Lei de Hooke)
        Ass = Md2/(Dsd*(d-d2))
        As = As1 + As2

    Dic['cal'] = cal
    Dic["x"] = x

        # Armadura Minima
    if 0.0015*bw*d >= As:
        As = 0.0015*bw*d

    Dic["As"] = As
    Dic["Ass"] = Ass

        # Armadura de Pele
    if h > 60:
        Asp_face = (0.1/100)*bw*h
        Dic['Asp_face'] = Asp_face


    return(Dic)
