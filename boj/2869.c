#include <stdio.h>

int	main(void)
{
	int u;
	int d;
	int h;
	int day;

	scanf("%d %d %d", &u, &d, &h);
	day = 1;
	if (u >= h)
		;
	else if (u - d <= 0)
	{
		printf("%d", 0);
		return (0);
	}
	else if (((h - u) % (u - d)) == 0)
	{
		day += ((h - u) / (u - d));
	}
	else
	{
		day += ((h - u) / (u - d));
		day++;
	}
	printf("%d", day);
	return (0);
}