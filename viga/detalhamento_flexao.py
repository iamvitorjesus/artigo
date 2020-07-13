def detalhamento_flexao(Dic):
    import math
    from viga.detalhamento_cortante import detalhamento_cortante

    Sec = detalhamento_cortante(Dic)

            # Opções comerciais de diametro (mm) de barra
    Bar = [(4.2, 0.109),(5.0, 0.154),(6.3, 0.245),(8.0, 0.395),(10.0, 0.617),
    (12.5, 0.963),(16.0, 1.578),(20.0, 2.466),(22.0, 2.984),(25.0, 3.853),
    (32.0, 6.313),(40.0, 9.865)]

    ol = Sec['ol']/10
    ot = Sec['ot']/10
    ols = Sec['ols']/10

        # ARMADURA DE COMPRESSÃO
    Abs = (math.pi)*(float(ols)**2)/4 #Área de uma barra em cm² *
    nbs = Sec['Ass']/Abs #Número de barras necessárias
    nbs = math.ceil(nbs) #Número real de barras
    Sec['nbs'] = nbs # Número  real de barras
    Sec['Abs'] = Abs

    Aefs = nbs*Abs #Área efetiva de aço
    Aefs = round(Aefs,2)
    Sec['Aefs'] = Aefs # Área efetiva de aço

    aves = max(2, ols, 0.5*Sec['Dmax']) # Espaçamento vertical mínimo
    Sec['aves'] = aves

    ahos = max(2, ols, 1.2*Sec['Dmax']) # Espaçamento horizontal mínimo
    Sec['ahos'] = ahos

    nbmaxs = math.floor((Sec['bw'] - (2* (Sec['c'] + ot) ) + ahos)/(ols+ahos))
    Sec['nbmaxs'] = nbmaxs # Número máximo de barras por camada

    ahs = (Sec['bw'] -(ols*nbmaxs)-((Sec['c']+ot)*2) )/(nbmaxs-1)
    Sec['ahs'] = ahs # Espaçamento real

    ncs = math.ceil(nbs/nbmaxs) # Número de camadas necessárias
    Sec['ncs']= ncs


        # ARMADURA DE TRAÇÃO

    Ab = (math.pi)*(float(ol)**2)/4 #Área de uma barra em cm² *
    nb = Sec['As']/Ab #Número de barras necessárias
    nb = math.ceil(nb) #Número real de barras
    Sec['nb']= nb # Número  real de barras
    Sec['Ab'] = Ab

    Aef = nb*Ab #Área efetiva de aço
    Aef = round(Aef,2)
    Sec['Aef'] = Aef # Área efetiva de aço

    ave = max(2, ol, 0.5*Sec['Dmax']) # Espaçamento vertical mínimo
    Sec['ave'] = ave

    aho = max(2, ol, 1.2*Sec['Dmax']) # Espaçamento horizontal mínimo
    Sec['aho'] = aho

    nbmax = math.floor((Sec['bw'] - (2* (Sec['c'] + ot) ) + aho)/(ol+aho))
    Sec['nbmax'] = nbmax # Número máximo de barras por camada

    ah = (Sec['bw'] -(ol*nbmax)-((Sec['c']+ot)*2) )/(nbmax-1)
    Sec['ah'] = ah # Espaçamento real

    nc = math.ceil(nb/nbmax) # Número de camadas necessáriaS
    Sec['nc']= nc

        # Ancoragem de Armadura
    Sec['n1'] = 2.25 # Nervurada
    if Sec['Mk'] > 0:
        Sec['n2ol'] = 1 # Tração na Boa aderência
        Sec['n2ols'] = 0.7 # Compressão na Má aderência
    else:
        Sec['n2ol'] = 0.7 # Tração na Má aderência
        Sec['n2ols'] = 1 # Compressão na Boa aderência


    if Sec['ol'] < 32:
        Sec['n3ol'] = 1
    else:
        Sec['n3ol'] = (132 - Sec['ol'])/100

    if Sec['ols'] < 32:
        Sec['n3ols'] = 1
    else:
        Sec['n3ols'] = (132 - Sec['ols'])/100

    Sec['fbd_ol'] = Sec['n1']*Sec['n2ol']*Sec['n3ol']*Sec['fctd']
    Sec['fbd_ols'] = Sec['n1']*Sec['n2ols']*Sec['n3ols']*Sec['fctd']

    Sec['lbl'] = (ol/4)*(Sec['fyd']/Sec['fbd_ol']) # Comprimento Básico
    Sec['lblnec'] = (0.7*Sec['lbl'])*((Sec['As'])/Sec['Aef']) #Comprimento de ancoragem necessario para a armadura de pele
    Sec['lblmin'] = max(0.3*Sec['lbl'], 10*ol, 10)

    if Sec['lblnec'] < Sec['lblmin']:
        Sec['lblnec'] = Sec['lblmin']

    Sec['lbls'] = (ols/4)*(Sec['fyd']/Sec['fbd_ols'])
    Sec['lblsnec'] = (1*Sec['lbls'])*((Sec['Ass'])/Sec['Aefs']) #Comprimento de ancoragem necessario para a armadura de pele
    Sec['lblsmin'] = max(0.3*Sec['lbls'], 10*ols, 10)

    if Sec['lblsnec'] < Sec['lblsmin']:
        Sec['lblsnec'] = Sec['lblsmin']


        # 9.4.2.3 Ganchos das armaduras de tração

    if Sec['ganchol'] == 1:    # semicirculares, com ponta reta de comprimento não inferior a 2 φ.
        Sec['gan_ol'] = 2*ol    # Ganchos em cm
    elif Sec['ganchol'] == 2:  # em ângulo de 45° (interno), com ponta reta de comprimento não inferior a 4 φ.
        Sec['gan_ol'] = 4*ol    # Dois ganchos de 7 cm
    else:                       # em ângulo reto, com ponta reta de comprimento não inferior a a 8 φ.
        Sec['gan_ol'] = 8*ol

    Sec['lb1disp'] = Sec['t1'] - Sec['c']
    Sec['lb2disp'] = Sec['t2'] - Sec['c']
        # Armadura de Pele

    if Sec['h'] > 60:
        Sec['fbd_op'] = Sec['n1']*0.7*1*Sec['fctd']
        Sec['lbp'] = ((Sec['op']/10)/4)*(Sec['fyd']/Sec['fbd_op'])

        Sec['lbpmin'] = max(0.3*Sec['lbp'], Sec['op'], 10)

        nsp_face = math.ceil(Sec['Asp_face']/((math.pi)*((Sec['op']/10)**2)/4))
        e = Sec['d']/nsp_face
        if e > 20:
            e = 20
        Sec['nsp_face'] = nsp_face
        Sec['e'] = e
        Sec['comp_op'] = (Sec['l0']*100) + Sec['lb1disp'] + Sec['lb2disp']
        for d in Bar:
            if d[0] == Sec['op']:
                Sec['ro_op'] = d[1]
        Sec['peso_op'] = Sec['ro_op']*(Sec['comp_op']/100)*nsp_face*2

        Sec['Aspef'] = nsp_face*2*((math.pi)*((Sec['op']/10)**2)/4) # Área Efetiva da Armadura de Pele
        Sec['lbpnec'] = (1*Sec['lbp'])*((Sec['Asp_face']*2)/Sec['Aspef']) #Comprimento de ancoragem necessario para a armadura de pele
        if Sec['lbpnec'] < Sec['lbpmin']:
            Sec['lbpnec'] = Sec['lbpmin']



    if Sec['lb1disp'] >= Sec['lblnec']:
        Sec['lblk1'] = Sec['lb1disp']
    else:
        Sec['lblk1'] = Sec['lblnec']

    if Sec['lb2disp'] >= Sec['lblnec']:
        Sec['lblk2'] = Sec['lb2disp']
    else:
        Sec['lblk2'] = Sec['lblnec']

    Sec['comp_ol'] = Sec['gan_ol'] + Sec['lblk1'] + (Sec['l0']*100) + Sec['lblk2'] + Sec['gan_ol']  # Comprimento de um estribo (cm)

    for d in Bar:
        if d[0] == Sec['ol']:
            Sec['ro_ol'] = d[1]
    Sec['peso_ol'] = Sec['ro_ol']*(Sec['comp_ol']/100)*nb # Peso total kg


    Sec['comp_ols'] = (Sec['l0']*100) + Sec['lb1disp'] + Sec['lb2disp']   # Comprimento de um estribo (cm) + Sec['Anc_ol']

    for d in Bar:
        if d[0] == Sec['ols']:
            Sec['ro_ols'] = d[1]
    Sec['peso_ols'] = Sec['ro_ols']*(Sec['comp_ols']/100)*nbs # Peso total kg


    xi = (Sec['c']*10) + Sec['ot'] + (Sec['ol']/2)
    yi = Sec['h'] - ((Sec['c']*10) + Sec['ot'] + (Sec['ol']/2))

    xs = (Sec['c']*10) + Sec['ot'] + (Sec['ols']/2)
    ys = xs


    if Sec['Mk'] < 0:
        yi = (Sec['c']*10) + Sec['ot'] + (Sec['ol']/2)
        ys = Sec['h'] - ((Sec['c']*10) + Sec['ot'] + (Sec['ols']/2))



        #   conta feita em milimetros
    c = Sec['c']*10
    ahult = 0
    nbhul = 0
    if nc*nbmax != nb:
        k = nc - 1
        nbult = nb - (k*nbmax)
        if nbult > 1:
            ahult = (Sec['bw'] - (nbult*Sec['ol'] + ((c+Sec['ot'])*2)))/(nbult-1)




    P = [] # Matriz de posição das barras
    i = 1 # Contador de barras
    k = 1 # Contador de camadas
    while i < Sec['nb'] + 1 :
        if cam == nc:
            ah = ahult

        P.append([xi, yi])
        xi +=
        if k == Sec['nbmax']:
            xi = (Sec['c']*10) + Sec['ot'] + (Sec['ol']/2)
            yi +=  Sec['ol'] + (ave*10)
            k = 1
            cam = 1

        i += 1
        k += 1



    return (Sec)
