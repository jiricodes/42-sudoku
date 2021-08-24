#! /bin/bash
# parses copied input from sudokuweb.org
# takes copied raw input file as an argument

RAW=$1
BASEDIR=$(dirname "$0")
INPUTS=$BASEDIR/../inputs

s=$(cat $RAW | tr -d '\n' | sed -e 's/.\{9\}/&\n/g' | tr ' ' '.')
n=$(echo "$s" | grep -P -o '\d' | wc -l)

l=$(find $INPUTS -name "$n*" | tail -n 1 | tail -c 3)
l=$(expr $l + 1)
newname=$(printf "%d_clues_solvable_%02d" $n $l)
echo $s > $INPUTS/$newname
