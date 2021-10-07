import math
import mathLib

#MATHEMATIK

#Analysis
def getNormalform():
    print("1 - Normalform_zu_Mitternachtsform")
   # print("a * (x + d)2 + e --> ax2 + bx + c")

    a = float(input("Enter parameter a:"))
    d = float(input("Enter parameter d: "))
    e = float(input(("Enter parameter e:")))

    b = float(2 * a * d)
    c = float(a * pow(d, 2) + e)

    print(str(a)+"x2 + "+str(b)+"x + "+str(c))
    Analysis_getFunc()
def getScheitelform():
    print("2 - Mitternachtsform_zu_Normalform")
   # print("ax2 + bx + c --> a * (x +d)2 + e")
    a = float(input("Enter parameter a: "))
    b = float(input("Enter parameter b: "))
    c = float(input("Enter parameter c: "))

    d = float(b / (a * 2))
    e = float(c - (a * pow(d, 2)))
    print(str(a)+" * (x + "+str(d)+")2 + "+str(e))
    x = float(-1 * d)
    print("Scheitelpunkt: x = " + str(x) + ", y = " + str(e))
    Analysis_getFunc()
def getSchnittpunkte_XAchse():
    print("3 - Schnittpunkte X-Achse / Mitternachtsformel")
    # print("x1|2 = (-b +- Wurzel(b2 - 4ac)) / 2a")
    a = float(input("Enter parameter a: "))
    b = float(input("Enter parameter b: "))
    c = float(input("Enter parameter c: "))

    n = float(pow(b, 2) - (4 * a * c))
    if n > 0:
      w = float(math.sqrt(n))
      x1 = float(((-1 * b) + w) / (2*a))
      x2 = float(((-1 * b) - w) / (2 * a))
      print("x1 = "+str(x1)+", x2 = "+str(x2))

    elif n == 0:
        w = float(math.sqrt(n))
        x1 = float(((-1 * b) + w) / (2 * a))
        print("x1 = " + str(x1))

    elif n < 0:
        print("keine Schnittpunkte mit der X-Achse")

    Analysis_getFunc()
def getScheitelformWith3Points():
    #y = ax2 + bx + c
    print("5 - Normalform einer Parabel mit 3 Punkten bestimmen")
    point1 = input("Enter first point (x,y): ").split(",")
    point2 = input("Enter second point (x,y): ").split(",")
    point3 = input("Enter third point (x,y): ").split(",")

    y_C0 = float(float(point1[1]) - float(point2[1]))
    a_C0 = float(pow(float(point1[0]), 2) - pow(float(point2[0]), 2))
    b_C0 = float(float(point1[0]) - float(point2[0]))

    y_C1 = float(float(point2[1]) - float(point3[1]))
    a_C1 = float(pow(float(point2[0]), 2) - pow(float(point3[0]), 2))
    b_C1 = float(float(point2[0]) - float(point3[0]))

    # parameter .._C0  * b_C1   |     parameter ..C1 * b_C0
    #gleichsetzen von b um b weg zu kürzen
    y_B0 = y_C0 * b_C1
    a_B0 = a_C0 * b_C1
    b_B0 = b_C0 * b_C1

    y_B1 = y_C1 * b_C0
    a_B1 = a_C1 * b_C0
    b_B1 = b_C1 * b_C0

    y_B2 = float(y_B0 - y_B1)
    a_B2 = float(a_B0 - a_B1)
    b_B2 = float(b_B0 - b_B1) # sollte jetzt null sein

    a = float(y_B2 / a_B2)
    b = float((y_B1 - (a_B1 * a)) / b_B1)
    c = float(float(point1[1]) - (pow(float(point1[0]), 2) * a + float(point1[0]) * b))
    print("y = "+str(a)+"x2 + "+str(b)+"x + "+str(c))
    Analysis_getFunc()

def getWerteTabelleParabel():
   # xvalues = input("Enter x-values to calculate: ")
    xvalues = input("Enter x values to calculate, seperated by a comma: ").split(",")
    a = float(input("Enter parameter a: "))
    n = float(input("Enter exponent n: "))
    b = float(input("Enter parameter b: "))
    c = float(input("Enter parameter c: "))
    count = 1
    for x in xvalues:
        x = float(x)
        y = a * pow(x,n) + b * x + c
        print("y"+str(count)+" = "+str(y))
        count += 1
    Analysis_getFunc()
#Rechtwinkliges Dreieck

#Geometrie

def A_pi_r2():
    #A = pi * r2
    r = input("Enter parameter radius (r <einheit>): ")
    if r == "ges.":
        A1 = input("Enter parameter Flächeninhalt ( A <einheit>): ")
        A1 = A1.split()
        A = float(A1[0])
        rres = float(math.sqrt(A / math.pi))
        einheit = str(A1[1])
        einheit = einheit.replace("2","")
        print("Radius = "+str(rres)+" "+einheit)
    else:
        r1 = r.split()
        r2 = float(r1[0])
        Ares = float(math.pi * pow(r2, 2))
        print("Flächeninhalt = "+str(Ares)+" "+r1[1]+"2")
    RechtwinkligesDreieck_getFunc()
#PHYSIK

