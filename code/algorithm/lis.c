#include<stdio.h>


int a[100000] = {0};
int b[100000] = {0};
int max_count = 0;
int n = 0;

int max(int a, int b)
{
	return a > b ? a : b;
}

int lis(int k)
{
	int i = 0;
	int ret = 0;
	int mc = 0;
	for(i = k; i < n; i++)
	{
		if(a[i] > a[k])
		{
			ret = lis(i);
			mc = max(mc, ret);
		}
	}

	return mc + 1;
}

int main()
{
	int max_len = 0;
	while(scanf("%d", &n) != EOF)
	{
		int i = 0;
		for (i = 0; i < n; i++)
			scanf("%d", &a[i]);
		
		//max_len = lis(0);
		for (i = 0; i < n; i++)
		{
			printf("%d\n", lis(i));
		}

		printf("%d\n", max_len);
	}
	return 0;
}