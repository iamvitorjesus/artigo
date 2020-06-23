# -*- coding: utf-8 -*-
import math

'CORTANTE'
'Método de calculo I'
def cortanteM1(Dic):
    from viga.flexaosimples import flexaosimples
    Sec = flexaosimples(Dic)

    # Tratamento de Dados
    Vk = Sec['Vk']
    t1 = Sec['t1']
    t2 = Sec['t2']
    l0 = Sec['l0']
    a1 = min(t1/2,0.3*h)
    a2 = min(t2/2,0.3*h)
    lef = 100*l0 + a1 + a2

    fctm = 0.3*(Sec['fck']**(2/3))/10 #kN/cm²

    fywk = int(input("Resistência Caracteristica do Estribo (MPa): "))
    fywd = fywk/(Sec['gs']*10)# kN/cm²

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

    a = int(input("Ângulo do estribo (graus): "))

    if a == 90:
        Vrd2 = (fcd2*Sec['bw']*0.9*Sec['d'])/2
    else:
        Vrd2 = fcd2*Sec['bw']*0.9*Sec['d']*(1+(1/math.tan(math.radians(Sec['fck']))))

    if Vsd >= Vrd2:
        print('''As bielas serão esmagadas.

        É necessário um redimencionamento ou aumento da resistência do concreto''')
        return cortanteM1() #recursividade

    else:
        Vc0 = 0.6*fctd*Sec['bw']*Sec['d']
        Vc = Vc0
        Vsw = Vsd - Vc
        Asw = Vsw/(0.9*Sec['d']*fywd*(math.sin(math.radians(a))
                               + math.cos(math.radians(a))))

    Aswmin = 0.2*fctm*Sec['bw']*math.sin(math.radians(a))/fywd
    if Asw <= Aswmin:
        Asw = Aswmin

    Sec["Asw"] = Asw
    Sec["Aswmin"] = Aswmin

    Sec['t1'] = t1
    Sec['t2'] = t2
    Sec['l0'] = l0
    Sec['lef'] = lef
    Sec['a1'] = a1
    Sec['a2'] = a2

    Sec['fctm'] = fctm
    Sec['fywk'] = fywk
    Sec['fywd'] = fywd

    Sec['Vsd'] = Vsd
    Sec['Vsdmin'] = Vsdmin
    Sec['Vrd2'] = Vrd2
    Sec['a'] = a

    return(Sec)


'Método de calculo II'
def cortanteM2():
    from viga.flexaosimples import flexaosimples
    Sec = flexaosimples()

        # Seção longitudinal
    Vk = float(input("Esforço Cortante (kN): "))
    t1 = int(input("Espessura do pilar de apoio da esquerda (cm): "))
    t2 = int(input("Espessura do pilar de apoio da direita (cm): "))
    l0 = int(input("Comprimento do vão livre entre os pilares (cm): "))
    a1 = min(t1/2,0.3*Sec['h'])
    a2 = min(t2/2,0.3*Sec['h'])
    lef = 100*l0 + a1 + a2

    t = 30 # Angulo da Biela de Compressão
    Sec['t'] = t

    Vsd = Vk*Sec['gf']
        #Redução do cortante
    reduzir = False
    if reduzir == True:
        Vsd = Vsd*(lef-Sec['d'])/lef

    fywk = int(input("Resistência Caracteristica do Estribo (MPa): "))

    fctm = 0.3*(Sec['fck']**(2/3))/10 #kN/cm²
    fywd = fywk/(Sec['gs']*10)# kN/cm²

        # Concreto
    fcd = Sec['fck']/(Sec['gc']*10) # kN/cm²
    fctd = 0.7*fctm/Sec['gc']
    av =(1 - (Sec['fck']/250))
    fcd2 = 0.6*av*fcd #Tensão resistente na biela

    a = int(input("Ângulo do estribo (graus): "))

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

    if Vsd >= Vrd2:
        print('''As bielas serão esmagadas.
        É necessário um redimencionamento ou aumento do fck''')
        return cortanteM2()

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

    Aswmin = 0.2*fctm*Sec['bw']*math.sin(math.radians(a))/fywd
    if Asw <= Aswmin:
        Asw = Aswmin

    Sec["Asw"] = Asw
    Sec["Aswmin"] = Aswmin

    Sec['t1'] = t1
    Sec['t2'] = t2
    Sec['l0'] = l0
    Sec['lef'] = lef
    Sec['a1'] = a1
    Sec['a2'] = a2

    Sec['fctm'] = fctm
    Sec['fywk'] = fywk
    Sec['fywd'] = fywd

    Sec['Vsd'] = Vsd
    Sec['Vsdmin'] = Vsdmin
    Sec['Vrd2'] = Vrd2
    Sec['a'] = a

    return(Sec)
'''def susp():
    alinhamento = 0 # face inf. da 2º esta acima da face inf. da 1º
    if alinhamento == 0:
        Asusp = (Sec['Vsd']/Sec['fyd'])*(ha/hapoio)
    elif alinhamento == 1: # face inf. da 2º esta abaixo da face inf. da 1º
        Asusp = (Sec['Vsd']/Sec['fyd'])'''
