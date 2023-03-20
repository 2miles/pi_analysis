import string

class Consecutive:
    length = 0
    location = 0
    num = '0'

pi_str = ""
with open("pi_10_million.txt") as f:
    pi_str = f.read()


def count_each_digit(pi: string) -> list['int']:
    counts = [0] * 10
    for i in range(len(pi) - 1):
        count_digit(int(pi[i]), counts)
    return counts
    

def count_digit(digit: int, counts: list['int']): 
    counts[digit] += 1


def longest_repetition(pi:string) -> Consecutive:
    result = Consecutive()
    max = 0
    ## iterate through each digit
    for i in range(len(pi) - 1):
        start = i
        end = i + 1
        # compare the digit with the next and see if they're the same
        if pi[start] == pi[end]:
            count = 1
            # as long as they're the same, compare the digit after that against the original digit
            # keeping a count as you go 
            while pi[start] == pi[end]:
                count += 1
                end += 1
            if count > max:
                result.num = pi[start]
                result.location = start
                max = count
        # skip the string we just counted
        i += max
    result.length = max
    return result


counts = count_each_digit(pi_str)
results = longest_repetition(pi_str)



print("\nDigits of pi calculated: ")
print("---------------------------------------")
print(f"{len(pi_str) - 2}")

print("\nCount of each digit: ")
print("---------------------------------------")
for i in range(10):
    print(f"{i}:        {counts[i]}")
print("\nLongest consecutive repeated digit: ")
print("---------------------------------------")
print(f"Length:   {results.length}")
print(f"Number:   {results.num}")
print(f"Location: {results.location}")
print()

