#include <stdlib.h>
#include <stdio.h>

int	rev_num(int n)
{
	return ((n % 100 % 10 * 100) + (n % 100 / 10 * 10) + (n / 100));
}

int main(void)
{
	int	a;
	int	b;

	scanf("%d %d", &a, &b);
	
	if (a % 10 > b % 10)
		printf("%d", rev_num(a));
	else if (a % 10 < b % 10)
		printf("%d", rev_num(b));
	else if (a % 100 / 10 > b % 100 / 10)
		printf("%d", rev_num(a));
	else if (a % 100 / 10 < b % 100 / 10)
		printf("%d", rev_num(b));
	else if (a / 100 > b / 100)
		printf("%d", rev_num(a));
	else if (a / 100 < b / 100)
		printf("%d", rev_num(b));
}
