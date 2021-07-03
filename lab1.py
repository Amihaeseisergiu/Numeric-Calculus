import math
import random
import time

def prob1():
    u = 10
    m = 0
    while 1.0 + u ** (-m) != 1.0:
        m += 1
    
    return u ** (-(m-1))

print(prob1())

def prob2():
    a = 1.0
    u = prob1()
    b = u / 10
    c = u / 10
    
    if (a + b) + c == a + (b + c):
        print("Adunarea este asociativa")
    else:
        print("Adunarea nu este asociativa")

    def getMulNotAssoc():
        while True:
            a = random.random()
            b = random.random()
            c = random.random()

            if a*(b*c) != (a*b)*c:
                print(a); print(b); print(c)
                return a,b,c
    
    a,b,c = getMulNotAssoc()
    if (a * b) * c == a * (b * c):
        print("Inmultirea este asociativa")
    else:
        print("Inmultirea nu este asociativa")

prob2()

def my_tan(x, e):
    def inner_tan(x, e):
        f = 0
        mic = 10 ** (-12)
        if f == 0:
            f = mic
        C = f
        D = 0
        b = 1
        a = x
        
        D = b + a * D
        if D == 0: D = mic
        C = b + a / C
        if C == 0: C = mic
        D = 1 / D
        delta = C * D
        f = delta * f
        b += 2
        a = -(x * x)
        
        while abs(delta - 1) >= e:
            D = b + a * D
            if D == 0: D = mic
            C = b + a / C
            if C == 0: C = mic
            D = 1 / D
            delta = C * D
            f = delta * f
            b += 2
        return f
        
    if not (0 <= x < (1/2) * math.pi):
        if x < 0:
            return -inner_tan((-x) % math.pi, e)
        
        return inner_tan(x % math.pi, e)
    
    return inner_tan(x, e)

def my_tan2(x):
    def inner_tan(x):
        c1 = 0.33333333333333333
        c2 = 0.133333333333333333
        c3 = 0.053968253968254
        c4 = 0.0218694885361552
        x_2 = x * x
        x_3 = x_2 * x
        x_5 = x_3 * x_2
        x_7 = x_5 * x_2
        x_9 = x_7 * x_2
        
        return x + c1 * x_3 + c2 * x_5 + c3 * x_7 + c4 * x_9
    
    if (1/4) * math.pi <= x < (1/2) * math.pi:
        return 1 / inner_tan((1/2) * math.pi - x)
    elif -(1/2) * math.pi <= x < -(1/4) * math.pi:
        return - (1 / inner_tan((1/2) * math.pi + x))
    
    return inner_tan(x)
    
def prob3():
    error = 0
    totalTime = time.time()
    for i in range(0, 10000):
        x = random.uniform(-(math.pi / 2) + 10 ** (-10), math.pi / 2 - 10 ** (-10))
        mtan = my_tan(x, 10 ** (-10))
        error += abs(math.tan(x) - mtan)
    
    print("Eroarea medie functii continue %f"%(error / 10000))
    print("Timp total functii continue %f"%(time.time() - totalTime))
    
    error = 0
    totalTime = time.time()
    for i in range(0, 10000):
        x = random.uniform(-(math.pi / 2) + 10 ** (-10), math.pi / 2 - 10 ** (-10))
        mtan = my_tan2(x)
        error += abs(math.tan(x) - mtan)
    
    print("Eroarea medie polinoame %f"%(error / 10000))
    print("Timp total polinoame %f"%(time.time() - totalTime))
    