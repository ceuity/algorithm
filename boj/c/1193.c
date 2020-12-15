#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int n;
	int a;
	int b;
	int sign;

	scanf("%d", &n);
	a = 1;
	b = 1;
	sign = 1;
	while (--n)
	{
		if (sign == 1 && a == 1)
		{
			b += 1;
			sign = -1;
		}
		else if (sign == 1 && a != 1)
		{
			a -= 1;
			b += 1;
		}
		else if (sign == -1 && b == 1)
		{
			a += 1;
			sign = 1;
		}
		else if (sign == -1 && b != 1)
		{
			a += 1;
			b -= 1;
		}
	}
	printf("%d/%d", a, b);
}
