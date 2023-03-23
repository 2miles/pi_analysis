from config import *

class Consecutive:
    """
    Used to package up related data pertaining to a string of repeating decimals within a string of decimals
    """

    length: int = 0
    location: int = 0
    num : str = '0'

    def __init__(self, length, location, num):
        self.length = length
        self.location = location
        self.num = num

def main():
    digits = ""
    with open(DIGIT_FILE) as f:
        digits = f.read(NUM_DIGITS)
    counts = count_each_digits_occurrences(digits)
    results = get_repeated_decimals_list(digits, REPEATED)
    display_results(counts, results)


def count_each_digits_occurrences(digits: str) -> list[int]:
    counts = [0] * 10
    for i in range(NUM_DIGITS):
        counts[int(digits[i])] += 1
    return counts

def get_repeated_decimals_list(digits:str, min:int) -> list['Consecutive']:
    """

    """
    results = []
    i = 0
    while i < NUM_DIGITS - 1:
        if digits[i] == digits[i + 1]:
            result = count_repeated(digits, i, min)
            if result != None:
                results.append(result)
                i += min
                continue    
        i += 1
    return results

def count_repeated(digits:str, loc:int, min:int) -> list[Consecutive] | None:
    """
    Starting at `loc` index of `digits`, if the first `min` or more digits are repeated
    return the location, number, and digit that was repeated, otherwise return None.
    """

    count = 1
    end = loc + 1
    while digits[loc] == digits[end]:
        count += 1
        end += 1
    if count >= min:
        return Consecutive(length=count, location=loc, num=digits[loc])
    return None

def display_results(counts:list[int], results: list['Consecutive'] ) -> None:
    print(f"\nDigits of pi calculated: {NUM_DIGITS}")
    print("---------------------------------------")
    if VERBOSE:
        print("\nNumber of times each digit appears: ")
        print("---------------------------------------")
        for i in range(10):
            print(f"{i}:        {counts[i]}")
        print (f"\nInstances of {REPEATED} or more repeated digits: {len(results)}")
        print("---------------------------------------")
        for result in results:
            print(f"Digit: '{result.num}',  Length: {result.length},  Location: {result.location}")
        print()

if __name__ == "__main__":
    main()