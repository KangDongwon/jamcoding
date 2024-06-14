#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int dupl(int a[], int n)
{
    int i;
    for(i=0; i<6; i++)
    {
        if(a[i] == n)
            return 1;
    }

    return 0;
}

void sort(int a[])
{
    int i, j, temp;

    for (i = 0; i < 6; i++)
    {
        for (j = i+1; j < 6; j++)
        {
            if (a[j] < a[i])
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
     }
}

int main()
{
    srand(time(NULL));

    int n, i=0;

    int arr[7]= {0,};

    while(i<7)
    {
        n = rand() % 45 + 1;
        if(dupl(arr, n) != 1)
        {
            arr[i] = n;
            i++;
        }
    }

    sort(arr);

    for(i=0; i<7; i++)
    {
        if(i==6)
            printf("bonus %d", arr[i]);
        else
            printf("%d ", arr[i]);
    }


    return 0;
}
