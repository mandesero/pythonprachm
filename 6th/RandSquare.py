from random import random


def randsquare(A, B):
    R = [(A[0], (B[0] + A[0]) / 2 - (B[1] - A[1]) / 2, B[0], (B[0] + A[0]) / 2 + (B[1] - A[1]) / 2),
         (A[1], (B[1] + A[1]) / 2 + (B[0] - A[0]) / 2, B[1], (B[1] + A[1]) / 2 - (B[0] - A[0]) / 2)]
    vect1 = [
        R[0][1] - R[0][0],
        R[1][1] - R[1][0]
    ]
    vect2 = [
        R[0][3] - R[0][0],
        R[1][3] - R[1][0]
    ]

    r1 = random()
    r2 = random()
    for i in range(2):
        vect1[i] *= r1
        vect2[i] *= r2

    return vect1[0] + vect2[0] + R[0][0], vect1[1] + vect2[1] + R[1][0]


import numpy as np
import matplotlib.pyplot as plt
def showgr(Dots, Corners, Name="Dots"):
    X, Y = zip(*Dots)
    fig, ax = plt.subplots(num=Name)
    ax.set_aspect(1)
    ax.scatter(X, Y)
    ax.fill(*Corners, fill=False)
    plt.show()



def show(A, B, num=1000):
    dots = [randsquare(A, B) for i in range(num)]
    R = [(A[0], (B[0] + A[0]) / 2 - (B[1] - A[1]) / 2, B[0], (B[0] + A[0]) / 2 + (B[1] - A[1]) / 2),
         (A[1], (B[1] + A[1]) / 2 + (B[0] - A[0]) / 2, B[1], (B[1] + A[1]) / 2 - (B[0] - A[0]) / 2)]
    showgr(dots, R)

show((6,7), (2,12), 5000)


