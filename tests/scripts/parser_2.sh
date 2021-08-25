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
	echo "$line"
	break
	((i=i+1))
done < "$INFILE"