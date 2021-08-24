from collections import Counter

def isPalindrome(s):
    return len([1 for c in Counter(s).values() if c % 2]) <= 1


print(isPalindrome("abb"))