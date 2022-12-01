from sympy import Symbol, sin, cos
from sympy.physics.vector import *
import numpy as np

N = ReferenceFrame('N')
q1 = dynamicsymbols('q1')
u1 = dynamicsymbols('u1')
l1 = Symbol('l1')

A = N.orientnew('A', 'Axis', [q1, N.x])
A.set_ang_vel(N, u1 * N.x)

J0 = Point('J0')
J1 = J0.locatenew('J1', l1 * (cos(q1) * A.x + sin(q1) * A.y))
J1.set_vel(A, l1 * u1 * (-sin(q1) * A.x + cos(q1) * A.y))
J1.v1pt_theory(J1, N, A)

