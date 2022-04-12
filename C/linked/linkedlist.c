#include<stdio.h>
#include<stdlib.h>
/*
struct node
{
    int data;
    struct node* next;
};



int main()
{
    struct node* first = (struct node*)malloc(sizeof(struct node)); 
    first->data = 10;
    first->next = NULL;
    printf("%d",first->data);
    return 0;
}*/

int main()
{
    int a=5;
    int* b;
    
    b = &a;
    
    printf("%d",*b);

    return 0;
}