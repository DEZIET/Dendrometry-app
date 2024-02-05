from math import pi

def wysokosc_Lorey(ni,di,hi):

     # pierśnicowe pole przekroju dla di
    gi =[]
    
    for i in range(len(di)):
        arg = (pi * di[0+i]**2)/40000
        gi.append(arg)
    #
        
    sumanidihi = sum([i*j*k for i, j, k in zip(ni, gi, hi)])
    sumanigi = sum([i*j for i, j in zip(ni, gi)])
    Hl = sumanidihi/sumanigi
    return Hl 



if __name__ == '__main__':
    
    h = [22.2, 20.2, 21.5, 22.4, 20.2, 21, 24.8, 22.3, 23.1, 22.1, 23.5, 24.1, 22.5, 24.5, 21]
    d = [28.6, 26.7, 25.4, 26.6, 29.4, 29.5, 34.3, 30.9, 32.2, 29.9, 29.2, 33.3, 26.3, 38.7, 26.5]
    