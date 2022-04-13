import numpy as np
import matplotlib.pyplot as plt

with open('IOC-L08-ep8chTargets.dat') as f:
    nr_canale1=next(f)
    nr_esantioane_per_trial1=next(f)
    nr_trialuri1=next(f)
    irelevant1=next(f)
    frecventa_esantionare1=next(f)
coloane1 = np.loadtxt('IOC-L08-ep8chTargets.dat', unpack = True,skiprows=5)
obiecte_esantioane1=[]

triale=[]
for index_trial in range(int(nr_trialuri1)):
    trial=[]
    for index_canale in range(int(nr_canale1)):
        for index_esantion in range(int(nr_esantioane_per_trial1)):
                trial.append(coloane1[index_esantion][index_trial*8+index_canale])
    triale.append(trial)
triale_organizate1=[]
for trial in triale:
    canale=[]
    for index_canal in range(int(nr_canale1)):
        esantioane=[]
        for index_esantion in range(int(nr_esantioane_per_trial1)):
            esantioane.append(trial[index_canal*180+index_esantion])
        canale.append(esantioane)
    triale_organizate1.append(canale)    

with open('IOC-L08-ep8chNONTargets.dat') as f:
    nr_canale2=next(f)
    nr_esantioane_per_trial2=next(f)
    nr_trialuri2=next(f)
    irelevant2=next(f)
    frecventa_esantionare2=next(f)
coloane2 = np.loadtxt('IOC-L08-ep8chNONTargets.dat', unpack = True,skiprows=5)

triale2=[]
for index_trial in range(int(nr_trialuri2)):
    trial=[]
    for index_canale in range(int(nr_canale2)):
        for index_esantion in range(int(nr_esantioane_per_trial2)):
                trial.append(coloane2[index_esantion][index_trial*8+index_canale])
    triale2.append(trial)
triale_organizate2=[]

for trial in triale2:
    canale=[]
    for index_canal in range(int(nr_canale2)):
        esantioane=[]
        for index_esantion in range(int(nr_esantioane_per_trial2)):
            esantioane.append(trial[index_canal*180+index_esantion])
        canale.append(esantioane)
    triale_organizate2.append(canale) 

medii_trials1=[]
for index_esantion in range(int(nr_esantioane_per_trial1)):
    medii_canal1=[]
    for index_canal in range(int(nr_canale1)):
        media1=0
        for index_trial in range(int(nr_trialuri1)):
            media1+=triale_organizate1[index_trial][index_canal][index_esantion]
        media1=media1/int(nr_trialuri1)
        medii_canal1.append(media1)
    medii_trials1.append(medii_canal1)

trial_mediu1=[]
for index_canal in range(int(nr_canale1)):
    medii_canal1=[]
    for index_esantion in range(int(nr_esantioane_per_trial1)):
        medii_canal1.append(medii_trials1[index_esantion][index_canal])
    trial_mediu1.append(medii_canal1)
    

medii_trials2=[]
for index_esantion in range(int(nr_esantioane_per_trial2)):
    medii_canal2=[]
    for index_canal in range(int(nr_canale2)):
        media2=0
        for index_trial in range(int(nr_trialuri2)):
            media2+=triale_organizate2[index_trial][index_canal][index_esantion]
        media2=media2/int(nr_trialuri2)
        medii_canal2.append(media2)
    medii_trials2.append(medii_canal2)
    
    



trial_mediu2=[]
for index_canal in range(int(nr_canale2)):
    medii_canal2=[]
    for index_esantion in range(int(nr_esantioane_per_trial2)):
        medii_canal2.append(medii_trials2[index_esantion][index_canal])
    trial_mediu2.append(medii_canal2)
    

lista_y=[]
for index_esantion in range(int(nr_esantioane_per_trial1)):
    lista_y.append(index_esantion/int(frecventa_esantionare1))


for index_canal in range(int(nr_canale1)):
    plt.subplot(3,3,index_canal+1)
    plt.plot(lista_y,trial_mediu1[index_canal])
    plt.plot(lista_y,trial_mediu2[index_canal])
    plt.xlim([0,0.7])
    plt.ylim([-10,10])
    x_ticks=[0.1,0.2,0.3,0.4,0.5,0.6,0.7]
    y_ticks=[-5,0,5]
    x_labels=[0.1,0.2,0.3,0.4,0.5,0.6,0.7]
    y_labels=[-5,0,5]
    plt.xticks(ticks=x_ticks,labels=x_labels)
    plt.yticks(ticks=y_ticks,labels=y_labels)
plt.show()


medii_trials_baseline_1=[]
for index_esantion in range(int(26)):
    medii_canal1=[]
    for index_canal in range(int(nr_canale1)):
        media1=0
        for index_trial in range(int(nr_trialuri1)):
            media1+=triale_organizate1[index_trial][index_canal][index_esantion]
        media1=media1/int(nr_trialuri1)
        medii_canal1.append(media1)
    medii_trials_baseline_1.append(medii_canal1)

trial_baseline_1=[]
for index_canal in range(int(nr_canale1)):
    medii_canal1=[]
    for index_esantion in range(int(26)):
        medii_canal1.append(medii_trials_baseline_1[index_esantion][index_canal])
    trial_baseline_1.append(medii_canal1)

medii_trials_baseline_2=[]
for index_esantion in range(int(26)):
    medii_canal2=[]
    for index_canal in range(int(nr_canale2)):
        media2=0
        for index_trial in range(int(nr_trialuri2)):
            media2+=triale_organizate2[index_trial][index_canal][index_esantion]
        media2=media2/int(nr_trialuri2)
        medii_canal2.append(media2)
    medii_trials_baseline_2.append(medii_canal2)

trial_baseline_2=[]
for index_canal in range(int(nr_canale2)):
    medii_canal2=[]
    for index_esantion in range(int(26)):
        medii_canal2.append(medii_trials_baseline_2[index_esantion][index_canal])
    trial_baseline_2.append(medii_canal2)
