#include <stdio.h>

int sum_arr(int *arr, int n)
{
	int i;
	int sum;

	i = 1;
	sum = 0;
	while (i < n)
	{
		sum += *arr;
		arr++;
		i++;
	}
	return (sum);
}

int	main(void)
{
	int	test_case;
	int arr[15][14];
	int k;
	int n;
	int i;
	int j;

	scanf("%d", &test_case);
	i = 0;
	j = 1;
	while (j < 15)
	{
		arr[0][j] = j;
		j++;
	}
	i++;
	while (i < 15)
	{
		j = 1;
		while (j < 15)
		{
			arr[i][j] =

	while (test_case--)
	{
		scanf("%d\n%d", &k, &n);
		while (i < 


