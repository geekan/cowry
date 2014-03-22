#include<stdio.h>
auto int a=5; // auto cannot be in file scope
int main(){
	int x;
	x=~a+a&a+a<<a;
	printf("%d",x);
	return 0;
}
