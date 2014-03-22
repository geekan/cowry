#include<stdio.h>
int main(){
	int arr[3]={10,20,30};
	int x=0;
	x = ++arr[++x] + ++x + arr[--x];
	printf("%d ",x);
	return 0;
}
