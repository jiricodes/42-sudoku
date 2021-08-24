/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_static_grid.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/24 11:50:04 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 18:24:19 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"
#include <stdio.h>

/*
** @brief	Checks validity of the current state for solution
**
**			This approach iterates over the board 3x in different directions.
**			Rows, Columns and Boxes are check each for validity.
**			Another solution would be to track each groups validity
**			and iterate over board only once. The question is CPU cycles
**			versus memory.
** 
** @return	int  1 if valid else 0
*/

int is_solution(int (*grid)[SUDOKU_SIZE]) {
	int column;
	int row;
	int used_numbers; //holds bit values 
	int	box;

	//check rows
	used_numbers = 0;
	row = 0;
	while (row < SUDOKU_SIZE) {
		column = 0;
		while (column < SUDOKU_SIZE) {
			if ( grid[row][column] == 0 || used_numbers & (1 << grid[row][column]))
				return (0);
			used_numbers |= 1 << grid[row][column];
			column++;
		}
		used_numbers = 0;
		row++;
	}

	//check columns
	used_numbers = 0;
	column = 0;
	while (column < SUDOKU_SIZE) {
		row = 0;
		while (row < SUDOKU_SIZE) {
			// checking for grid[row][column] == 0 is obsolete
			if (used_numbers & (1 << grid[row][column]))
				return (0);
			used_numbers |= 1 << grid[row][column];
			row++;
		}
		used_numbers = 0;
		column++;
	}

	// check boxes
	// Number 3 could be substite for const SUDOKU_BOX_SIZE making the code more flexible
	used_numbers = 0;
	box = 0;
	while (box < SUDOKU_SIZE) {
		row = (box / 3) * 3; // int division truncates the rows, possible row values are therefore 1,2,3;
		while (row < ((box / 3) * 3) + 3) { // same trick as above, upper limit it offset by 3
			column = (box % 3) * 3; // similar to row trunc, modulo supplies columns instead
			while (column < ((box % 3) * 3) + 3) {
				// checking for grid[row][column] == 0 is obsolete
				if (used_numbers & (1 << grid[row][column]))
					return (0);
				used_numbers |= 1 << grid[row][column];
				column++;
			}
			used_numbers = 0;
			row++;
		}
		box++;
	}
	return (1);
}

int is_candidate(int (*grid)[SUDOKU_SIZE], int row, int column, int value) {
	int r;
	int c;
	int box;

	// check row
	c = 0;
	while (c < SUDOKU_SIZE) {
		if (value == grid[row][c])
			return (0);
		c++;
	}

	// check column
	r = 0;
	while (r < SUDOKU_SIZE) {
		if (value == grid[r][column])
			return (0);
		r++;
	}

	// check box
	box = (row / 3) * 3 + (column / 3);
	r = (box / 3) * 3;
	while (r < ((box / 3) * 3) + 3) {
		c = (box % 3) * 3;
		while (c < ((box % 3) * 3) + 3) {
			if (value == grid[r][c])
				return (0);
			c++;
		}
		r++;
	}

	return (1);
}

/*
** @brief	Finds first empty (0) cell in the grid. If not 0 guaranteed in input,
**			user should check if output row == SUDOKU_SIZE then no 0 found.
** 
** @param	row 
** @param	column 
** 
*/

void	find_first_zero(int (*grid)[SUDOKU_SIZE], int *row, int *column) {
	*row = 0;
	while (*row < SUDOKU_SIZE) {
		*column = 0;
		while (*column < SUDOKU_SIZE) {
			if ( grid[*row][*column] == 0)
				return ;
			*column += 1;
		}
		*row += 1;
	}
}
