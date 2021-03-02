#include<stdio.h>
#define NUM1 1
#define NUM2 1
void fibonacci(int index);
int main(void)
{
    int n;

    printf("enter index: \n");
    scanf("%d",&n);
    printf("1 1 ");
    fibonacci(n);

    return 0;
}

void fibonacci(int index)
{
    int ans;
    int ans_before1 = 1;
    int ans_before2 = 1;

    if (index > 0 && index <= 2)
        ans = 1;
    else
    {
        for (int i=0;i<index;i++)
        {
            ans = ans_before1+ans_before2;
            ans_before2 = ans_before1;
            ans_before1 = ans;

            printf("%d ",ans);
        }
    }

    return 0;
}
