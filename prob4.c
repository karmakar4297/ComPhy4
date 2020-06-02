#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>
int main()
{
	int N=10000, i;
	float arr[N],num;
	FILE *fp;
	fp=fopen("prob4out.txt","w");
	srand(time(0));
	for(i=0;i<N;i++)
	{
		num=rand()/((float)RAND_MAX+1);
		arr[i]=-(0.5)*log(1-num);
		fprintf(fp,"%.4f\n",arr[i]);
	}
	fclose(fp);
}
