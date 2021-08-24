/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printer.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/24 11:51:02 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 12:05:30 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"

/*
** @brief	Simple Error message helper function
** 
** 
*/

void error_message() {
	write(2, "Error\n", 6);
}


/*
** @brief	Printing out function.
** 
** @param	*int[SUDOKU_SIZE] Grid to be printed
*/

void print_sudoku(int (*grid)[SUDOKU_SIZE]) {
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
