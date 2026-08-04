// UVa 11342

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_MAX 50000

int results[NUM_MAX][3] = {-1};

int main(void)
{
    for (int i = 0; i < NUM_MAX; ++i)
        for (int j = 0; j < 3; ++j)
            results[i][j] = -1;

    const int max_root = (int) round(sqrt(NUM_MAX));
    for (int i = 0; i <= max_root; ++i)
        for (int j = 0; j <= max_root; ++j)
            for (int k = 0; k <= max_root && i*i + j*j + k*k <= NUM_MAX; ++k)
            {
                int three_squared = i*i + j*j + k*k;
                if (results[three_squared - 1][0] == -1)
                {
                    results[three_squared - 1][0] = i;
                    results[three_squared - 1][1] = j;
                    results[three_squared - 1][2] = k;
                }
            }

    int N;
    scanf("%d", &N);
    while (N--)
    {
        int n;
        scanf("%d", &n);

        if (results[n - 1][0] == -1)
        {
            printf("-1\n");
            continue;
        }

        printf("%d %d %d\n",
            results[n - 1][0],
            results[n - 1][1],
            results[n - 1][2]
        );
    }

    return 0;
}