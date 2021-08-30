# 42-sudoku
Sudoku solver is one of the 42 piscine's team project. This is a reference solution and a test suite for evaluating new pisciners at Hive Helsinki, or any other 42 school for that matter.

## example-solution
Contains a Sudoku solver with recursive approach. Not Norm complient and not satisfying all requirements (e.g. doesn't invalidate multiple solution sudokus).


```
make
```

## Resources
Contains the subject pdf as well as some links

## Tests
Test suite with norminette, compilation, leaks and multiple input tests (errors, valids, different difficulty). Tested on Linux (Ubuntu 18.04) and MacOS (BigSur).

Requires norminette and (if Linux) valgrind. If multiple norminettes are present or your command is non-standard `norminette`, the command can be customize on [line 7 of tester.sh](https://github.com/jiricodes/42-sudoku/blob/915dd9d9d2497c556349af9945de0203a4d1375b/tests/scripts/tester.sh#L7).

### Usage
It is recommended to open new terminal, since first command of the script is `tput reset`, that clears the whole terminal window (including history).

```
cd tests
make SUDOKU=project_path
```

or

```
cd tests
make
```
which uses the `example-solution/` to run tests.


## Contributions

Contributions are very welcome. Do not hesitate to PR your own solutions, tests, resources, language and typo fixes etc. Issues tab is open for business as well.

### Adding tests
If you would like to add more tests to the main `tester.sh` please follow this patterns:
- the user should be prompted before starting the test. For example:
	```
	echo ""
	i=2 # counter for number of lines to move cursor back
	while true
	do
		read -p "Would you like to run extra hard tests? This may take a while (y/n): " ret #prompt
		case $ret in
			[Yy]* ) tput cuu $i; tput ed; break;; # do not change tput code if you're not sure.
			[Nn]* ) tput cuu $i; tput ed; exit ;;
			* ) ((i=i+1)); echo -n "Please answer y/n. ";;
		esac
	done
	```
- feel free to choose structure of your own tests. but generally input and expected files should be located in their relevant folders. If you would like to use my preset do following:
	* create identically named folders and test files in `tests/inputs/` and `tests/expected/`
	* add the above described prompt and following lines at the end of `tests/scripts/tester.sh` and adjust echoes and folder paths accordingly:
	```
	#<Section name comment>
	echo ""
	echo "Section name"
	$TESTFILES $TARGET $BASEDIR/../inputs/<path to input filder> $BASEDIR/../expected/<path to expected results folder>
	```
### Sudoku solvers
The solution must be complient with the [subject](/resources/rush01.en.pdf). 42 Norm can be found [here](https://github.com/42School/norminette). I would prefer unique solutions or solutions showcasing specific feature, way of coding or e.g. memory management. Please describe your solution well in PR or README.

### Sudoku generators
It would be neat to have a sudoku generator that could generate tests on demand. I might have a go on it at some point, but there's no time right now.
