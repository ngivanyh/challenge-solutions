// UVa 514

#include <stack>
#include <iostream>

using namespace std;

int get_block();
bool eval(int n, int * seq);

int main(void)
{
    while (get_block())
        ;

    return 0;
}

int get_block()
{
    int n;
    cin >> n;
    if (!n) return 0;
    while (true)
    {
        int seq[n];
        for (int & s : seq)
        {
            cin >> s;
            if (!s)
            {
                cout << '\n';
                return n;
            }
        }

        cout << ((eval(n, seq)) ? "Yes" : "No") << '\n';
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

            if (sequence.top() != want)
                return false;
            sequence.pop();
        }
        else if (sequence.top() == want)
            sequence.pop();
    }

    return true;
}