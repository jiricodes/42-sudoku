/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sudoku.h                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/23 13:21:30 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 12:09:46 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef SUDOKU_H
# define SUDOKU_H

# include <stdlib.h>
# include <unistd.h>

/*
** @brief	Sudoku size, currently the program is not designed to solve
**			other sizes, but could be refactored.
*/

# define SUDOKU_SIZE 9

/*
** @brief	Sudoku is considered invalid when under 17 clues are presented.
** 			McGuire, G.; Tugemann, B.; Civario, G. There Is No 16-Clue Sudoku:
**			Solving the Sudoku Minimum Number of Clues Problem via Hitting Set
**			Enumeration. Exp. Math. 2014, 23, 190–217.
**			https://www.tandfonline.com/doi/abs/10.1080/10586458.2013.870056
*/

# define SUDOKU_MIN_CLUES 17

typedef struct	s_sudoku_state {
	int			grid[SUDOKU_SIZE][SUDOKU_SIZE];
	int			candidates[SUDOKU_SIZE][SUDOKU_SIZE];
}				t_sudoku_state;


/*
**	Function Prototypes ********************************************************
*/


int handle_input(int argc, char **argv, int (*grid)[SUDOKU_SIZE]);

int solve_recursive(int (*grid)[SUDOKU_SIZE]);
int is_solution(int (*grid)[SUDOKU_SIZE]);
int is_candidate(int (*grid)[SUDOKU_SIZE], int row, int column, int value);
void find_first_zero(int (*grid)[SUDOKU_SIZE], int *row, int *column);

void print_sudoku(int (*grid)[SUDOKU_SIZE]);
void error_message();

#endif // SUDOKU_H