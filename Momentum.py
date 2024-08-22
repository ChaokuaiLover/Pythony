def mmt(mass,velocity):
    a = mass * velocity
    return a
Unit = str(input('Enter the unit : '))
M = float(input('Enter the mass : '))
V = float(input('Enter the velocity  : '))
print('Momentum ; ' ,mmt(M,V), Unit)