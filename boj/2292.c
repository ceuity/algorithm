#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int n;
	int	i;
	int a;
	int b;

	scanf("%d", &n);
	i = 0;
	a = 0;
	b = 1;
	while (1)
	{
		if (a < n && n <= b)
			break;
		++i;
		a = b;
		b = b + (6 * i);
	}
	i++;
	printf("%d", i);
}
