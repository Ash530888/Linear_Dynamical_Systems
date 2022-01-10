import matplotlib.pyplot as plt
import numpy as np

import sys
import argparse

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--B", help="number of simulation steps",
                        default="2000")
    parser.add_argument("--A", help="matrix A",
                        default=" 0.9872, -0.0272, 0.008 ,  1.0128")
    parser.add_argument("--C", help="matrix C",
                        default="1.0,0.0,0.0,1.0")
    parser.add_argument("--Gamma",
                        help="state noise covariance",
                        default="0.001,0.0,0.0,0.001")
    parser.add_argument("--Sigma",
                        help="observation noise covariance",
                        default="0.05,0.0,0.0,0.05")
    parser.add_argument("--m0",
                        help=" mean of the initial state",
                        default="0,0")
    parser.add_argument("--V0",
                        help="covariance of the initial state",
                        default="0.001,0.0,0.0,0.001")




    args = parser.parse_args()
    B=int(args.B)
    C=np.fromstring(args.C, sep=',').reshape(2,2)
    A=np.fromstring(args.A, sep=',').reshape(2,2)
    Gamma=np.fromstring(args.Gamma, sep=',').reshape(2,2)
    Sigma=np.fromstring(args.Sigma, sep=',').reshape(2,2)
    m0=np.fromstring(args.m0, sep=',')
    V0=np.fromstring(args.V0, sep=',').reshape(2,2)

    X=np.zeros((2,B))
    Y=np.zeros((2,B))

    w=np.random.multivariate_normal(m0, Gamma,(B,))
    v=np.random.multivariate_normal(m0, Sigma,(B,))

    x0 = np.random.multivariate_normal(m0, V0, (2,))
    X[0,0],X[1,0]=x0[0,0],x0[1,0]
    y0=np.add(np.dot(C,x0),v[0])
    Y[0,0],Y[1,0]=y0[0,0],y0[0,1]


    x=np.zeros(2,)
    for i in range(1, B):
        x[0],x[1]=X[0][i-1],X[1][i-1]
        Xn=np.add(np.dot(A,x),w[i])
        X[0,i],X[1,i]=Xn[0],Xn[1]
        Yn=np.add(np.dot(C,Xn),v[i])
        Y[0,i],Y[1,i]=Yn[0],Yn[1]

    print(Y)

    plt.plot(X[0,:],X[1,:])
    plt.xlabel('x[0]')
    plt.ylabel('x[1]')
    plt.show()
    plt.plot(Y[0,:],Y[1,:],c='r')
    plt.xlabel('y[0]')
    plt.ylabel('y[1]')
    plt.show()



if __name__=="__main__":
    main(sys.argv)
