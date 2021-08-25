/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush02.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ablette <ablette@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/07/25 22:13:56 by ablette           #+#    #+#             */
/*   Updated: 2019/07/25 22:31:13 by ablette          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdlib.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_print_row(char start, char mid, char end, int x)
{
	ft_putchar(start);
	while (--x > 1)
		ft_putchar(mid);
	if (x > 0)
		ft_putchar(end);
	ft_putchar('\n');
}

int		main(int ac, char **av)
{
	int x;
	int y;

	if (ac != 3)
		return (1);
	x = atoi(av[1]);
	y = atoi(av[2]);
	if (x == 0 || y == 0)
		return (1);
	ft_print_row('A', 'B', 'A', x);
	while (--y > 1)
		ft_print_row('B', ' ', 'B', x);
	if (y > 0)
		ft_print_row('C', 'B', 'C', x);
	return (0);
}
