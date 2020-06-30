def detalhamento_flexao(Dic):
    import math
    from viga.detalhamento_cortante import detalhamento_cortante


    Sec = detalhamento_cortante(Dic)

    Barras = [4.2,5.0,6.3,8,10,12.5,16,20,22,25,32,40]#Opções comerciais de diametro (mm) de barra

    ol = Sec['ol']/10
    ot = Sec['ot']/10
    #M = {}
    #for d in Barras:
    A = (math.pi)*((float(ol)/10)**2)/4 #Área de uma barra em cm² *
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

    nbmax = math.floor((Sec['bw'] - (2* (Sec['c'] + ot) ) + aho)/(ol+aho)) # Número máximo de barras por camada
    Sec['nbmax'] = nbmax

    x = (Sec['bw'] -(ol*nbmax)-((c+ot)*2) )/(nbmax-1) # Espaçamento real
    Sec['x'] = x

    nc = math.ceil(nb/nbmax) # Número de camadas necessáriaS
    #ol = str(ol)
    Sec['nc']= nc





    #if nc*nbmax == M[ol][1]:
        # print ('\n%d camadas com %d barras' %(nc,nbmax))
    #else:
        #k = nc - 1
        #n = M[ol][1] - (k*nbmax)
        # print('\n%d camadas com %d barras e 1 camada com %d barras' %(k,nbmax,n))


    return (Sec)
