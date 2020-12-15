import numpy as np
import sys
import importlib

np.set_printoptions(precision=9, suppress=True)

args = sys.argv[1:]
l = len(args)
v=0
t=0
if (l == 0):
    exit("Missing arguments")
for i in range(l):
    if (args[i] == "-h" or args[i] == "--help"):
        print("python matmul_backtrans.py [-v] [--set wiki/test/file]")
        exit()
    if (args[i] == "-v"):
        print("verbose mode on")
        v = 1
    if (args[i] == "--set"):
        if (args[i+1] == "test"):
            print("using set: test")
            t='test'
        elif (args[i+1] == "wiki"):
            print("using set: wiki")
            t='wiki'
        elif (args[i+1] == "file"):
            try:
                print("using set: file " + args[i+2])
                filename = str(args[i+2])
                t='file'
            except:
                exit("Missing input filename")
        else:
            exit("This set does not exist. Available test sets are: wiki and test")

n = 0
A = 0
V = 0
T = 0
if (t == 'test'):
    A = np.array([[1., 0.5, 0.25], [2, 1., 0.5], [4., 2., 1.]])
    V = np.array([[1., 0., 0.], [0.5, 1., 0.], [0.25, 0.5, 0.]])
    T = np.array([[1., 0., 0.], [0., 0.25, 0.], [0., 0., 0.]])
elif (t == 'wiki'):
    A = np.array([[12., -51., 4.], [6., 167., -68.], [-4., 24., -41.]])
    V = np.array([[1., 0., 0.], [0.23077, 1., 0.], [-0.15385, 0.05556, 0.]])
    T = np.array([[1.85, -0.82, 0.], [0., 1.99, 0.], [0., 0., 0.]])
#    T = np.array([[1.85, 0., 0.], [0., 1.99, 0.], [0., 0., 0.]])
elif (t == 'file'):
    modulename=filename.replace('.py','')
    print(modulename)
    mymodule = importlib.import_module(modulename)
    A = mymodule.A
    V = mymodule.V
    T = mymodule.T

n = A.shape[0]
    
    
if (v == 1):
    print
    print("==============")
    print("Input matrices")
    print("==============")
    print
    print("A")
    print(A)
    print
    print("V")
    print(V)
    print
    print("T")
    print(T)
    print

    

if (v == 1):
    print
    print("================================")
    print("Solving: the mathematical way...")
    print("================================")
    print



VH = np.matrix(V).getH()
TH = np.matrix(T).getH()

VT = np.matmul(V, TH)
if (v == 1):
    print("VT")
    print(VT)
VTV = np.matmul(VT, VH)
if (v == 1):
    print("VTV")
    print(VTV)
VTVA = np.matmul(VTV, A)
if (v == 1):
    print("VTVA")
    print(VTVA)
R = A - VTVA 
    
if (v == 1):
    print
    print("======")
    print("RESULT")
    print("======")
    print
    
print 
print(R)
print 

