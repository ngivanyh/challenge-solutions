#include <math.h>
#include <vector>
#include <stdio.h>

typedef long long ll;
using namespace std;

#define CREATE_PERFECT_ODD 0
#define GET_NUMBER_CLOSE 1

int main(void)
{
    ll num;
    scanf("%lld", &num);
    // printf("%lld\n", num);
    // generate vector of digits (reversed)
    vector<int> digits;
    for (int i = 10, n = num; n > 0; n /= i)
        digits.push_back(n % i);

    // perfect odd > num
    int task = CREATE_PERFECT_ODD;
    vector<int> gpo = digits;
    ll gpo_number = 0;
    for (int i = gpo.size() - 1; i >= 0; --i)
    {
        // printf("i: %d, digit: %d, gpo: %lld, task: %d\n", i, gpo[i], gpo_number, task);
        if (task == CREATE_PERFECT_ODD)
        {
            if (!(gpo[i] & 1))
            {
                gpo[i] += 1;
                task = GET_NUMBER_CLOSE;
            }
        }
        else
        {
            gpo[i] = 1;
        }

        gpo_number += gpo[i] * (ll) pow(10, i);
    }

    // printf("gpo: %lld %lld\n", gpo_number, num);

    if (gpo_number == num)
    {
        printf("0\n");
        return 0;
    }

    // perfect odd < num
    task = CREATE_PERFECT_ODD;
    vector<int> mpo = digits;
    ll mpo_number = 0;
    for (int i = mpo.size() - 1; i >= 0; --i)
    {
        // printf("i: %d, digit: %d, mpo: %lld, task: %d\n", i, mpo[i], mpo_number, task);

        if (task == CREATE_PERFECT_ODD)
        {
            if (mpo[i] && !(mpo[i] & 1))
            {
                mpo[i] -= 1;
                task = GET_NUMBER_CLOSE;
            }
            else if (!mpo[i])
            {
                mpo[i] = 9;
                mpo[i - 1]--; // FIX: case: 35001 or 35010
                mpo_number -= (ll) pow(10, i + 1);
                task = GET_NUMBER_CLOSE;
            }
        }
        else
        {
            mpo[i] = 9;
        }

        mpo_number += mpo[i] * (ll) pow(10, i);
    }

    // printf("mpo: %lld\n", mpo_number);

    printf("%lld\n", min(abs(gpo_number - num), abs(mpo_number - num)));
    return 0;
}