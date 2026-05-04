plates = int(input())

for _ in range(plates):
    letters, numbers = input().split("-")
    numbers = int(numbers)
    letters = [(ord(l) - 65) * 26 ** (len(letters) - 1 - i) for i, l in enumerate(letters)]
    print("nice" if abs(numbers - sum(letters)) <= 100 else "not nice")