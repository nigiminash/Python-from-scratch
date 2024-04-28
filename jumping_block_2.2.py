import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
root.title('Jumpy Block')
root.geometry('1000x700')
runer = 0

class Block(tk.Label):
    def __init__(self, master, x, y):
        tk.Label.__init__(self, master)
        self.configure(bg = 'red', width = 10, height = 5, text = "°>°", anchor = CENTER)
        self.configure(font = 'Helvetica 15 bold')
        self.a = x
        self.b = y
        self.place(x = self.a, y = self.b)
        self.Leben = 4
        self.d = 0
        self.xH = 0
        self.gravity = 0
        self.aaa = True
        self.punkte = 0
        self.speed = 3
        

    def Sprung(self, event):
        if (event.keysym == "space" and self.aaa == True):
            root.after(0, self.Sprung2)
            self.aaa = False


    def Sprung2(self, event = None):
        try:
            self.place(x = self.a, y = self.b - self.xH)
            self.xH += self.speed
            if (self.xH % 10 == 0):
                self.gravity += 1
            if (self.xH > 250):
                 self.d = 1
            if (self.xH < 250):
                self.d = 0
            if (self.d == 0):
                root.after(self.gravity, self.Sprung2)
            if (self.d == 1):
                self.gravity += 1
                root.after(2, self.Landung)
        except:
            pass 
    def Landung(self, event = None):
        self.place(x = self.a, y = self.b - self.xH)
        self.xH -= self.speed
        if (self.xH % 10 == 0):
            self.gravity -= 1
        if (self.xH > 0):
            root.after(self.gravity, self.Landung)
        if (self.xH == 0):
            self.d = 0
            self.gravity = 0
            self.aaa = True

        
class Kreis(tk.Label):
    def __init__(self, master, x, y):
        tk.Label.__init__(self, master)
        self.a = x
        self.b = y
        self.place(x = self.a, y = self.b)
        self.configure(width = 6, height = 3, bg = 'blue')
        self.xL = 0
        self.r = True
        self.speed = 3
        root.after(0, self.rollen)
        

    def rollen(self, event = None,):
        try:
            global Spieler1
            global HP
            global PS
            global Menü
            global runer
            if (Menü.x == 1):
                self.place(x = self.a - self.xL, y = self.b)
                self.xL += self.speed
            if (Spieler1.Leben == 0 and runer == 0):
                Game_over()
            if (self.xL in range (10, 20)):
                self.r = True
            if (Overlap(Spieler1, self, 100, 50) == True and self.r == True):
                Spieler1.Leben -= 1
                runer = 0
                HP.configure(text = "Leben: " + str(Spieler1.Leben))
                self.r = False
            if (self.xL < self.a):
                root.after(3, self.rollen)
            else:
                self.a = 1000
                self.b = random.randint(400, 550)
                self.xL = 0
                root.after(0, self.rollen)
                Spieler1.punkte += 1
                PS.configure(text = "Punkte: " + str(Spieler1.punkte))
        except:
            pass

def Overlap(a, b, Rangex, Rangey):
    corax = a.winfo_x()
    coray = a.winfo_y()
    corbx = b.winfo_x()
    corby = b.winfo_y()
    if (corbx in range(corax - Rangex, corax + Rangex) and corby in range (coray - Rangey, coray + Rangey)):
        return True
            

def Game_over():
    Retry = retry(root)
    


def klonen(time):
    Kreis2 = Kreis(root, 1000, random.randint(500, 700))
    root.after(time, klonen(1000))



