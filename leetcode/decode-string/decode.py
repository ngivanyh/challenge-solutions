# Leetcode 394

class Solution:
    def decodeString(self, s: str) -> str:
        def decode(to_decode, i, decoded):
            if i == len(to_decode):
                return decoded

            char = to_decode[i]
            if char.isdigit():
                og_i = i
                while (i := i+1) and to_decode[i].isdigit():
                    pass
                repeats = int(to_decode[og_i : i])
                # print(i)
                i, decoded2 = decode(to_decode, i + 1, [])
                # print(i, decoded2)
                decoded += decoded2 * repeats

                return decode(to_decode, i + 1, decoded)
            elif char == "]":
                return (i, decoded)
            else:
                decoded.append(char)
                return decode(to_decode, i + 1, decoded)

        return "".join(decode(s, 0, []))