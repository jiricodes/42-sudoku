/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   example-unittest.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jnovotny <jnovotny@student.hive.fi>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/08/24 11:45:50 by jnovotny          #+#    #+#             */
/*   Updated: 2021/08/24 18:26:28 by jnovotny         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "sudoku.h"
#include <stdio.h>
#include <assert.h>

static void	test_is_solution() {
	int ret;

	printf("is_solution:\t");
	int	grid[SUDOKU_SIZE][SUDOKU_SIZE] = {{9, 0, 0, 0, 7, 0, 0, 0, 0},
										  {2, 0, 0, 0, 9, 0, 0, 5, 3},
										  {0, 6, 0, 0, 1, 2, 4, 0, 0},
										  {8, 4, 0, 0, 0, 1, 0, 9, 0},
										  {5, 0, 0, 0, 0, 0, 8, 0, 0},
										  {0, 3, 1, 0, 0, 4, 0, 0, 0},
										  {0, 0, 3, 7, 0, 0, 6, 8, 0},
										  {0, 9, 0, 0, 5, 0, 7, 4, 1},
										  {4, 7, 0, 0, 0, 0, 0, 0, 0}};
	ret = is_solution(grid);
	assert(ret == 0);
	int	grid2[SUDOKU_SIZE][SUDOKU_SIZE] = {{5, 3, 6, 8, 2, 7, 9, 4, 1},
										  {1, 7, 2, 9, 6, 4, 3, 5, 8},
										  {8, 9, 4, 1, 5, 3, 2, 6, 7},
										  {7, 1, 5, 3, 4, 9, 8, 2, 6},
										  {6, 4, 3, 7, 8, 2, 1, 9, 5},
										  {9, 2, 8, 5, 1, 6, 7, 3, 4},
										  {4, 8, 1, 2, 9, 5, 6, 7, 3},
										  {3, 6, 9, 4, 7, 1, 5, 8, 2},
										  {2, 5, 7, 6, 3, 8, 4, 1, 9}};
	ret = is_solution(grid2);
	assert(ret == 1);
	printf("OK\n");
}

static void test_is_candidate() {
	int row, col, val, ret;

	printf("is_candidate:\t");
	int	grid[SUDOKU_SIZE][SUDOKU_SIZE] = {{9, 0, 0, 0, 7, 0, 0, 0, 0},
										  {2, 0, 0, 0, 9, 0, 0, 5, 3},
										  {0, 6, 0, 0, 1, 2, 4, 0, 0},
										  {8, 4, 0, 0, 0, 1, 0, 9, 0},
										  {5, 0, 0, 0, 0, 0, 8, 0, 0},
										  {0, 3, 1, 0, 0, 4, 0, 0, 0},
										  {0, 0, 3, 7, 0, 0, 6, 8, 0},
										  {0, 9, 0, 0, 5, 0, 7, 4, 1},
										  {4, 7, 0, 0, 0, 0, 0, 0, 0}};
	row = 0;
	col = 1;
	val = 2;
	ret = is_candidate(grid, row, col, val);
	assert(ret == 0);
	val = 6;
	ret = is_candidate(grid, row, col, val);
	assert(ret == 0);
	col = 2;
	val = 7;
	ret = is_candidate(grid, row, col, val);
	assert(ret == 0);
	val = 5;
	ret = is_candidate(grid, row, col, val);
	assert(ret == 1);
	printf("OK\n");
}

int main() {
	test_is_solution();
	test_is_candidate();
	return (0);
}