/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/24 11:48:18 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 11:48:25 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"

int main(int argc, char **argv) {
	// in C there is technically no memory difference between single int array with size [X * X]
	// and 2d array with [X][X]. Neither it should affect compute performance. In other languages
	// this may be untrue.
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
		ret = solve_recursive(grid);
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