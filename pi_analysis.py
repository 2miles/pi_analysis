import string

class Consecutive:
    length = 0
    location = 0
    num = '0'

pi_str = ""
with open("pi_100_million.txt") as f:
    pi_str = f.read()

def longest_repetition(pi:string) -> Consecutive:
    result = Consecutive()
    max = 0
    for i in range(len(pi) - 1):
        start = i
        end = i + 1
        if pi[start] == pi[end]:
            count = 1
            while pi[start] == pi[end]:
                count += 1
                end += 1
            if count > max:
                result.num = pi[start]
                result.location = start
                max = count

    result.length = max

    return result

results = longest_repetition(pi_str);

print(f"Length:   {results.length}")
print(f"Location: {results.location}")
print(f"Number:    {results.num}")
print(len(pi_str))
print(longest_repetition(pi_str))
