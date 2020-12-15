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
        print("python createTestCase.py [-v] [-n <size-nxn>]")
        exit()
    if (args[i] == "-v"):
        print("verbose mode on")
        v = 1
    if (args[i] == "-n"):
        try:
            print("Creating test case matrix (integers between 0 and 30) of size " + args[i+1] + "x" + args[i+1])
            n=int(args[i+1])
        except:
            exit("Missing size of matrix")

# Creating random matrix (values between 0 and 1)
A = np.random.randint(30, size=(n,n))
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
        outF.write("%.1f" % A[row, col])

        if col != n-1:
            outF.write(", ")
        
    if row == n-1:
        outF.write("]")
    else:
        outF.write("], ")
                
outF.write("])\n")


print
print("matrix.py file has been written")
