#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int exprs;
    scanf("%d", &exprs);

    int *brackets = malloc(sizeof(int) * exprs);
    char expr[20];

    for (int i = 0; i < exprs; ++i)
    {
        scanf("%s", expr);

        int total = 0, parens = 0;
        for (int j = 0; j < 20 && expr[j] != '\0' && total >= 0; ++j)
        {
            if (expr[j] == '(')
            {
                // count the "paren pairs" while we're at it
                total++;
                parens++;
            }
            else if (expr[j] == ')')
                total--;
        }

        brackets[i] = (!total) ? parens : 0;
    }

    for (int i = 0; i < exprs; ++i)
        printf("%d\n", brackets[i]);

    free(brackets);
    return 0;
}