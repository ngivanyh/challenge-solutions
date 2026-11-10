def mv(word, chars):
    if not chars: return word

    wl = len(word)
    if chars > 0:
        return word[wl - chars % wl:wl] + word[:wl - chars % wl]
    else:
        return word[-chars % wl:wl] + word[:-chars % wl]


words, length, rearrangements = map(int, input().split())

word_list = [input() for _ in range(words)]

score = 0
for _ in range(rearrangements):
    rearrangement = list(map(int, input().split()))
    word_list = [mv(w, r) for w, r in zip(word_list, rearrangement)]

    for l in range(length):
        letters = {}
        for w in word_list:
            if w[l] not in letters:
                letters[w[l]] = 1
            else:
                letters[w[l]] += 1
        score += max(letters.values())

print(score)