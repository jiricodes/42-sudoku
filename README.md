# 42-sudoku
Sudoku solver is one of the 42 piscine's team project. This is reference solution and test kit when evaluating new pisciners at Hive Helsinki

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

```
cd tests
make test SUDOKU=project_path
```

 TODO
 Error management 2.0
 - [ ] add test containing incorrect solution
 - [ ] add test containing grid with multiple solutions
 
 Consider in general
 - [ ] leaks test
 - [ ] speed test
