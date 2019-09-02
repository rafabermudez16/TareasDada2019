#lachicharronera .py


def chicha(a, b, c):
    d  = b * b - 4 * a * c
    if d >= 0: #raices reales
        return ((-b + (d ** .5)) / (2.0 / a),
                (-b - (d ** .5)) / (2.0 / a))
    else:
        d = -d #raices complejas
        return (complex(-b, (d ** .5)) / (2.0 * a),
                complex(-b, -(d ** .5)) / (2.0 * a))

#prueba
x1, x2 = chicha(5, 10, 6)
if x1 == x2:
    print ("\n\n\n\nSoluciones reales e iguales: \t\n\n\n\nx1 = x2 = %.2f" % x1)
elif type(x1) == complex:
     print ("\n\n\n\n Soluciones complejas y conjugadas \t\n\n\n\n x1 = %.2f+%.2fi \t\n\n\n\n x2 = %.2f+%.2fi" % (x1.real, x1.imag, x2.real, x2.imag))
else:
    print ("\n\n\n\n Soluciones reales y diferentes \t\n\n\n\n x1 = %.2f, \t\n\n\n\n x2 = %.2f" % (x1, x2))
