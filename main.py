import sys

import sympy as sp
from sympy.utilities.lambdify import lambdify

epsilon = 0.0001
#print the derivative in a symbol way
x =sp.symbols('x')
my_f =x**2 -5*x +2
print("my_func: ", my_f)
my_f1=sp.diff(my_f, x)
print("f' : ", my_f1)
d1 = sp.diff(my_f1)
print("f'': ", d1)

#calc the derivative from func -> lambdify
f = x**2 -5*x +2
f_prime = f.diff(x)
print("f : ",f)
print("f' : ",f_prime)
f = lambdify(x, f)
f_prime = lambdify(x, f_prime)
print("f(1):",f(1))
print("f'(1):",f_prime(1))


def bisection(f, start_point, end_point):
    if f(start_point) * f(end_point) >= 0:
        print("Bisection method " )
        return None
    a_n = start_point
    b_n = end_point
    counter = 0
    while (b_n - a_n) >= epsilon:
        m_n = (a_n + b_n) / 2
        f_m_n = f(m_n)
        counter +=1
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    print('Found solution after', counter, 'iterations.')
    return (a_n + b_n) / 2


def newton(f, Df, x0, max_iter):
    xn = x0
    for n in range(0, max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

def secant(f, x0, x1):
    f_x0 = f(x0)
    f_x1 = f(x1)
    iteration_counter = 0
    while abs(f_x1) > epsilon and iteration_counter < 100:
        try:
            denominator = float(f_x1 - f_x0) / (x1 - x0)
            x = x1 - float(f_x1) / denominator
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
            sys.exit(1)  # Abort with error
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter += 1
        # Here, either a solution is found, or too many iterations
    if abs(f_x1) > epsilon:
        iteration_counter = -1
    if iteration_counter > 0:  # Solution found
        print("Number of function calls: %d" % (2 + iteration_counter))
        print("A solution is: %f" % (x))
    else:
        print("Solution not found!")


# switch_case
def switch_case(choise, start, end):
    i = start
    #1 for Bisection,2 for  Newton Rapson , 3 for secant
    if choise == '1':
        while i < end:
            if i * (i + 0.1) < 0:
                bisection(f, i, i+0.1)
            i = i + 0.1
    elif choise == '2':
        while i < end:
            if i * (i + 0.1) < 0:
                newton(f, f_prime, i, i+0.1)
            i = i + 0.1
    elif choise == '3':
        while i < end:
            if i * (i + 0.1) < 0:
                secant(f, i, i+0.1, epsilon)
            i = i + 0.1
    else:
        print("Bad Choise")


start = input("enter  start range: ")
start = int(start)
end = input("enter end range: ")
end = int(end)
choise = input(
    "In what method you interested in finding the roots of the equation \n1 for Bisection, 2 for  Newton Rapson , 3 for secant\nyour choise ? : ")
switch_case(choise,start,end)







