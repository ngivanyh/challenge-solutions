#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

typedef struct dice {
    int top;
    int bottom;
    int left;
    int right;
    int front;
    int back;

    void forwards()
    {
        // the "current" top in this case will become the previous one
        int prev_top = this->top;

        this->top = this->back;
        this->back = this->bottom;
        this->bottom = this->front;
        this->front  = prev_top;
    }

    void rightwards()
    {
        int prev_top = this->top;

        this->top = this->left;
        this->left = this->bottom;
        this->bottom = this->right;
        this->right = prev_top;
    }
} dice;

int main()
{
    int die_count, changes;
    cin >> die_count >> changes;
	vector<dice> die(die_count);

	for (dice & d : die)
        d = {1, 6, 5, 2, 4, 3};

	for (int i = 0; i < changes; ++i)
    {
        pair<int, int> change;
        cin >> change.first >> change.second;
        pair<int, int> idx = {change.first - 1, change.second - 1};

        if (change.first > 0 && change.second > 0)
            swap(die[idx.first], die[idx.second]);
        else if (change.second == -1)
            die[idx.first].forwards();
        else
            die[idx.first].rightwards();
    }

    for (int i = 0; i < die_count - 1; ++i)
        printf("%d ", die[i].top);
    printf("%d\n", die[die.size() - 1].top);

	return 0;
}