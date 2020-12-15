#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	count;
	int i;
	char str[301];

	count = 0;
	i = 0;
	scanf("%s", str);
	while (str[i])
	{
		if (str[i] == 'd' && str[i + 1] == 'z' && str[i + 2] == '=')
		{
			count++;
			i += 2;
		}
		else if (str[i] == 'd' && str[i + 1] == '-')
		{
			count++;
			i += 1;
		}
		else if ((str[i] == 'c' || str[i] == 's' || str[i] == 'z') && str[i + 1] == '=')
		{
			count++;
			i += 1;
		}
		else if (str[i] == 'c' && str[i + 1] == '-')
		{
			count++;
			i += 1;
		}
		else if ((str[i] == 'l' || str[i] == 'n') && str[i + 1] == 'j')
		{
			count++;
			i += 1;
		}
		else
			count++;
		i++;
	}
	printf("%d", count);
}