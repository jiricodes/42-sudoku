/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   solver_recursive.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/24 11:49:05 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 16:49:06 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"
#include <stdio.h>

/*
** @brief	Solves given sudoku recursively.
**
**			TO-DO: even when solution found, check for multi solution to invalidate it.
** 
** @return	int  
*/

int solve_recursive(int (*grid)[SUDOKU_SIZE]) {
	int current_row;
	int current_col;
	int current_val;
	int ret;

	if (is_solution(grid))
		return (0);
	// printf("\n\nrecursion status\n"); fflush(NULL);
	// print_sudoku(grid);
	current_val = 1;
	find_first_zero(grid, &current_row, &current_col);
	if (current_row == SUDOKU_SIZE || current_col == SUDOKU_SIZE)
		return (0);
	while (current_val <= 9) {
		if (is_candidate(grid, current_row, current_col, current_val)) {
			grid[current_row][current_col] = current_val;
			ret = solve_recursive(grid);
			if (ret == 0)
				return (0);
		}
		current_val++;
	}
	grid[current_row][current_col] = 0;
	return (1);
}
