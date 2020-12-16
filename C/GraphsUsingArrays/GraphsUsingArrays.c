#include <stdio.h>
#include <stdlib.h>


int main()
{

    int n=5;
    int graph[5][5]={{0 , 34 , 0 , 0 , 78},
                    {0 , 0 , 11 , 41 , 3},
                    {0 , 0 , 0 , 57 , 0},
                    {0 , 0 , 0 , 0 , 144},
                    {0 , 0 , 0 , 0 , 0}};

    /*
    int graph[n][n];

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            graph[i][j]=0;
        }
    }
    
    while(1)
    {
        int m,N,weight;
        char ans='q';
        printf("From ...");
        scanf("%d",&m);
        printf("To ...");
        scanf("%d",&N);
        printf("Weight = ");
        scanf("%d",&weight);
        if(m>N)
        graph[N][m]=weight;
        else
        graph[m][N]=weight;
        printf("Want 2 continue? y/n : ");
        scanf("\n%c",&ans);
        if(ans=='n')
        break;
        else if(ans=='y')
        printf("\n");
    } 
    */
    for(int i=0;i<n-1;i++)
    {
        for(int j=i+1;j<n;j++)
        {
            if(graph[i][j]!=0)
            {
                printf("There is a link between %d and %d whose weight is %d.\n",i,j,graph[i][j]);
            }
        }

    }

    return 0;
}
