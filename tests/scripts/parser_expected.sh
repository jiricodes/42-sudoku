#! /bin/bash
# parses copied solution from sudokuweb.org
# takes copied raw input file and desired outputname as arguments

RAW=$1
NAME=$2
BASEDIR=$(dirname "$0")
EXPECT=$BASEDIR/../expected

cat $RAW | tr -d '\n' | sed -e 's/.\{9\}/&\n/g' | tr ' ' '.' | awk '$1=$1' FS= OFS=" " > $EXPECT/$NAME
