/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sudoku.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/23 12:41:26 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/23 22:15:11 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"
#include <stdio.h>

/*
** @brief	Simple Error message helper function
** 
** 
*/

static void error_message() {
	write(2, "Error\n", 6);
}

/*
** @brief	Handles transcription from command line arguments into 2d grid
** 
** @param	argc Number of arguments
** @param	argv Array of argument strings
** @param	grid Output grid
** 
** @return	int  0 on success or 1 on error
*/

static int handle_input(int argc, char **argv, int (*grid)[SUDOKU_SIZE]) {
	int row;
	int column;

	row = 0;
	while (row < argc) {
		column = 0;
		while (column < 9) {
			if (argv[row][column] == '.') {
				grid[row][column] = 0;
			} else if (argv[row][column] >= '1' && argv[row][column] <= '9') {
				grid[row][column] = argv[row][column] - 48;
			} else {
				return (1);
			}
			column++;
		}
		if (argv[row][column] != '\0')
			return (1);
		row++;
	}
	return (0);
}

/*
** @brief	Printing out function.
** 
** 
*/

static void print_sudoku(int (*grid)[SUDOKU_SIZE]) {
	int row;
	int column;
	char c;

	row = 0;
	while (row < SUDOKU_SIZE) {
		column = 0;
		while (column < SUDOKU_SIZE) {
			c = grid[row][column] + 48;
			write(1, &c, 1);
			if (column != SUDOKU_SIZE - 1)
				write(1, " ", 1);
			column++;
		}
		write(1, "\n", 1);
		row++;
	}
}

/*
** @brief	Checks validity of the current state
** 
** 
** @return	int  1 if valid else 0
*/

static int is_solution(int (*grid)[SUDOKU_SIZE]) {
	int column;
	int row;
	int used_numbers; //holds bit values 

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
			if ( grid[row][column] == 0 || used_numbers & (1 << grid[row][column]))
				return (0);
			used_numbers |= 1 << grid[row][column];
			row++;
		}
		used_numbers = 0;
		column++;
	}
	return (1);
}


static int solve(int (*grid)[SUDOKU_SIZE]) {
	while (!is_solution(grid)) {
		
	}
	return (1);
}

int main(int argc, char **argv) {
	int	grid[SUDOKU_SIZE][SUDOKU_SIZE];
	int ret;

	ret = 0;
	if (argc == SUDOKU_SIZE + 1)
	{
		argv++;
		argc--;
		ret = handle_input(argc, argv, grid);
		if (ret != 0) {
			error_message();
			return (ret);
		}
		print_sudoku(grid);
	} else {
		error_message();
		ret = 1;
	}
	return (ret);
}