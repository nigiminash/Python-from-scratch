def veginere (text, code):
    alph = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    c = []
    while (i < len(text)):
        x = 0
        while (x != 26):
            if (alph[x] == text[i]):
                g = x
            x = x + 1
        c.append(g)
        i = i + 1

    ab = len(text)
    a = []
    while (ab != 0):
        a.append([])
        ab = ab - 1

    e = 0
    f = []
    while (e < len(code)):
        x = 0
        while (x != 26):
            if (alph[x] == code[e]):
                g = x
            x = x + 1
        f.append(g)
        e = e + 1

    ac = 0
    ad = 0
    while (ac < len(text)):
        a[ac] = (c[ac] + f[ad]) % 26
        ac = ac + 1
        ad = ad + 1
        if (ad == len(code)):
            ad = 0

    ae = ""
    af = 0
    while (af < len(a)):
        ah = a[af]
        ag = alph[ah]
        ae = ae + ag
        af = af + 1

    print("Geheimtext lautet: ", ae)

    
    

        

while (0 == 0):
    x = input("Ihr Text:  ")
    y = input("Ihr Code:  ")
    veginere (x, y)
    print("------------------------------------------------------------------------------------------")
