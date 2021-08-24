/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   input_handler.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/24 12:05:03 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 21:10:25 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"

/*
** @brief	Handles transcription from command line arguments into 2d grid
** 
** @param	argc Number of arguments
** @param	argv Array of argument strings
** @param	grid Output grid
** 
** @return	int  0 on success or 1 on error
*/

int handle_input(int argc, char **argv, int (*grid)[SUDOKU_SIZE]) {
	int row;
	int column;
	int clue_count; // The valid sudoku must have 17 or more clues.

	clue_count = 0;
	row = 0;
	while (row < argc) {
		column = 0;
		while (column < 9) {
			if (argv[row][column] == '.') {
				grid[row][column] = 0;
			} else if (argv[row][column] >= '1' && argv[row][column] <= '9') {
				grid[row][column] = argv[row][column] - 48;
				clue_count += 1;
			} else {
				return (1);
			}
			column++;
		}
		if (argv[row][column] != '\0')
			return (1);
		row++;
	}
	if (clue_count >= SUDOKU_MIN_CLUES)
		return (0);
	else
		return (1);
}
