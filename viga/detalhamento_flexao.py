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

    return (Sec)
