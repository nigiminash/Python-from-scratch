def jägerzaun_entschlüsseln(t, c):
    i = 0
    e = 0
    s = 1
    v = []

    # Liste an Listen erstellen
    while (i < c):
        v.append([])
        i = i + 1

    # Werte zurücksetzen
    i = 0

    # Buchstaben in Linien sortieren
    while (i < len(t)):
        v[e].append(t[i])
        e = e + s
        if (e == 0):
            s = 1
        if (e == c - 1):
           s = -1
        i = i + 1

     # Werte zurücksetzen   
    i = 0
    u = 0
    while (i < len(v)):
        k = v[i]
        m = ""
        e = 0
        while (e < len(k)):
            m = m + t[u]
            u = u + 1
            e = e + 1
        v[i] = [m]
        i = i + 1
        
    i = 0
    #Liste erstellen, nach der abgelesen wird welcher
    #Buchstabe in die Liste eingesetzt wird
    f = []
    while (i < c):
        f.append([0])
        i = i + 1

    #Werte zurücksetzen
    i = 0
    d = 0
    q = 0
    k = []
    g = []
    e = 0
    s = 1
    aaa = ""
    
    while (i < len(t)):
    #Liste wählen, aus der der Buchstabe entnommen wird
        k = v[e]
        kk = k [0]

    #Zahl auswählen, die aus f genommen wird
        b = f[e]
        h = b[0]

    #f jeden Zug verändern
        f_zähler = f[e]
        f_zähler[0] = f_zähler[0] + 1
        f[e] = f_zähler
        
    #Leseraster für f erstellen
        e = e + s
        if (e == 0):
            s = 1
        if (e == c - 1):
           s = -1
           
    #den schlussendlichen Buchstaben an definierter Stelle in die Endliste einsetzen
        a = kk[h]
        aa = a[0]
        aaa = aaa + aa

    #nächsten Buchstaben wählen
        i = i + 1

        
    print (aaa)



while (0 == 0):
    x = input("Ihr verschlüsselter Text:  ")
    y = int(input("Der dazugehörige Code:  "))
    jägerzaun_entschlüsseln(x, y)
    print ("------------------------------------------------------------------------------------------------")