class Start(tk.Frame):
    def __init__(self, master):
        self.x = 0
        self.f = 0
        tk.Frame.__init__(self, master)
        self.configure(bg = 'cyan', width=1000, height=700)
        self.Klist = []

        
        def Spielstart(event):
            self.x = 1
            self.destroy()
        def schw1(event):
            global Kreis1
            global Spieler1
            global HP
            Spieler1.speed = 2
            Spieler1.Leben = 6
            Kreis1.speed = 1
            HP.configure(text = "Leben: " + str(Spieler1.Leben))
            if (self.f == 1):
                global Kreis2
                self.f = 0
                try:
                    self.Klist(0).destroy()
                except:
                    pass
        def schw2(event):
            global Kreis1
            global Spieler1
            global HP
            Spieler1.Leben = 3
            Spieler1.speed = 3
            Kreis1.speed = 4
            HP.configure(text = "Leben: " + str(Spieler1.Leben))
            if (self.f == 1):
                global Kreis2
                self.f = 0
                try:
                    Kreis.destroy()
                except:
                    pass
        def K2():
            Kreis2 = Kreis(root, 1000, 500)
            Kreis2.speed = 4
            Kreis2.xL = -500
            self.Klist.append(Kreis2)
            print(self.Klist)
        def schw3(event):
            if (self.f == 0):
                global Kreis1
                global Spieler1
                global HP
                Spieler1.speed = 6
                Kreis1.speed = 4
                Spieler1.Leben = 2
                HP.configure(text = "Leben: " + str(Spieler1.Leben))
                self.f = 1
                root.after(0, K2)
            
        self.pack(anchor = CENTER)
        self.B1 = tk.Button(self, text = 'Start', font ='Helvetica 15 bold', height= 10, width=20)
        self.B1.bind("<Button-1>", Spielstart)
        self.B1.place(x = 450, y = 200)
        self.B2 = tk.Button(self, text = 'Easy', height= 2, width=8, bg = 'green')
        self.B2.bind("<Button-1>", schw1)
        self.B2.place(x = 250, y = 500)
        self.B3 = tk.Button(self, text = 'Normal', height= 2, width=8, bg = 'yellow')
        self.B3.bind("<Button-1>", schw2)
        self.B3.place(x = 500, y = 500)
        self.B4 = tk.Button(self, text = 'Hard', height= 2, width=8, bg = 'red')
        self.B4.bind("<Button-1>", schw3)
        self.B4.place(x = 750, y = 500)


class retry(tk.Frame):
    def __init__(self, master):

        def r():
            global runer
            runer = 1
        
        def restart(event):
            Menü = Start(root)
            r()
            
            Spieler1.a = 50
            Spieler1.b = 550
            Spieler1.place(x = Spieler1.a, y = Spieler1.b)
            Spieler1.Leben = 4
            Spieler1.d = 0
            Spieler1.xH = 0
            Spieler1.gravity = 0
            Spieler1.aaa = True
            Spieler1.punkte = 0
            Spieler1.speed = 3

            Kreis1.a = 1000
            Kreis1.b = 580
            Kreis1.place(x = Kreis1.a, y = Kreis1.b)
            Kreis1.configure(width = 6, height = 3, bg = 'blue')
            Kreis1.xL = 0
            Kreis1.r = True
            Kreis1.speed = 3

            self.destroy()

            

            

            HP = tk.Label(text = "Leben:  " + str(Spieler1.Leben), font = 'Helvetica 15 bold')
            HP.place(x = 300, y = 30)
            PS = tk.Label(text = "Punkte:  " + str(Spieler1.punkte), font = 'Helvetica 15 bold')
            PS.place(x = 700, y = 30)


        tk.Frame.__init__(self, master)
        self.dthmsg = tk.Label(self, text = 'GAME OVER', bg = 'white', font ='Helvetica 30 bold')
        self.dthmsg.place(x = 400, y = 50)
        self.configure(bg = 'black', width=1000, height=700)
        self.BR = tk.Button(self, text = 'restart', font ='Helvetica 15 bold', height= 10, width=20)
        self.BR.bind("<Button-1>", restart)
        self.BR.place(x = 400, y = 200)
        self.pack(anchor = CENTER)
       



Menü = Start(root)
Spieler1 = Block(root, 50, 550)
Kreis1 = Kreis(root, 1000, 580)

HP = tk.Label(text = "Leben:  " + str(Spieler1.Leben), font = 'Helvetica 15 bold')
HP.place(x = 300, y = 30)
PS = tk.Label(text = "Punkte:  " + str(Spieler1.punkte), font = 'Helvetica 15 bold')
PS.place(x = 700, y = 30)



root.bind("<KeyPress>", Spieler1.Sprung)





root.mainloop()
