# 42-sudoku
Sudoku solver is one of the 42 piscine's team project. This is reference solution and test suite for evaluating new pisciners at Hive Helsinki

## example-solution
Contains a Sudoku solver with recursive approach. Not Norm complient and not satisfying all requirements (e.g. doesn't invalidate multiple solution sudokus).


```
make
```


## resources
Contains the subject pdf as well as some links

## tests
Test suite with norminette, compilation, leaks and multiple input tests (errors, valids, different difficulty). Tested on Linux (Ubuntu 18.04) and MacOS (BigSur).

Requires norminette and (if Linux) valgrind.

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
which uses the example-solution to run tests.
