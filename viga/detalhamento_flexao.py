def detalhamento_flexao(Dic):
    import math
    from viga.detalhamento_cortante import detalhamento_cortante


    Sec = detalhamento_cortante(Dic)

    Barras = [4.2,5,6.3,8,10,12.5,16,20,22,25,32,40]#Opções comerciais de diametro (mm) de barra

    M = {}
    print('\nOpções de diâmetros de Barra Longitudinal')
    for d in Barras:
        A = (math.pi)*((float(d)/10)**2)/4 #Área de uma barra em cm² *
        nb = Sec['As']/A #Número de barras necessárias
        nb = math.ceil(nb) #Número real de barras
        Aef = nb*A #Área efetiva de aço
        d = float(d)
        M[d]= [round((d/10),2) , nb , round(Aef,3)]#Output

        ##################### Escolha da Armadura na pagina de Resultados
    # print('Sugestão de Diâmetro - entre 8mm e 16mm')
    #ol = Sec['ol']
    #o = M[ol][0]
    #ave = max(2, o, 0.5*Sec['Dmax']) #Espaçamento vertical mínimo

    #aho = max(2, o, 1.2*Sec['Dmax']) #Espaçamento horizontal mínimo

    #nbmax = math.floor((Sec['bw'] - (2*(Sec['c'] + Sec['ot'])) + aho)/(o+aho))
    # print('\nNúmero máximo de barras por camada: %d'%nbmax)
    #nc = math.ceil((M[ol][1])/nbmax)

    # print ('\nNúmero de camadas necessárias: %d' %nc)
    #if nc*nbmax == M[ol][1]:
        # print ('\n%d camadas com %d barras' %(nc,nbmax))
    #else:
        #k = nc - 1
        #n = M[ol][1] - (k*nbmax)
        # print('\n%d camadas com %d barras e 1 camada com %d barras' %(k,nbmax,n))

    return (M)
