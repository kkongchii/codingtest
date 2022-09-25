#include<stdio.h>

int main() {
	int i, j, arr[30][30] = { 0 };
	for (i = 0; i < 30; i++)
		for (j = 0; j < 30; j++)
			arr[i][j] = 1;
	
	for (i = 1; i < 30; i++)
		for (j = 1; j < 30; j++)
			arr[i][j] = arr[i-1][j]+arr[i][j-1];

	scanf("%d %d", &i, &j);

	printf("%d", arr[i - j][j - 1]);

	return 0;
}