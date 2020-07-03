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

    A = (math.pi)*(float(ol)**2)/4 #Área de uma barra em cm² *
    nb = Sec['As']/A #Número de barras necessárias
    nb = math.ceil(nb) #Número real de barras
    Sec['nb']= nb # Número  real de barras

    Aef = nb*A #Área efetiva de aço
    Aef = round(Aef,2)
    Sec['Aef']= Aef # Área efetiva de aço

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

#    if Sec['ganchol'] = 'a': # 9.4.6.1 Ganchos dos estribos
#        if  5 >= 5*(ot/10):
#            Sec['Anc_ol'] = 5*2 # Dois ganchos de 5 cm
#        else:
#            Sec['Anc_ol'] = 5*(ot/10)*2
#    elif Sec['ganchot'] = 'b':
#        if  7 >= 10*(ol/10):
#            Sec['Anc_ol'] = 7*2 # Dois ganchos de 7 cm
#        else:
#            Sec['Anc_ol'] = 10*(ot/10)*2

        # Armadura de Pele
    if Sec['h'] > 60:
        nsp_face = math.ceil(Sec['Asp_face']/((math.pi)*((Sec['op']/10)**2)/4))
        e = Sec['d']/nsp_face
        if e > 20:
            e = 20
        Sec['nsp_face'] = nsp_face
        Sec['e'] = e
        Sec['comp_op'] = (Sec['l0']*100) + Sec['t1'] + Sec['t2']
        for d in Bar:
            if d[0] == Sec['op']:
                Sec['ro_op'] = d[1]
        Sec['peso_op'] = Sec['ro_op']*(Sec['comp_op']/100)*nsp_face*2

    Sec['comp_ol'] = (Sec['l0']*100) + Sec['t1'] + Sec['t2']   # Comprimento de um estribo (cm) + Sec['Anc_ol']

    for d in Bar:
        if d[0] == Sec['ol']:
            Sec['ro_ol'] = d[1]
    Sec['peso_ol'] = Sec['ro_ol']*(Sec['comp_ol']/100)*nb # Peso total kg

    return (Sec)
