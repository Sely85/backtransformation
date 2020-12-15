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
        print("python computeTfactor.py [-v] [--input file (should contain matrix V and vector tau)]")
        exit()
    if (args[i] == "-v"):
        print("verbose mode on")
        v = 1
    if (args[i] == "--input"):
        try:
            print("using data from file " + args[i+1])
            filename = str(args[i+1])
            t='file'
        except:
            exit("Missing input filename")


modulename=filename.replace('.py','')
print(modulename)
mymodule = importlib.import_module(modulename)
V = mymodule.V
tau = mymodule.tau

if (v == 1):
    print
    print("==============")
    print("Input matrices")
    print("==============")
    print
    print("V")
    print(V)
    print
    print("tau")
    print(tau)
    print
    
m = tau.shape[0]
n = tau.shape[1]
effsize = m - 1
T = np.zeros((m,m))

for j in range(0, effsize):
    for i in range(0, j):
        for k in range(0, j):
            v_a = V[0:m, k:k+1]
            v_b  = V[0:m, j:j+1]
            tau_t = T[i:i+1,k:k+1]
            T[i, j] = T[i,j] + tau_t * np.matmul(np.transpose(v_a), v_b)
        T[i,j] =  - tau[j, 0] * T[i,j]
    T[j, j] = tau[j, 0]

if (v == 1):
    print
    print("==============")
    print("Output matrix:")
    print("   T factor   ")
    print("==============")
    print
    print(T)


outF = open("myTfactor.py", "w")
outF.write("import numpy as np\n")
outF.write("T = np.array([")
for row in range(0, V.shape[0]):
    outF.write("[")
    for col in range(0, V.shape[1]):
        outF.write("%.5f" % T[row, col])

        if col != V.shape[1]-1:
            outF.write(", ")
        
    if row == V.shape[0]-1:
        outF.write("]")
    else:
        outF.write("], ")
                
outF.write("])\n")

print
print("myTfactor.py file has been written")
