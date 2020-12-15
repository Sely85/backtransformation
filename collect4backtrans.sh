#!/bin/bash

cat matrix.py > test-backtrans.py
grep "V " myReflectorsAndTaus.py >> test-backtrans.py
grep "T " myTfactor.py >> test-backtrans.py
