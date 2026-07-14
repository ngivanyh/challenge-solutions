#include <iostream>
#include <queue>

using namespace std;

int main(void)
{
    int actions;
    queue<int> q;
    vector<int> fronts;

    cin >> actions;

    int action;
    for (int i = 0; i < actions; ++i)
    {
        cin >> action;

        if (action == 1)
        {
            int to_insert;
            cin >> to_insert;
            q.push(to_insert);
        }
        else if (action == 2)
            fronts.push_back((q.empty()) ? -1 : q.front());
        else
        {
            if (q.empty()) continue;
            q.pop();
        }
    }

    for (int & f : fronts)
        cout << f << '\n';

    return 0;
}