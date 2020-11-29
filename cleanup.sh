#! /bin/bash

# used (with caution) to remove all dirs created for that day (i.e mistake withe new_day.sh)

DAY=$1

find . -name day1 -type d -exec rm -rf {} \;