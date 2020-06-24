# -*- coding: utf-8 -*-
import math

'CORTANTE'
'Método de calculo I'
def cortanteM1(Dic):
    from viga.flexaosimples import flexaosimples
    Sec = flexaosimples(Dic)

    t1 = Sec['t1']
    t2 = Sec['t2']
    a1 = min(t1/2,0.3*h)
    a2 = min(t2/2,0.3*h)
    Sec['a1'] = a1
    Sec['a2'] = a2

    l0 = Sec['l0']
    lef = (100*l0) + a1 + a2
    Sec['lef'] = lef

    fctm = 0.3*(Sec['fck']**(2/3))/10 #kN/cm²
    Sec['fctm'] = fctm

    fywk = Sec['fywk']
    fywd = fywk/(Sec['gs']*10)# kN/cm²
    Sec['fywd'] = fywd


    Vk = Sec['Vk']
    Vsd = Vk*Sec['gf']
        #Redução do cortante
    reduzir = False
    if reduzir == True:
        Vsd = Vsd*(lef-Sec['d'])/lef

    Vsdmin = 0.06*(Sec['fck']**(2/3))*Sec['bw']*0.9*Sec['d']/(Sec['gs']*10)

        # Concreto
    fctd = 0.7*fctm/Sec['gc']
    av =(1 - (Sec['fck']/250))
    fcd2 = 0.6*av*Sec['fcd'] #Tensão resistente na biela

    a = Sec['a']


    if a == 90:
        Vrd2 = (fcd2*Sec['bw']*0.9*Sec['d'])/2
    else:
        Vrd2 = fcd2*Sec['bw']*0.9*Sec['d']*(1+(1/math.tan(math.radians(Sec['fck']))))

    if Vsd >= Vrd2:
        print('''As bielas serão esmagadas.

        É necessário um redimencionamento ou aumento da resistência do concreto''')
        return redirect(url_for("newproject")) #recursividade


    else:
        Vc0 = 0.6*fctd*Sec['bw']*Sec['d']
        Vc = Vc0
        Vsw = Vsd - Vc
        Asw = Vsw/(0.9*Sec['d']*fywd*(math.sin(math.radians(a))
                               + math.cos(math.radians(a))))

    Sec['Vrd2'] = Vrd2
    Sec['Vsd'] = Vsd
    Sec['Vsdmin'] = Vsdmin


    Aswmin = 0.2*fctm*Sec['bw']*math.sin(math.radians(a))/fywd
    if Asw <= Aswmin:
        Asw = Aswmin

    Sec["Asw"] = Asw
    Sec["Aswmin"] = Aswmin

    return(Sec)


'Método de calculo II'
def cortanteM2(Dic):
    from viga.flexaosimples import flexaosimples
    Sec = flexaosimples(Dic)

        # Seção longitudinal
    t1 = Sec['t1']
    t2 = Sec['t2']
    a1 = min(t1/2,0.3*Sec['h'])
    a2 = min(t2/2,0.3*Sec['h'])
    Sec['a1'] = a1
    Sec['a2'] = a2

    l0 = Sec['l0']
    lef = 100*l0 + a1 + a2
    Sec['lef'] = lef

    t = 30 # Angulo da Biela de Compressão
    Sec['t'] = t

    Vk = Sec['Vk']
    Vsd = Vk*Sec['gf']
    Sec['Vsd'] = Vsd
        #Redução do cortante
    reduzir = False
    if reduzir == True:
        Vsd = Vsd*(lef-Sec['d'])/lef

    fywk = Sec['fywk']

    fctm = 0.3*(Sec['fck']**(2/3))/10 #kN/cm²
    Sec['fctm'] = fctm
    fywd = fywk/(Sec['gs']*10)# kN/cm²
    Sec['fywd'] = fywd

        # Concreto
    fcd = Sec['fck']/(Sec['gc']*10) # kN/cm²
    Sec['fcd'] = fcd

    fctd = 0.7*fctm/Sec['gc']
    Sec['fctd'] = fctd

    av =(1 - (Sec['fck']/250))
    Sec['av'] = av

    fcd2 = 0.6*av*fcd #Tensão resistente na biela
    Sec['fcd2'] = fcd2

    a = Sec['a']

    if a == 90:
        Vrd2 = (fcd2*Sec['bw']*0.9*Sec['d']*
                math.cos(math.radians(t))*math.sin(math.radians(t)))
    else:
        Vrd2 = fcd2*Sec['bw']*0.9*Sec['d']*(((1/math.tan(math.radians(t)))
                                    +(1/math.tan(math.radians(a))))
                                     *((math.sin(math.radians(t)))**2))

    Vsdmin = 0.2*0.3*(Sec['fck']**(2/3))*Sec['bw']*0.9*Sec['d']*(((1/math.tan(math.radians(t)))
                                    +(1/math.tan(math.radians(a))))
                                     *((math.sin(math.radians(t)))**2))/(Sec['gs']*10)
    Sec['Vsdmin'] = Vsdmin
    Sec['Vrd2'] = Vrd2
    if Vsd >= Vrd2:
        #print('''As bielas serão esmagadas.
        #É necessário um redimencionamento ou aumento do fck''')
        return redirect(url_for("newproject"))

    else:
        Vc0 = 0.6*fctd*Sec['bw']*Sec['d']
        if Vsd <= Vc0:
            Vc1 = Vc0
        elif Vrd2 == Vsd:
            Vc1 = 0
        elif Vsd > Vc0:
            Vc1 = Vc0*(Vrd2-Vsd)/(Vrd2-Vc0)
    Vc = Vc1
    Vsw = Vsd - Vc
    Asw = Vsw/(0.9*Sec['d']*fywd*(((1/math.tan(math.radians(t)))+
                            (1/math.tan(math.radians(a))))
                           *((math.sin(math.radians(a))))))
    Sec['Vc'] = Vc
    Sec['Vsw'] = Vsw

    Aswmin = 0.2*fctm*Sec['bw']*math.sin(math.radians(a))/fywd
    Sec["Aswmin"] = Aswmin
    if Asw <= Aswmin:
        Asw = Aswmin
    Sec["Asw"] = Asw


    return(Sec)
'''def susp():
    alinhamento = 0 # face inf. da 2º esta acima da face inf. da 1º
    if alinhamento == 0:
        Asusp = (Sec['Vsd']/Sec['fyd'])*(ha/hapoio)
    elif alinhamento == 1: # face inf. da 2º esta abaixo da face inf. da 1º
        Asusp = (Sec['Vsd']/Sec['fyd'])'''
