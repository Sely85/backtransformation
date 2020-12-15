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
        print("python computeReflectorsAndTaus.py [-v] [--input file (should contain A matrix)]")
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
A = mymodule.A

if (v == 1):
    print
    print("============")
    print("Input matrix")
    print("============")
    print
    print("A")
    print(A)
    print
    
m = A.shape[0]
V = np.zeros((m,m))
tau = np.zeros((m,1))

R = A

for j in range(0, m-1):
    s = -np.sign(R[j,j])
    aj = R[j:m, j:j+1]
    norm_aj = np.linalg.norm(aj)
    uj = R[j,j] - s * norm_aj
    vj = R[j:m, j:j+1]/uj
    vj[0,0] = 1.
    V[j:m,j:j+1] = vj

    tauj = - s * uj / norm_aj
    tau[j,0] = tauj

    R[j:m, j+1:m] = R[j:m, j+1:m] - tauj * np.matmul(vj, np.matmul(np.transpose(vj), R[j:m, j+1:m]))

    
if (v == 1):    
    print    
    print("V: matrix of reflectors") 
    print(V)
    print
    print("tau: matrix of tau factors") 
    print(tau)



outF = open("myReflectorsAndTaus.py", "w")
outF.write("import numpy as np\n")
outF.write("V = np.array([")
for row in range(0, V.shape[0]):
    outF.write("[")
    for col in range(0, V.shape[1]):
        outF.write("%.5f" % V[row, col])
        if col != V.shape[1]-1:
            outF.write(", ")        
    if row == V.shape[0]-1:
        outF.write("]")
    else:
        outF.write("], ")
outF.write("])\n")
outF.write("tau = np.array([")
for row in range(0, tau.shape[0]):
    outF.write("[")
    outF.write("%.5f" % tau[row, 0])
    if row == V.shape[0]-1:
        outF.write("]")
    else:
        outF.write("], ")
outF.write("])\n")

print
print("myReflectorsAndTaus.py file has been written")
