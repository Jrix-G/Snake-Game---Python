tab = [[10, 15], [0, 2], [10, 15], [0, 3]]

for i in range(len(tab)):
    info = tab[i-1]
    tab2 = tab.remove(tab[i])
    for n in range(len(tab)):
        if tab[n] == info:
            print(tab[n])