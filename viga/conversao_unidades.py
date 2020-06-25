def conversao_unidades(Dic):
        # Geometria
    h = Dic['h']
    unith = Dic['unith']
    bw = Dic['bw']
    unitbw = Dic['unitbw']
    t1 = Dic['t1']
    unitt1 = Dic['unitt1']
    t2 = Dic['t2']
    unitt2 = Dic['unitt2']
    l0 = Dic['l0']
    unitl0 = Dic['unitl0']

    if unitbw == 2:
        bw = bw*100
    Dic["bw"] = bw ####

    if unith == 2:
        h = h*100
    Dic["h"] = h ####

    if unitt1 == 2:
        t1 = t1*100
    Dic['t1'] = t1 ####

    if unitt2 == 2:
        t2 = t2*100
    Dic['t2'] = t2 ####

    if unitl0 == 2:
        l0 = l0/100
    Dic['l0'] = l0 ####

        # Resistência e Esforços
    Es = Dic['Es']
    unitEs = Dic['unitEs']
    if unitEs == 2:
        Es = Es/1000
    elif unitEs == 3:
        Es = Es/1000000
    elif unitEs == 4:
        Es = Es/100
    Dic["Es"] = Es ####

    fck = Dic["fck"]
    unitfck = Dic['unitfck']
    if unitfck == 2:
        fck = fck*10
    elif unitfck == 3:
        fck = fck/1000
    Dic["fck"] = fck ####

    fyk = Dic["fyk"]
    unitfyk = Dic['unitfyk']
    if unitfyk == 2:
        fyk = fyk*10
    elif unitfck == 3:
        fyk = fyk/1000
    Dic["fyk"] = fyk ####

    fywk = Dic['fywk']
    unitfywk = Dic['unitfywk']
    if unitfywk == 2:
        fywk = fywk*10
    elif unitfywk ==3:
        fywk = fywk/1000
    Dic['fywk'] = fywk


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
    Dic['Mk'] = Mk ####

    Vk = Dic['Vk']
    unitVk = Dic['unitVk']
    if unitVk == 2:
        Vk = Vk/1000
    elif unitVk == 3:
        Vk = (Vk*10)/1000
    Dic['Vk'] = Vk

    CAA = Dic['CAA']
    if CAA == 1:
        c = 2.5#cm
        classe = 'Classe Ⅰ'
    elif CAA == 2:
        c = 3 #cm
        classe = 'Classe Ⅱ'
    elif CAA == 3:
        c = 4 #cm
        classe = 'Classe Ⅲ'
    elif CAA == 4:
        c = 5 #cm
        classe = 'Classe Ⅳ'
    Dic["c"] = [c, classe] ####

    Brita = Dic["Brita"]
    if Brita == 0:
        Dmax = 0.95 #cm
    elif Brita == 1:
        Dmax = 1.90 #cm
    elif Brita == 2:
        Dmax = 2.50 #cm
    elif Brita == 3:
        Dmax = 5.00 #cm
    Dic['Dmax'] = Dmax ####

    return Dic
