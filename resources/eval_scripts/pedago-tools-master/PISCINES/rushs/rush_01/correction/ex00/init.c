#include "init.h"
#include "env.h"
#include "check.h"



int	validate_grid(t_env *env)
{
	int	i;

	i = 0;
	while (i < 9)
	{
		if (check_line(env, i))
			return (1);
		else if (check_col(env, i))
			return (1);
		else if (check_square(env, i))
			return (1);
		i = i + 1;
	}
	return (0);
}

int	get_line(t_env *env, char *line, int linenum)
{
	int	i;

	i = 0;
	while (i < 9)
	{
		if (line[i] <= '9' && line[i] >= '1')
			env->tab[linenum * 9 + i] = line[i];
		else if (line[i] == '.')
			env->tab[linenum * 9 + i] = 0;
		else
			return (1);
		i = i + 1;
	}
	if (line[i] != 0)
		return (1);
	return (0);
}

int	init(t_env *env, int argc, char **argv)
{
	int	i;

	if (argc != 10)
		return (1);
	env->solution_found = 0;

	i = 0;
	while (i < 9)
	{
		if (get_line(env, argv[i + 1], i))
			return (1);
		i = i + 1;
	}
	if (validate_grid(env))
	{
		return (1);
	}
	return (0);
}
