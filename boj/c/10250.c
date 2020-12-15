#include <stdio.h>

int main(void)
{
	int count;
	int i = 0;
	int h;
	int w;
	int	n;

	scanf("%d", &count);
	while (i < count)
	{
		if (i != 0)
			printf("\n");			
		scanf("%d %d %d", &h, &w, &n);
		if (n % h == 0)
		{
			if (n / h <= 9)
				printf("%d0%d", h, (n / h));
			else
				printf("%d%d", h, (n / h));
		}
		else
		{
			if (n / h + 1 < 10)
				printf("%d0%d", n % h, (n / h + 1));
			else
				printf("%d%d", n % h, (n / h + 1));
		}
		i++;
	}
	return (0);
}