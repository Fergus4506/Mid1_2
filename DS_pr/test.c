#include <stdio.h>
#include <stdlib.h>
#include <malloc.h> // Add this line
static int s[]={1,2,3};
int (*f(int c))[]{
    int sd[]={4,5,6}, (*p)[3],*ap;
    switch (c) {
        case 1 : p=&s; break;
        case 2 : p=&sd; break;
        case 3 : p=malloc(3*sizeof(int)); ap=(*p); ap[0]=7;ap[1]=8;ap[2]=9;
    }
    printf("enter f, %d,\n",(*p)[c-1]);
    return p;
}
int t() {int ta[3]={11,12,13}; return 0;}
void main() {
    int (* (*a[3])(int))[],(*xp)[3];
    a[0]=f; a[1]=f; a[2]=f;
    xp=a[0](1); t(); printf("main %d\n", (*xp)[0]);
    xp=a[1](2); t(); printf("main %d\n", (*xp)[1]);
    xp=a[2](3); t(); printf("main %d\n", (*xp)[2]);
}
