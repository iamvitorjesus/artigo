def escolha(Dic, M):
    ol = Dic['ol']
    o = M[ol][0]
    ave = max(2, o, 0.5*Dic['Dmax']) #Espaçamento vertical mínimo

    aho = max(2, o, 1.2*Dic['Dmax']) #Espaçamento horizontal mínimo

    nbmax = math.floor((Dic['bw'] - (2* (Dic['c'][0] + Dic['ot']) ) + aho)/(o+aho)) # Número máximo de barras por camada
    nc = math.ceil((M[ol][1])/nbmax) # Número de camadas necessáriaS

        #if nc*nbmax == M[ol][1]:
            # print ('\n%d camadas com %d barras' %(nc,nbmax))
        #else:
            #k = nc - 1
            #n = M[ol][1] - (k*nbmax)
            # print('\n%d camadas com %d barras e 1 camada com %d barras' %(k,nbmax,n))