#Umrechen
def v1():
    #print("m/s -> km/h")
    print("number km/h   OR  number m/s")

    entered = input("Enter velocity in km/h or m/s: ").split()
    v = float(entered[0])
    if entered[1] == "m/s":
          v = float(v * 3.6)
          print(str(v)+" km/h")
    else:
        v = float(v / 3.6)
        print(str(v) + " m/s")
    getBereichP()

#Mechanik
def F_ma():
    #F = m * a
    print("1 - Kraft (Masse, Beschleunigung)")
    F = input("Enter parameter F(N): ")
    if F == "ges.":
     m = float(input("Enter parameter m(kg): "))
     a = float(input("Enter parameter a(m/s2): "))
     Fres = float(m * a)
     print("F = "+str(Fres)+"N")
    else:
        F = float(F)
        m = input("Enter parameter m(kg): ")
        if m == "ges.":
            a = float(input("Enter parameter a(m/s2): "))
            mres = float(F / a)
            print("m = "+str(mres)+"kg")
        else:
            m = float(m)
            ares = float(F / m)
            print("a = "+str(ares)+"m/s2")
    Mechanik_getFunc()
def v_st():
    #v = s / t
    print("2 - Geschwindigkeit, strecke, zeit")
    v = input("Enter parameter v(m/s): ")
    if v == "ges.":     #v gesucht
     s = float(input("Enter parameter s(m): "))
     t = float(input("Enter parameter t(s): "))
     vres = float(s / t)
     vres2 = float(vres * 3.6)
     print("v = "+str(vres)+"m/s")
     print("v = " + str(vres2) + "km/h")
    else:
        v = float(v)
        s = input("Enter parameter s(m): ")
        if s == "ges.":    #s gesucht
            t = float(input("Enter parameter t(s): "))
            sres = float(v * t)
            print("m = "+str(sres)+"m")
        else:               #t gesucht
            s = float(s)
            tres = float(s / v)
            print("t = "+str(tres)+"s")
    Mechanik_getFunc()




def Analysis_getFunc():

    print("Functions: ")
    print("1 - Scheitelform_zu_Normalform")
    print("2 - Normalform_zu_Scheitelform")
    print("3 - Schnittpunkte X-Achse / Mitternachtsformel")
    print("4 - Wertetabelle")
    print("5 - Normalform einer Parabel mit 3 Punkten bestimmen")

    entered = input("Function: ")

    if entered == "back":
        getBereichM()

    elif entered == "1":
        getNormalform()

    elif entered == "2":
        getScheitelform()

    elif entered == "3":
        getSchnittpunkte_XAchse()

    elif entered == "4":
        getWerteTabelleParabel()

    elif entered == "5":
        getScheitelformWith3Points()

    else:
        print("Function does not exist")
        Analysis_getFunc()
def RechtwinkligesDreieck_getFunc():
    print("Functions: ")
    print("1 - Satz des Pythagoras")
    print("2 - A = pi * r2")

    entered = input("Function: ")

    if entered == "back":
        getBereichM()

    elif entered == "1":
        getNormalform()
    elif entered == "2":
        A_pi_r2()

    else:
        print("Function does not exist")
        RechtwinkligesDreieck_getFunc()

def Mechanik_getFunc():

    print("Functions: ")
    print("1 - Kraft (Masse, Beschleunigung)")
    print("2 - Geschwindigkeit, strecke, zeit")

    entered = input("Function: ")

    if entered == "back":
        getBereichP()

    elif entered == "1":
        F_ma()

    elif entered == "2":
        v_st()

    else:
        print("Function does not exist")
        Mechanik_getFunc()

def getBereichM():
    print("Bereiche:")
    print("1 - Analysis")
    print("2 - Geometrie")

    entered = input("Bereich: ")

    if entered == "back":
        getSubject()

    elif entered == "1":
        Analysis_getFunc()
    elif entered == "2":
        RechtwinkligesDreieck_getFunc()

    else:
        print("Bereich does not exist")
        getBereichM()

def getUmrechnungen():
    print("1 - m/s  km/h")


    entered = input("Umrechnung: ")

    if entered == "back":
        getBereichP()

    elif entered == "1":
        v1()

    else:
        getUmrechnungen()
def getBereichP():
    print("Bereiche:")
    print("1 - Mechanik")
    print("2 - Umrechnen")

    entered = input("Bereich: ")

    if entered == "back":
        getSubject()

    elif entered == "1":
        Mechanik_getFunc()

    elif entered == "2":
        getUmrechnungen()

    else:
        print("Bereich does not exist")
        getBereichP()

def getSubject():
    print("Fächer:")
    print("1 - Mathematik")
    print("2 - Physik")
    print("3 - Chemie")

    entered = input("Bereich: ")

    if entered == "1":
        getBereichM()

    elif entered == "2":
        getBereichP()

    else:
        print("Bereich does not exist")
        getSubject()


getSubject()
#print(mathLib.getWkt_kumulierteWkt(0.4,8,20,max_k=False,less_k=False,min_k=True,more_k=False,array=False) - mathLib.getWkt_kumulierteWkt(0.4,12,20,max_k=False,less_k=False,min_k=True,more_k=False,array=False))





