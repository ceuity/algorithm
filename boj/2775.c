#include <stdio.h>

int sum_arr(int *arr, int n)
{
	int i;
	int sum;

	i = 1;
	sum = 0;
	while (i <= n)
	{
		sum += arr[i];
		i++;
	}
	return (sum);
}

int	get_arr(int k, int n)
{
	int arr[15][15];
	int i;
	int j;

	i = 1;
	j = 1;
	while (j <= 14)
	{
		arr[0][j] = j;
		j++;
	}
	while (i <= k)
	{
		j = 1;
		while (j <= n)
		{
			arr[i][j] = sum_arr(arr[i - 1], j);
			j++;
		}
		i++;
	}
	return (arr[k][n]);
}

int main(void)
{
	int test_case;
	int k;
	int n;

	scanf("%d", &test_case);
	while (test_case)
	{
		scanf("%d\n%d", &k, &n);
		if (test_case != 1)
			printf("%d\n", get_arr(k, n));
		else
			printf("%d", get_arr(k, n));
		test_case--;
	}
	return (0);
}