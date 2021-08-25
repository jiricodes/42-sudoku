#! /bin/bash

INFILE=$1
OUTFILE=$2

INDIR=praser_in
OUTDIR=parser_out

mkdir -p $INDIR
mkdir -p $OUTDIR

rm -f $INDIR/* $OUTDIR/*

i=0
while read -r line
do
	line=$(echo $line | tr -d "'" | awk '{$1=""}1' | awk '{$1=$1}1')
	n=$(echo "$line" | grep -P -o '\d' | wc -l)
	s=$(($i*9+1))
	e=$(($s+9))
	c=$(($e+1))
	echo "[$n] $line"
	out=$(sed -n '$s,$e;$c' $OUTFILE)
	echo "$out"
	break
	((i=i+1))
done < "$INFILE"