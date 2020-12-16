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
        print("python analytical_backtrans.py [-v] [--set wiki/test/file]")
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


print("all-test-matrices.cpp has been written: it contains lambdas to create test cases (for DLAF)")
outF = open("all-test-matrices.cpp", "w")

outF.write("auto el_C = [](const GlobalElementIndex& index) {\n")
outF.write("  static const double values[] = {")
for col in range(0, A.shape[1]):
    for row in range(0, A.shape[0]):
        outF.write("%.5f" % A[row, col])
        if row == A.shape[0]-1:
            outF.write(" ")
        else:
            outF.write(", ")        
    if col != A.shape[1]-1:
        outF.write(", ")
outF.write("};\n")
outF.write("  return values[index.row() + %d * index.col()];\n" % n)
outF.write("};\n")
outF.write("\n")
    
W = np.zeros((n,n))
W2 = np.zeros((n,n))
R = A

if (v == 1):
    print
    print("==============================")
    print("Solving: the analytical way...")
    print("==============================")
    print


for i in range(0, n-1):
    if (v == 1):
        print("step", i)
    for k in range(i, n):
        if (v == 1):
            print("k ", k)
            print("Vki ", V[k,i])
            print("Tii ", T[i,i])

        W[k,i] = V[k,i] * T[i,i]
    if (v == 1):
        print("W")
        print(W)

    for k in range(0, n):
        for j in range(i, n):
            W2[i,k] = W2[i,k] + W[j,i] * R[j,k]
    if (v == 1):
        print("W2")
        print(W2)
            
    for k in range(i, n):
        for j in range(0, n):
            #print("step, k, j", i, k, j)
            R[k,j] = R[k,j] - V[k,i]*W2[i,j]
    if (v == 1):
        print("R")
        print(R)        
        print


if (v == 1):
    print
    print("======")
    print("RESULT")
    print("======")
    print
    
print 
print(R)
print 


outF.write("auto el_V = [](const GlobalElementIndex& index) {\n")
outF.write("  static const double values[] = {")
for col in range(0, V.shape[1]):
    for row in range(0, V.shape[0]):
        outF.write("%.5f" % V[row, col])
        if row == V.shape[0]-1:
            outF.write(" ")
        else:
            outF.write(", ")        
    if col != V.shape[1]-1:
        outF.write(", ")
outF.write("};\n")
outF.write("  return values[index.row() + %d * index.col()];\n" % n)
outF.write("};\n")
outF.write("\n")

outF.write("auto el_T = [](const GlobalElementIndex& index) {\n")
outF.write("  static const double values[] = {")
for col in range(0, T.shape[1]):
    for row in range(0, T.shape[0]):
        outF.write("%.5f" % T[row, col])
        if row == T.shape[0]-1:
            outF.write(" ")
        else:
            outF.write(", ")        
    if col != T.shape[1]-1:
        outF.write(", ")
outF.write("};\n")
outF.write("  return values[index.row() + %d * index.col()];\n" % n)
outF.write("};\n")
outF.write("\n")

outF.write("auto res = [](const GlobalElementIndex& index) {\n")
outF.write("  static const double values[] = {")
for col in range(0, R.shape[1]):
    for row in range(0, R.shape[0]):
        outF.write("%.5f" % R[row, col])
        if row == R.shape[0]-1:
            outF.write(" ")
        else:
            outF.write(", ")        
    if col != R.shape[1]-1:
        outF.write(", ")
outF.write("};\n")
outF.write("  return values[index.row() + %d * index.col()];\n" % n)
outF.write("};\n")
