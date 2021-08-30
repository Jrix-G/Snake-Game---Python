tab = [[10, 15], [0, 2], [10, 15], [10, 15],[0, 2],[0, 3]]

for i in range(len(tab)):
    m = 0
    for n in range(len(tab)):
        if tab[i] == tab[n]:
            m += 1
            if m == 2:
                print(tab[n])