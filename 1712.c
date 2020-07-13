#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int A;
	int B;
	int C;

	scanf("%d %d %d", &A, &B, &C);
	if (B >= C)
		printf("-1");
	else
		printf("%d", (A / (C - B)) + 1);
}

