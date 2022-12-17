#include<stdio.h>

#define NUM 64

double total ,current;

int main(void){
  int   i = 1;
total = current = 1.0;

while (i<NUM){
    i = i + 1;
    current = 2.0 * current;
    total = total + current;
    printf("This is %d count ",i);
    getchar();
    printf("There are total is %12.2e\n",total);

}

return 0;
}