import math

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