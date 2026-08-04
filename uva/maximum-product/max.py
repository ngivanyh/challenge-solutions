# UVa 11059

"""
to simulate the UVa input of EOF, create a file and put in your input
then use redirection: python max.py < a.txt
"""

def main():
    try:
        i = 1
        while (_ := int(input())):
            seq = list(map(int, input().split()))
            product = 0 if (p := find(seq)) and p < 0 else p
            print(f"Case #{i}: The maximum product is {product}.\n")
            i += 1
    except EOFError:
        pass

def find(seq):
    SEQ_LEN_PLUS = len(seq) + 1
    products = []
    for l in range(1, SEQ_LEN_PLUS):
        for i in range(SEQ_LEN_PLUS - l):
            product = 1
            for j in range(i, i+l):
                product *= seq[j]
            products.append(product)

    return max(products)

if __name__ == "__main__":
    main()