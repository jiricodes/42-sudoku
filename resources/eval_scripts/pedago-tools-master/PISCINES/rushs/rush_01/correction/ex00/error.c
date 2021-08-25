#include "error.h"
#include <unistd.h>


int	ft_error(void)
{
	write(1, "Error\n", 6);
	return (1);
}
