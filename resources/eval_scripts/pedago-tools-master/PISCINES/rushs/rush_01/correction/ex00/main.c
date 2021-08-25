#include "error.h"
#include "init.h"
#include "env.h"
#include "find_solution.h"
#include <stdio.h>
#include <stdlib.h>

int ft_strlen(char *s)
{
  int i = 0;
  while (s[i]) {
    s++;
  }
  return(i);
}

int	main(int argc, char **argv)
{
	t_env	env;
  (void)argc;
  (void)argv;
  int i;

  // ft_strlen(NULL);
	if (init(&env, argc, argv))
		return ft_error();
	else if (find_solution(&env, 0))
		return ft_error();
	else if (env.solution_found == 0)
		return ft_error();
	print_solution(&env);
	return (0);
}
