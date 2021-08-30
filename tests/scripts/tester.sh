#! /bin/bash

# needed for correct tput functionality with every pass
tput reset
tput init

NORM_CMD="norminette"

TARGET_DIR=$1

TMP_DIR=tmp
mkdir -p $TMP_DIR

TARGET=$TMP_DIR/rush-1

BASEDIR=$(dirname "$0")
TESTFILES=./$BASEDIR/test_files.sh

OK='\033[0;32mOK\033[0m'
FAILED='\033[0;31mFAILED\033[0m'

echo "################################################################"
echo "#                                                              #"
echo "#    SUDOKU TESTER                                             #"
echo "#                                                              #"
echo "#       Designed for 42 piscine rush-01 evaluations.           #"
echo "#       Issues and PRs are welcome at                          #"
echo "#       https://github.com/jiricodes/42-sudoku                 #"
echo "#                                                              #"
echo "#                                                              #"
echo "#                            Made by jiricodes.com (2021)      #"
echo "#                                                              #"
echo "################################################################"
echo ""

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

# GROUP: Preliminary tests
echo "*** PRELIMINARIES **********************************************"
echo ""
echo "Simple"

# Team present
title="Whole group present"
tput sc
while true
do
	read -p "Is the whole team present? (y/n): " ret
	case $ret in
		[Yy]* ) tput rc; tput ed; printf "%-56s $OK\n" "$title"; break;;
		[Nn]* ) tput rc; tput ed; printf "%-56s $FAILED\n" "$title"; break ;;
		* ) echo -n "Please answer y/n. ";;
	esac
done

# Check files
title="Files in repository"
tput sc
echo "Here is list of files in given directory:"
ls -a $TARGET_DIR
while true
do
	read -p "Are all files correct? (y/n): " ret
	case $ret in
		[Yy]* ) tput rc; tput ed; printf "%-56s $OK\n" "$title"; break;;
		[Nn]* ) tput rc; tput ed; printf "%-56s $FAILED\n" "$title"; break ;;
		* ) echo -n "Please answer y/n. ";;
	esac
done

# norm test
norm_ver=$(eval "$NORM_CMD --version | tail -n 1")
if [ "$?" -ne "0" ]
then
	echo "Norminette not available"
	exit
fi

norm=$(eval "$NORM_CMD $TARGET_DIR" | grep -i "error")
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

# Error inputs
echo ""
echo "Preliminary tests"
# A badly formatted grid
title="A badly formatted grid"
ret=$(./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5....8.." ".31..4..." "..37..68.." ".9..5.741" "47......." 2>&1)
if [ "$ret" == "Error" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi

# A wrong grid
title="A wrong grid"
ret=$(./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "48......." 2>&1)
if [ "$ret" == "Error" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi

# A grid with bad characters
title="A grid with bad characters"
ret=$(./$TARGET "9...7.,.." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "48......." 2>&1)
if [ "$ret" == "Error" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi

# A grid with too many or too few boxes
title="A grid with too many or too few boxes"
ret=$(./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "........." ".9..5.741" 2>&1)
if [ "$ret" == "Error" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi

# features
echo ""
echo "*** FEATURES ***************************************************"

# Functionality tests
echo ""
echo "Functionality tests"
title="Functionality tests"
$TESTFILES $TARGET $BASEDIR/../inputs/features $BASEDIR/../expected/features

# Explanations
echo ""
echo "Explanations part"
title="Explanations"
echo "All members should know the code as a whole and explain"
echo "their work in detail. The grade is based on the worst answer."
echo "Ask following questions:"
echo "  - (No code) What's the algorithm? How it works?"
echo "  - If bit manipulation present, please explain"
echo "  - Explain some complex lines of code"
echo "  - Ask the team what recursion is"
echo "  - What's the programs return value when sudoku is filled?"
echo "  - When is the sudoku unsolvable? Invalid?"
echo "  - Check and break malloc protections"
echo "  - etc."
echo ""

i=13
while true
do
	read -p "Were you satisfied with provided explanations? (y/n): " ret
	case $ret in
		[Yy]* ) tput cuu $i; tput ed; printf "%-56s $OK\n" "$title"; break;;
		[Nn]* ) tput cuu $i; tput ed; printf "%-56s $FAILED\n" "$title"; break ;;
		* ) ((i=i+1)); echo -n "Please answer y/n. ";;
	esac
done

# Errors 2.0
echo ""
echo "Error management 2.0"
title="Error management 2.0"
$TESTFILES $TARGET $BASEDIR/../inputs/error_management_2 $BASEDIR/../expected/error_management_2


# Continue prompt
echo ""
i=2
while true
do
	read -p "Would you like to run extra tests? (y/n): " ret
	case $ret in
		[Yy]* ) tput cuu $i; tput ed; break;;
		[Nn]* ) tput cuu $i; tput ed; exit ;;
		* ) ((i=i+1)); echo -n "Please answer y/n. ";;
	esac
done

# extras
echo ""
echo "*** EXTRAS *****************************************************"

# errors
echo ""
echo "Errors"
$TESTFILES $TARGET $BASEDIR/../inputs/extras_errors $BASEDIR/../expected/extras_errors

# solvable
echo ""
echo "Solvable"
$TESTFILES $TARGET $BASEDIR/../inputs/extras_solvable $BASEDIR/../expected/extras_solvable


# leaks
echo ""
echo "Leak"
title="Memory Leaks"
if [ "$os" == "Linux" ]
then
	valgrind --tool=memcheck --leak-check=full --show-leak-kinds=all ./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." > $TMP_DIR/leaks 2>&1
	ret=$(cat $TMP_DIR/leaks | grep -i "error summary" | awk '{ print $4 }')
else
	leaks -atExit -- ./$TARGET "9...7...." "2...9..53" ".6..124.." "84...1.9." "5.....8.." ".31..4..." "..37..68." ".9..5.741" "47......." > $TMP_DIR/leaks 2>&1
	ret=$(tail -n 2 $TMP_DIR/leaks | grep -i "leaks" | awk '{ print $3 }')
fi

if [ "$ret" == "0" ]
then
	printf "%-56s $OK\n" "$title"
else
	printf "%-56s $FAILED\n" "$title"
	exit
fi

# Continue prompt
echo ""
i=2
while true
do
	read -p "Would you like to run extra hard tests? This may take a while (y/n): " ret
	case $ret in
		[Yy]* ) tput cuu $i; tput ed; break;;
		[Nn]* ) tput cuu $i; tput ed; exit ;;
		* ) ((i=i+1)); echo -n "Please answer y/n. ";;
	esac
done

#hard
echo ""
echo "Extra hard tests"
$TESTFILES $TARGET $BASEDIR/../inputs/hard $BASEDIR/../expected/hard