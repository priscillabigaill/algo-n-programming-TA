#include <stdio.h>

int max_of_four(int a, int b, int c, int d){

    if (a >= b && a >= c && a >= d){
        return a;
    } else if (b >= a && b >= c && b >= d){
        return b;
    } else if (c >= a && c >= b && c >= d){
        return c;
    } else if (d >= a && d >= b && d >= c){
        return d;
    } else {
        return -100; // default
    }

}

int main(void){

    int a = 2;
    int b = 4;
    int c = 3;
    int d = 2;

    printf("%d\n",max_of_four(a,b,c,d));

    return 0;
}
