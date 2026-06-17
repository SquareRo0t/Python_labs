# Villkor och rekursion
# Heltalsdivisoin och rest vid division (modulus) - Uttrycks med // och modulus-operation %
# == Equal operator (Uttryck som undersöker likhet), = Assignment operator (kommmando som tvingar fram likhet), % Modulo Operator
# x != y är true om x inte är lika y
# x > y är True om x är större än y
# x < y är True om x är mindre än y
# x >= y är True om x är större eller lika med y
# x <= y är True om x är mindre eller lika med y
# Kallas rekursion när en funktion anropar sig själv
# Exekvering
#
def bounce(n):
    if n == 0:
        print("0")
    else:
        print(n)
        bounce(n - 1)
        print(n)


#
def bounce2(n):
    start_value = n
    while n >= 0:
        print(n)
        n = n - 1  # n-=1
    n = 1
    while n <= start_value:
        print(n)
        n = n + 1


#
def tvarsumman(n):  # n=123      12
    resten = n % 10  # 3       2
    ssss = n // 10  # 12       1
    if ssss == 0:
        return resten
    else:
        return resten + tvarsumman(ssss)


#
def tvarsumman2(n):  # 234
    sum = 0  # nollställer sum
    #
    while n > 0:  # Så länge n inte är en siffra
        rest = n % 10  # rest sparar sista siffran
        sum = sum + rest  # lägg till sista siffran på summan
        n = n // 10  # ta bort sista siffran från n
    sum = sum + n  # lägg till sista siffran till summan
    return sum  # returnera summan


# ------------------------------------------------------------------------------------
def f1(x):
    return x + 1


def f2(x):
    return x ** (12)  # x^12 -> derivatan: 12*x(12-1) = 12*x^11


def f3(x):
    return -(x**2) + 3 * x + 2  # -x^2+3x+2  -> -2x + 3 *x^(1-1) = -2x + 3


# --------------uppgift 5-------------------------------------------
def derivative(f, x, h):  # hitta lutning f=x+1
    formel = (1) / (2 * h) * (f(x + h) - f(x - h))
    return formel


def solve(f, x0, h):
    xold = x0
    diffx = h + 1  # hur fel är din
    while diffx > h:  # så länge felet är större än
        xnew = xold - f(xold) / derivative(f, xold, h)
        diffx = abs(xnew - xold)
        xold = xnew
    return xnew
