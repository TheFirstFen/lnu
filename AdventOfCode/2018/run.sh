#!/bin/bash

for ((day=1; day<=25; day++)); do
    echo "Running ./$day.py"
    python3 $day.py $day.in
done
