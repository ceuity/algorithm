#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int	n;

	scanf("%d", &n);
	if (n == 4 || n == 7)
		printf("-1");
	else if (n % 5 == 4)
		printf("%d", n / 5 + 2);
	else if (n % 5 == 3)
		printf("%d", n / 5 + 1);
	else if (n % 5 == 2)
		printf("%d", n / 5 + 2);
	else if (n % 5 == 1)
		printf("%d", n / 5 + 1);
	else
		printf("%d", n / 5);
}
