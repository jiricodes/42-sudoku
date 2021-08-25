#! /bin/bash
# takes sudoku binary, test files input and expected folders as arguments
# assumes ex
SUDOKU=$1
BASEDIR=$(dirname "$0")

INPUTS=$2
EXPECT=$3
OUTPUTS=$BASEDIR/../outputs

OK='\033[0;32mOK\033[0m'
FAILED='\033[0;31mFAILED\033[0m'

for f in $INPUTS/*
do
	fname=$(basename "$f")
	args=$(cat $f)
	./$SUDOKU $args > $OUTPUTS/$fname 2>&1
	diff=$(diff $OUTPUTS/$fname $EXPECT/$fname)
	if [ -z "$diff" ]
	then
		printf "%-56s $OK\n" $fname
	else
		printf "%-56s $FAILED\n" $fname
		echo "$diff" > $OUTPUTS/${fname}_diff 
	fi
done