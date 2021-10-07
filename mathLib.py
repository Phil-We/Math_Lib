import math

#Analysis

def getNormalform(a: float, d: float, e: float):
    print("1 - Normalform_zu_Mitternachtsform")
    b = float(2 * a * d)
    c = float(a * pow(d, 2) + e)
    print(str(a)+"x2 + "+str(b)+"x + "+str(c))
def getScheitelform(a: float, b: float, c: float):
    print("2 - Mitternachtsform_zu_Normalform")
    d = float(b / (a * 2))
    e = float(c - (a * pow(d, 2)))
    print(str(a)+" * (x + "+str(d)+")2 + "+str(e))
    x = float(-1 * d)
    return str("Scheitelpunkt: x = " + str(x) + ", y = " + str(e))
def getSchnittpunkte_XAchse(a: float, b: float, c: float):
    print("3 - Schnittpunkte X-Achse / Mitternachtsformel")
    # print("x1|2 = (-b +- Wurzel(b2 - 4ac)) / 2a")
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
def getNormalformWith3Points(point1:[float],point2:[float],point3:[float]):
    #y = ax2 + bx + c
    print("5 - Normalform einer Parabel mit 3 Punkten bestimmen")

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
def getWerteTabelleParabel(xvalues:[float],a:float,n:float,b:float,c:float):
    count = 1
    for x in xvalues:
        x = float(x)
        y = a * pow(x,n) + b * x + c
        print("y"+str(count)+" = "+str(y))
        count += 1


#Basics
def fac(n:float):
    r = n
    while n > 1:
        n -= 1
        r *= n
    return r



#Geometrie


#Stochastik
def getBinomialkoeffizient(n:float,k:float):
    #n! / (k! * (n-k)!)
    if (k != 0) and (n != k):
      b = float(fac(n) / (fac(k) * fac(n-k)))
      return b
    else:
        return 1
def getWkt_FormelVonBernoulli(p: float,k: float, n:float):
    if k <= n:
        q = float(1 - p)
        k2 = float(n - k)
        wkt = getBinomialkoeffizient(n,k) * pow(p,k) * pow(q,k2)
        return wkt
    else:
        return 0
def getWkt_kumulierteWkt(p: float,k: float, n:float,operator:str="<=",array: bool=False):
    p_1:float = 0
    p_2 = [float]
    if operator == "<=":
        while k >= 0:
            value = getWkt_FormelVonBernoulli(p, k, n)
            p_1 += value
            p_2.append(value)
            k -= 1
    elif operator == "<":
        k -= 1
        while k >= 0:
            value = getWkt_FormelVonBernoulli(p, k, n)
            p_1 += value
            p_2.append(value)
            k -= 1
    elif operator == ">=":
        while k <= n:
            value = getWkt_FormelVonBernoulli(p, k, n)
            p_1 += value
            p_2.append(value)
            k += 1
    elif operator == ">":
        k += 1
        while k <= n:
            value = getWkt_FormelVonBernoulli(p, k, n)
            p_1 += value
            p_2.append(value)
            k += 1


    if array == False:
        print('{0:.10f}'.format(p_1))
        return p_1
    else:
        return p_2
def getWkt_kumulierteWkt2(p: float,k_one: float,k_two: float, n:float):
    p_res: float = 0
    #P(4<X<8)
    while k_one <= k_two:
        value = getWkt_FormelVonBernoulli(p, k_one, n)
        p_res += value
        k_one += 1

    print('{0:.10f}'.format(p_res))
def getErwartungswert(n:float,p:float):
    my = float(n * p)
    return my
def getStandardabweichung(n: float, p:float):
    q = float(1 - p)
    sigma = math.sqrt(n * p * q)
    return sigma


# X <= k ; X < k; X >= k; X > k
# mindestens l, höchstens k => (X <= l) - (X <= k)
# mehr als l, weniger als k => (X < l) - (X < k)

#print(getWkt_FormelVonBernoulli(p=float(1/7),k=2,n=20))
#getWkt_kumulierteWkt(p=float(1/7),k=5,n=20,operator=">=",array=False)
#getWkt_kumulierteWkt2(p=0.3,k_one=3,k_two=8,n=20)
print(getSchnittpunkte_XAchse(a=-1,b=-6,c=5))