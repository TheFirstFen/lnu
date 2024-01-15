#!/bin/bash

for ((day=1; day<=25; day++)); do
	echo "Running ./get_input.py for day $day"
	./get_input.py --day "$day" > "$day.in"
	sleep 2
done
