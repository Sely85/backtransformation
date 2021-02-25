Back-transformation algorithm
=============================

This set of scripts has been used to understand back-transformation algorithm (with reflectors applied from 0 to k, with results comparable to a QR decomposition: Q<sub>n</sub> Q<sub>n-1</sub> ... Q<sub>1</sub> C).

Creating a random matrix
------------------------
`python createTestCase.py -n <n>`

This script creates a _n_ x _n_ matrix, filled with integers ranging from 0 to 30.


Compute Reflectors and Taus
---------------------------
`python computeReflectorsAndTaus.py --input matrix.py`

Using the output file of the previous step, reflectors and taus are computed with this script.


Computing T factor matrix
-------------------------
`python computeTfactor.py --input myReflectorsAndTaus.py`

This script takes as input the previously computed reflectors and taus and compute T factor matrix.


Collect data
------------
`bash collect4backtrans.sh`

This bash script collect starting matrix (A), matrix of reflectors (V) and matrix of T factor (T).


Back-transformation
-------------------
This first python script applies the back-transformation using matrix multiplications (solving A = A - V T V* A): 

`python matmul_backtrans.py  --set file test-backtrans.py`


This second python script applies the algorithm tuned for single element (or tiles in [DLAF](https://github.com/eth-cscs/DLA-Future)):

`python analytical_backtrans.py  --set file test-backtrans.py`
