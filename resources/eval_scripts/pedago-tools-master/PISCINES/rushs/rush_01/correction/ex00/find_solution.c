#include "find_solution.h"
#include "env.h"
#include <unistd.h>

void	print_solution(t_env *env)
{
	int 	line;
	int		col;

	line = 0;
	while (line < 9)
	{
		col = 0;
		while (col < 9)
		{
			if (col > 0)
				write(1, " ", 1);
			write(1, env->solution + line * 9 + col, 1);
			col = col + 1;
		}
		write(1, "\n", 1);
		line = line + 1;
	}
}

int		solution_found(t_env *env)
{
	int	i;

	if (env->solution_found != 0)
		return (1);
	env->solution_found = 1;
	i = 0;
	while (i < 81)
	{
		env->solution[i] = env->tab[i];
		i = i + 1;
	}
	return (0);
}

int		check_solution(t_env *env, int c, char val)
{
	int	i;
	int	line;
	int	col;
	int	square;

	i = 0;
	line = c / 9;
	col = c % 9;
	square = (line / 3) * 3 * 9 + (col / 3) * 3;
	while (i < 9)
	{
		if (env->tab[line * 9 + i] == val)
			return (0);
		if (env->tab[col + i * 9] == val)
			return (0);
		if (env->tab[square + i % 3 + (i / 3) * 9] == val)
			return (0);
		i = i + 1;
	}
	return (1);
}

int		find_solution(t_env *env, int c)
{
	char	i;

	if (c == 81)
		return solution_found(env);
	else if (env->tab[c] != 0)
		return find_solution(env, c + 1);
	else
	{
		i = '1';
		while (i <= '9')
		{
			if (check_solution(env, c, i))
			{
				env->tab[c] = i;
				if (find_solution(env, c + 1))
					return (1);
				env->tab[c] = 0;
			}
			i = i + 1;
		}
	}
	return (0);
}
