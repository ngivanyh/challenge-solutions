"""
you get a string and get where the string needs to go to

there may be multiple permutations of the string,
you must use the result of the last one to generate the new one

there is also a special output requirement, it should be pretty self-explanatory
"""

_, remixes, special_prints = map(int, input().split())

string = input()
remixed_strings = []

for _ in range(remixes):
    remix = sorted((int(pos), char) for pos, char in zip(input().split(), string))
    remixed_strings.append("".join(c[1] for c in remix))
    string = remixed_strings[-1]

for i in range(special_prints):
    print("".join(s[i] for s in remixed_strings))