#include <stdio.h>
#include <math.h>

int	get_result(int x, int y)
{
	int count;
	int sqrt_n;
	int left_n;

	count = 0;
	sqrt_n = (int)sqrt(y - x);
	left_n = (y - x) - (int)pow(sqrt_n, 2);
	if (left_n == 0)
		count = (sqrt_n * 2) - 1;
	else if (left_n <= sqrt_n)
		count = (sqrt_n * 2);
	else
		count = (sqrt_n * 2) + 1;
	return (count);
}

int main(void)
{
	int test_case;
	int x;
	int y;
		

	scanf("%d", &test_case);
	while (test_case--)
	{
		scanf("%d %d", &x, &y);
		if (test_case != 0)
			printf("%d\n", get_result(x, y));
		else
			printf("%d", get_result(x, y));
	}
	return (0);
}
