#! /bin/bash

INFILE=$1
OUTFILE=$2

INDIR=parser_in
OUTDIR=parser_out

mkdir -p $INDIR
mkdir -p $OUTDIR

rm -f $INDIR/* $OUTDIR/*

i=0
while read -r line
do
	line=$(echo $line | tr -d "'" | awk '{$1=""}1' | awk '{$1=$1}1')
	n=$(echo "$line" | grep -P -o '\d' | wc -l)

	l=$(find $INDIR -name "$n*" | tail -n 1 | tail -c 3)
	l=$(expr $l + 1)
	newname=$(printf "%d_clues_solvable_%02d" $n $l)

	echo $line > $INDIR/$newname

	s=$(($i*9+1))
	e=$(($s+8))
	c=$(($e+1))
	pattern="$s,${e}p;${c}q"
	out=$(sed -n $pattern $OUTFILE)
	echo "$out" > $OUTDIR/$newname

	((i=i+1))
done < "$INFILE"