# 4 podstawowe wzory dendrometryczne do drzewa leżącego
import math as m 

# Pole przekroju

def pole(d):

    g = (m.pi * d ** 2)/40000

    return g

# Hubera

def Huber(l,d): 
    
    g = (m.pi * d ** 2)/40000
    V = g * l

    return V 

# Hossfeld

def Hossfeld(l,d,dl,stan): 
    
    g = (m.pi * d ** 2)/40000
    
    if stan != 'strzała'  :
        gl = (m.pi * dl ** 2)/40000
    else:
        gl = 0

    V = ((3 * g + gl)/4) * l

    return V

# Smalian

def Smalian(l,d0,dl,stan): 
    
    g0 = (m.pi * d0 ** 2)/40000
    
    if stan != 'strzała' :
        gl = (m.pi * dl ** 2)/40000
    else:
        gl = 0

    V = ((g0 + gl)/2) * l

    return V

#Netwona

def Netwon(l,d0,d1_2,dl,stan): 
    
    g0 = (m.pi * d0 ** 2)/40000

    g1_2 = (m.pi * d1_2 ** 2)/40000
    
    if stan != 'strzała' :
        gl = (m.pi * dl ** 2)/40000
    else:
        gl = 0

    V = ((g0 + g1_2 + gl)/6) * l

    return V

#Francuski

def French(O1_2,l):

    O1_2 = O1_2/100

    V = (O1_2/5)**2 * 2*l
    
    return V




# Sekcyjny

def Sekcyjny(l_klody,l_sekcji,dn):
    
    gn = []

    for i in range(len(dn)):
        d = dn[0+i]
        g = (m.pi * d ** 2)/40000
        gn.append(g)
    
    g = sum(gn)
    
    la = len(gn) * l_sekcji - l_klody
    Va = la * (gn[-1]/2)
    V = l_sekcji * g * Va
    
    return V

def blad(V,Vrz):
    
    alfa = V -Vrz
    pw = (alfa/Vrz)*100
    return [alfa , pw]

def l_kszt(V,d,h):
    
    f= V/(((m.pi*d**2)/40000)*h)
    
    return f
 

if __name__ == '__main__':
    print(Huber(3,3))
    print(Smalian(3,3,3,3))
    print(Netwon(3,3,3,3,3))
    print(Hossfeld(3,33,3,4))
    print(Sekcyjny(3,3,[3,3,3]))
    print(blad(3,2))
    print(l_kszt(20,33,3))
    print(French(25,3))