#include<stdio.h> 
#include<conio.h> 
#include<string.h> 
void main() {     
    int p, r, t, result, i,j;     
    clrscr();      
    printf("Enter Principal amount:");     
    scanf("%d",&p);     
    printf("Enter Rate of Interest:");     
    scanf("%d",&r);     
    printf("Enter Total time(in months):");     
    scanf("%d",&t);          
    asm mov ax,p;     
    asm mov bx,r;     
    asm mul bx;     
    asm mul t;     
    asm mov result,ax; 
    printf("Simple Interest:%d\n",result/100);     
    getch(); 
} 