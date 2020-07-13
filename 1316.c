#include <stdio.h>
#include <stdlib.h>

int	check_strs(char *str)
{
	int i;
	int j;

	i = 0;
	while (str[i])
	{
		j = 0;
		while (j < i)
		{
			if (str[j] == str[i])
				return (0);
			j++;
		}
		while (str[i] == str[i + 1])
			i++;
		i++;
	}
	return (1);
}

int	main(void)
{
	int word_count;
	int	result = 0;
	int i = 0;
	char str[101];

	scanf("%d", &word_count);
	while (i < word_count)
	{
		scanf("%s", str);
		if (check_strs(str) == 1)
			result++;
		i++;
	}
	printf("%d", result);
	return (0);
}