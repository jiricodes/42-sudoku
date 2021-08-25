#! /bin/bash

TARGET_DIR=$1

TMP_DIR=tmp
mkdir -p $TMP_DIR

TARGET=$TMP_DIR/rush-1

OK='\033[0;32mOK\033[0m'
FAILED='\033[0;31mFAILED\033[0m'


# prereqs
os=$(uname)
if [ "$os" == "Linux" ]
then
	ret=$(valgrind --version)
	if [ "$?" -ne "0" ]
	then
		echo "Valgrind not installed"
		exit
	fi
fi

# norm test
norm_ver=$(norminette --version)
if [ "$?" -ne "0" ]
then
	echo "Norminette not available"
	exit
fi

norm=$(norminette $TARGET_DIR | grep -i "error!" )
title=$(printf "Norm [%s]" "$norm_ver")
if [ -z "$norm" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
fi

# compilation test
title="Compilation"
ret=$(gcc -Wall -Wextra -Werror -o $TARGET $TARGET_DIR/*.c 2>/dev/null)
if [ "$?" -eq "0" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi

# leaks
title="Memory Leaks"
if [ "$os" == "Linux" ]
then
	valgrind --tool=memcheck --leak-check=full --show-leak-kinds=all ./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." > $TMP_DIR/leaks 2>&1
	ret=$(cat $TMP_DIR/leaks | grep -i "error summary" | awk '{ print $4 }')
else
	leaks -atExit -- ./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." > $TMP_DIR/leaks 2>&1
	ret=$(tail -n 2 $TMP_DIR/leaks | grep -i "error summary" | awk '{ print $3 }')
fi

if [ "$ret" == "0" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi