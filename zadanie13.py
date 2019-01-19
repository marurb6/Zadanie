import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import aseegg as ag


t = np.linspace (0, 37.97, 200*37.97)
prob=200
dane = pd.read_csv(r"sub1trial20.csv", delimiter=',', engine='python')
sygnal=dane["kol1"]
sygnal1=dane["kol5"]

przefiltrowany = ag.pasmowozaporowy(sygnal, prob, 49, 51)
przefiltrowany = ag.pasmowoprzepustowy(przefiltrowany, prob, 1, 50)

plt.subplot(2,2,1)
plt.title("Sygnał")
plt.ylabel('Amplituda [µV]')
plt.xlabel('Czas [s]')
plt.plot(t, sygnal)

plt.subplot(2,2,3)
plt.title("Cyfry wyświetlane na ekranie")
plt.ylabel('Wyświetlana cyfra')
plt.xlabel('Czas [s]')
plt.plot(t, sygnal1)

plt.subplot(2,2,2)
plt.title("Przefiltrowany sygnał")
plt.ylabel('Amplituda [µV]')
plt.xlabel('Czas [s]')
plt.plot(t, przefiltrowany)

plt.subplot(2,2,4)
plt.title("Cyfry wyświetlane na ekranie")
plt.ylabel('Wyświetlana cyfra')
plt.xlabel('Czas [s]')
plt.plot(t, sygnal1)

plt.show()

kod=[]
p = 0
n = 0
for i in range(0, len(przefiltrowany)):
    n+=1 # licznik sprawdzający, czy jet prerwa między powtarzającymi się cyframi
    if przefiltrowany[i] > 0.05:
        l = int(dane.iloc[i]['kol5'])
        if p != l: #sprawdza, czy cyfra jest różna od poprzedniej zakodowanej
            kod.append(l) #dodaje cyfrę do listy odkodowanych
            p = l
        elif n > 10:
            kod.append(l) #dodaje powtórzoną cyfrę po przerwie > 10 sygnałów
        n = 0 #zeruje licznik przy amplitudzie > 1
print (kod)
