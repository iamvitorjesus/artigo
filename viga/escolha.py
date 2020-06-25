def choose_rebar(Dic, M):
    ol = Dic['ol']
    o = M[ol][0]
    ave = max(2, o, 0.5*Dic['Dmax']) #Espaçamento vertical mínimo

    aho = max(2, o, 1.2*Dic['Dmax']) #Espaçamento horizontal mínimo

    nbmax = math.floor((Dic['bw'] - (2* (Dic['c'][0] + Dic['ot']) ) + aho)/(o+aho))
    # print('\nNúmero máximo de barras por camada: %d'%nbmax)
    nc = math.ceil((M[ol][1])/nbmax)
