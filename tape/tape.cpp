#include <set>
#include <deque>
#include <stdio.h>

using namespace std;
typedef long long ll;
ll max_occurences[26];

bool check_prettyness(deque<char> tape);

int main(void)
{
    ll tape_length;
    scanf("%lld", &tape_length);

    for (ll & max_occurence : max_occurences)
        scanf("%lld", &max_occurence);

    char tape[tape_length + 1];
    scanf("%s", tape);

    ll result = 0;
    deque<char> pretty_tape;
    for (ll i = 0; i < tape_length - 2; ++i)
    {
        ll j = i + 1;
        while (!check_prettyness(pretty_tape))
        {
            pretty_tape.push_back(j);
        }
    }

    printf("%d", result);

    return 0;
}

bool check_prettyness(deque<char> tape)
{
    if (tape.size() < 3)
        return false;

    ll invalid_occurences = 0;
    set<char> included_chars;

    for (char c : tape)
    {

    }
}