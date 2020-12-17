import numpy as np
import sys
import importlib

np.set_printoptions(precision=9, suppress=True)

args = sys.argv[1:]
l = len(args)
v=0
t=0

#Set defaults
n = 3
t = 'int'
maxv = 200

if (l == 0):
    exit("Missing arguments")
for i in range(l):
    if (args[i] == "-h" or args[i] == "--help"):
        print("python createTestCase.py [-v] [-n <size-nxn>] [-t <int/float/complex> <max-val>]")
        exit()
    if (args[i] == "-v"):
        print("verbose mode on")
        v = 1
    if (args[i] == "-n"):
        try:
            print("Creating test case matrix of size " + args[i+1] + "x" + args[i+1])
            n=int(args[i+1])
        except:
            exit("Missing size of matrix")
    if (args[i] == "-t"):
        try:
            t=args[i+1]
            print("using " + args[i+1] + " type")
        except:
            exit("Missing type of values")
        if (t != 'int' and t != 'float' and t != 'complex'):
            exit("Type unsopported. Allowed types are: int, float and complex")
        try: 
            maxv=int(args[i+2])
            print("with maximum value " + args[i+2])
        except:
            print("assuming maximum value of 200")


# Creating random matrix
if (t == 'int'):
    A = np.random.randint(maxv, size=(n,n))
elif (t == 'float'):
    A = np.zeros((n,n))
    for row in range(0,n):
        for col in range(0,n):
            A[row, col] = np.random.random()*maxv
elif (t == 'complex'):
    A = np.zeros((n,n), dtype=complex)
    for row in range(0,n):
        for col in range(0,n):
            data = np.random.random()*maxv + np.random.random()*maxv *1j
            A[row, col] = data
            
if (v == 1):
    print
    print("===============")
    print(" Random matrix ")
    print("===============")
    print
    print(A)

# Write matrix A to file
outF = open("matrix.py", "w")
outF.write("import numpy as np\n")
outF.write("A = np.array([")
for row in range(0, n):
    outF.write("[")
    for col in range(0, n):
        if (t == 'int'):
            outF.write("%.1f" % A[row, col])
        elif (t == 'float'):
            outF.write("%.1f" % A[row, col])
        elif (t == 'complex'):
            outF.write('{:.2f}'.format(A[row, col]))

        if col != n-1:
            outF.write(", ")
        
    if row == n-1:
        outF.write("]")
    else:
        outF.write("], ")
                
outF.write("])\n")


print
print("matrix.py file has been written")
