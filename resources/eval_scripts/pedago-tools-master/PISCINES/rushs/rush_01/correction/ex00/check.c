#include "check.h"
#include "env.h"

int check_line(struct s_env *env, int num)
{
	int	i;
	int	j;
	
	i = 0;
	while (i < 9)
	{
		if (env->tab[i + num * 9] != 0)
		{
			j = i + 1;
			while (j < 9)
			{
				if (env->tab[j + num * 9] == env->tab[i + num * 9])
				{
					return (1);
				}
				j = j + 1;
			}
		}
		i = i + 1;
	}
	return (0);
}

int check_col(struct s_env *env, int num)
{
	int	i;
	int	j;
	
	i = 0;
	while (i < 9)
	{
		if (env->tab[i * 9 + num] != 0)
		{
			j = i + 1;
			while (j < 9)
			{
				if (env->tab[j * 9 + num] == env->tab[i * 9 + num])
				{
					return (1);
				}
				j = j + 1;
			}
		}
		i = i + 1;
	}
	return (0);
}

int check_square(struct s_env *env, int num)
{
	int	i;
	int	j;
	
	i = 0;
	num = (num % 3 * 3) + (num / 3) * 3 * 9;
	while (i < 9)
	{
		if (env->tab[num + i % 3 + (i / 3) * 9] != 0)
		{
			j = i + 1;
			while (j < 9)
			{
				if (env->tab[num + i % 3 + (i / 3) * 9] == env->tab[num + j % 3 + (j / 3) * 9])
				{
					return (1);
				}
				j = j + 1;
			}
		}
		i = i + 1;
	}
	return (0);
}

