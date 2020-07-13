#include <stdio.h>
#include <stdlib.h>

int	up_1(int u, int d, int h)
{
	int day;

	day = 1;
	if (u >= h)
		return (day);
	if (((h - u) % (u - d)) != 0)
	{
		day = ((h - u) / (u - d));
		day += 2;
	}
	else
	{
		day = ((h - u) / (u - d));
		day++;
	}
	return (day);
}

int	up_2(int u, int d, int h)
{
	int day;
	int now;


	now = 0;
	day = 1;
	while (1)
	{
		now += u;
		if (now >= h)
			return (day);
		now -= d;
		day++;
	}
}

int main(void)
{
	int u;
	int d;
	int h;

	scanf("%d %d %d", &u, &d, &h);
	printf("%d | %d\n", up_1(u, d, h), up_2(u, d, h));
}
