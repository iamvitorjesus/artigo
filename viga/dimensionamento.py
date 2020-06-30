def dimensionar(Dic):
    while True:
        metodo = Dic['Modelo']
        if metodo == 1:
            from viga.cortante import cortanteM1
            Sec = cortanteM1(Dic)
            break
        elif metodo == 2:
            from viga.cortante import cortanteM2
            Sec = cortanteM2(Dic)
            break
        else:
            continue
    return (Sec)
