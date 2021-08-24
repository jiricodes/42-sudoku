#! /bin/bash
# takes sudoku binary as an argument
SUDOKU=$1
BASEDIR=$(dirname "$0")

INPUTS=$BASEDIR/../inputs
EXPECT=$BASEDIR/../expected
OUTPUTS=$BASEDIR/../outputs

for f in $INPUTS/*
do
	fname=$(basename "$f")
	args=$(cat $f)
	echo -ne "$fname: \t"
	./$SUDOKU $args > $OUTPUTS/$fname 2>&1
	diff=$(diff $OUTPUTS/$fname $EXPECT/$fname)
	if [ -z "$diff" ]
	then
		echo "OK"
	else
		echo "KO"
		echo "$diff" > $OUTPUTS/${fname}_diff 
	fi
done