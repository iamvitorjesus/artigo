def detalhamento_flexao(Dic):
    import math
    from viga.detalhamento_cortante import detalhamento_cortante


    Sec = detalhamento_cortante(Dic)

    Barras = [4.2,5,6.3,8,10,12.5,16,20,22,25,32,40]#Opções comerciais de diametro (mm) de barra

    M = {}
    for d in Barras:
        A = (math.pi)*((float(d)/10)**2)/4 #Área de uma barra em cm² *
        nb = Sec['As']/A #Número de barras necessárias
        nb = math.ceil(nb) #Número real de barras
        Aef = nb*A #Área efetiva de aço
        d = float(d)
        M[d]= [round((d/10),2) , nb , round(Aef,3)]#Output


    ol = Sec['ol']
    o = M[ol][0]
    ave = max(2, o, 0.5*Sec['Dmax']) #Espaçamento vertical mínimo
    Sec['ave'] = ave

    aho = max(2, o, 1.2*Sec['Dmax']) #Espaçamento horizontal mínimo
    Sec['aho'] = aho

    nbmax = math.floor((Sec['bw'] - (2* (Sec['c'][0] + Sec['ot']) ) + aho)/(o+aho)) # Número máximo de barras por camada
    Sec['nbmax'] = nbmax

    nc = math.ceil((M[ol][1])/nbmax) # Número de camadas necessáriaS
    Sec['nc']= M[ol][1]

    Sec['nb']= M[ol][1] # Número  real de barras
    Sec['Aef']= M[ol][2] # Área efetiva de aço



    #if nc*nbmax == M[ol][1]:
        # print ('\n%d camadas com %d barras' %(nc,nbmax))
    #else:
        #k = nc - 1
        #n = M[ol][1] - (k*nbmax)
        # print('\n%d camadas com %d barras e 1 camada com %d barras' %(k,nbmax,n))


    return (Sec)
