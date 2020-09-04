#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
int main(){ 
	int count = 0;
	srand(time(NULL));
ans:
	string yn;
	cout << "추첨을 하시겠습니까?(y,n)";
	getline(cin, yn);
	if (yn == "y"){
		goto start;
	}
	return 0;
	start:
		srand(time(NULL));
		count = 0;
		printf("추첨시작\n");
		while(count < 7)
		{
			int r = rand() % 40 + 1;
			printf("%d번:%d\n", count + 1, r); 
			r = 0;
			count = count + 1;
		}
		goto ans;
}
