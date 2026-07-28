// i suppose it is a big reverser because it's C

#include <stdio.h>

int main(void)
{
    int N;
    scanf("%d", &N);

    int ns[N];
    int i = N;

    while (i--) scanf("%d", ns + i);

    for (i = 0; i < N; i++)
        printf("%d ", ns[i]);
}