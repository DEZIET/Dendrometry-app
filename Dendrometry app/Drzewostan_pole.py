from math import pi, sqrt 

def srednia_ar_D (ni,di):
    
    # mnożenie ni*di 
    sumadini = sum([i*j for i, j in zip(di, ni)])
    #
    sumni = sum(ni)
    D = sumadini/sumni
    return D

def piersnicowe_pole_przekroju(ni,di,pow):
    
    # pierśnicowe pole przekroju dla di
    gi =[]
    
    for i in range(len(di)):
        arg = (pi * di[0+i]**2)/40000
        gi.append(arg)
    #
    
    G = sum([i*j for i, j in zip(gi, ni)])
    G_ha = G/pow
    return [G , G_ha]
    
def przecietne_pole_przekroju(ni,di):
    
    G = piersnicowe_pole_przekroju(ni,di,1)[0]
    N = sum(ni)
    sr_g = G/N
    return sr_g

def przecietna_piersnica_przekrojowa(ni,di):
    
    sr_g = przecietne_pole_przekroju(ni,di)
    dg = sqrt((40000/pi*sr_g))
    return dg 


def odchylenie_stadardowe_piersnic(ni,di):
 
    sumanidi = sum([i*j for i, j in zip(ni, di)])
    # Potęge di tworzy wyrażennie === i*j**2
    sumanidi_dido2 = sum([i*j**2 for i, j in zip(ni, di)])
    #
    N= sum(ni)    
    odchyl = sqrt((sumanidi_dido2-((sumanidi**2)/N))/N)
    
    return odchyl 

def wspolczynnik_zmiennowci(ni,di):
    Wd = (odchylenie_stadardowe_piersnic(ni,di)/srednia_ar_D(ni,di)) * 100
    Wg = 2 * Wd
    return [ Wd , Wg ]


def liczebność_losowe_proby(ni,di):
    Wd = wspolczynnik_zmiennowci(ni,di)[0]
    Wg = wspolczynnik_zmiennowci(ni,di)[1]
    
    nd = (Wd/5)**2
    ng = (Wg/5)**2
    return [ nd , ng ]


if __name__ == '__main__': 
    ni = [2,20,23,50,77]
    di = [12,14,16,18,20]
    pow = 1.20
    print(srednia_ar_D(ni,di))
    print(piersnicowe_pole_przekroju(ni,di,pow))
    print(przecietne_pole_przekroju(ni,di))
    print(przecietna_piersnica_przekrojowa(ni,di))
    print(odchylenie_stadardowe_piersnic(ni,di))
    print(wspolczynnik_zmiennowci(ni,di))
    print(liczebność_losowe_proby(ni,di))


