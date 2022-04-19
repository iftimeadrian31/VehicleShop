import numpy as np
import matplotlib.pyplot as plt

with open('MI_BCIdataset.dat') as f:
    nr_canale=next(f)
    nr_esantioane_per_canal=next(f)
    nr_trialuri=next(f)
    irelevant=next(f)
    frecventa_esantionare=next(f)
    nume_atribut1=next(f)
    string_apartenenta_atribut1=next(f)
    lista_apartenenta_atribut1=list(map(int,string_apartenenta_atribut1.split("  ")))
    nume_atribut2=next(f)
    string_apartenenta_atribut2=next(f)
    lista_apartenenta_atribut2=list(map(int,string_apartenenta_atribut2.split("  ")))
coloane = np.loadtxt('MI_BCIdataset.dat', unpack = True,skiprows=9)
obiecte_esantioane=[]




