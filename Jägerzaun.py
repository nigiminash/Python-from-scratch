def jägerzaun(t, c):
    i = 0
    v = []
    e = 0
    s = 1
    p = 0
    d = ""
    while(i < c):
        v.append([])
        i = i + 1
    while(e < len(t)):
        v[p].append(t[e])
        p = p + s
        if (p == 0):
            s = 1
        if (p == c - 1):
           s = -1
        e = e + 1
    i = 0
    ende = ""
    kk = ""
    while (i < len(v)):
        k = v[i]
        j = 0
        
        while (j < len(k)):
            kk = kk + k[j]
            ende = ende + kk
            j = j + 1
            kk = ""
               
        i = i + 1
    print(ende)
    print("----------------------------------------------------------")






while (0 == 0):
    x = input("Ihr Text:  ")
    y = int(input("Ihr Schlüssel:  "))
    jägerzaun(x, y)
