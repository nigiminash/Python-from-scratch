def veginere_entschlüsseln(vt, s):
    alph = "abcdefghijklmnopqrstuvwxyz"
    et = ""
    i = 0
    v = []
    v2 = []
#Schlüssel in Zahlen ausschreiben
    while (i < len(s)):
        e = 0
        while (e < len(alph)):
            if (alph[e] == s[i]):
                v.append(e)
            e = e + 1
        
        i = i + 1
    print (v)

#Verschlüsselten Text in Zahlen übersetzen
    i = 0
    while (i < len(vt)):
        e = 0
        while (e < len(alph)):
            if (alph[e] == vt[i]):
                v2.append(e)
            e = e + 1
        
        i = i + 1
    print (v2)
        
#Text vom Schlüssel ableiten
    i = 0
    e = 0
    while (i < len(v2)):
        j = v2[i]
        k = v[e]
        if (k > j):
            j = j + 26
        m = j - k

        u = 0
        while (u < len(alph)):
            if (u == m):
                p = alph[u]
            u = u + 1
        et = et + p


        i = i + 1
        e = e + 1
        if (e == len(v)):
            e = 0


    


    print("Ihr entschlüsselter Text:   ", et)






while (0 == 0):
    x = input("Geben Sie hier den verschlüsselten Text ein:  ")
    y = input("Geben Sie hier den möglichen Schlüssel für den Text ein:  ")
    veginere_entschlüsseln(x, y)
    print:"___________________________________________________________________"
