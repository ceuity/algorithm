#include <stdio.h>
#include <stdlib.h>

int	main(void)
{
	int		result;
	int		i;
	char	str[16];

	scanf("%s", str);

	result = 0;
	i = 0;
	while(str[i])
	{
		if(str[i] == 'A' || str[i] == 'B' || str[i] == 'C')
			result += 3;
		else if (str[i] == 'D' || str[i] == 'E' || str[i] == 'F')
			result += 4;
		else if (str[i] == 'G' || str[i] == 'H' || str[i] == 'I')
			result += 5;
		else if (str[i] == 'J' || str[i] == 'K' || str[i] == 'L')
			result += 6;
		else if (str[i] == 'M' || str[i] == 'N' || str[i] == 'O')
			result += 7;
		else if (str[i] == 'P' || str[i] == 'Q' || str[i] == 'R' || str[i] == 'S')
			result += 8;
		else if (str[i] == 'T' || str[i] == 'U' || str[i] == 'V')
			result += 9;
		else if (str[i] == 'W' || str[i] == 'X' || str[i] == 'Y' || str[i] == 'Z')
			result += 10;
		i++;
	}
	printf("%d", result);
}
