// UVa 514

#include <stack>
#include <iostream>

using namespace std;

bool eval(int n, int * seq);

int main(void)
{
    while (1)
    {
        int n, i;
        cin >> n;
        if (!n) break;
        while (1)
        {
            int seq[n];
            for (i = 0; i < n; ++i)
            {
                cin >> seq[i];
                if (!seq[i]) break;
            }

            if (i != n)
            {
                cout << '\n';
                break;
            }

            cout << (eval(n, seq) ? "Yes" : "No") << '\n';
        }
    }

    return 0;
}

bool eval(int n, int * seq)
{
    stack<int> sequence;

    for (int i = 0, j = 1; i < n; ++i)
    {
        int want = seq[i];
        if (sequence.empty() || sequence.top() != want)
        {
            for (; j <= n; ++j)
            {
                sequence.push(j);
                if (j == want)
                {
                    ++j;
                    break;
                }
            }

            if (sequence.top() != want) return false;
        }

        sequence.pop();
    }

    return true;
}