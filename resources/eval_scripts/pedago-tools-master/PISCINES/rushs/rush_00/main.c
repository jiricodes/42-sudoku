/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ablette <ablette@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/05/26 20:57:39 by ablette           #+#    #+#             */
/*   Updated: 2019/05/26 21:49:21 by ablette          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

void rush(int x, int y);

int main(int ac, char **av)
{
  int x, y;

  x = atoi(av[1]);
  y = atoi(av[2]);
  // x = 4;
  // y = 3;
  rush(x, y);

  return (0);
}
