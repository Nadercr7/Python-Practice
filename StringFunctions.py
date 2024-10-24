def str_min(s1, s2):
    # Returns the lexicographically smaller string
    return s1 if s1 < s2 else s2


def str_max(s1, s2):
    # Returns the lexicographically larger string
    return s1 if s1 > s2 else s2


def str_length(s):
    # Returns the length of the string
    length = 0
    for _ in s:
        length += 1
    return length

- The underscore `_` is used as a variable, but in Python, it conventionally indicates that the loop variable is not going to be used inside the loop. 
"""It's a way of saying "I don't care about the value of this variable."""


def str_concat(s1, s2):
    # Returns the concatenation of two strings
    result = ''
    for c in s1:
        result += c
    for c in s2:
        result += c
    return result


def str_repeat(s, n):
    # Returns the string repeated n times
    result = ''
    for _ in range(n):
        result += s
    return result


def str_upper(s):
    # Returns the string in uppercase
    result = ''
    for c in s:
        # Check if character is lowercase a-z and convert to uppercase A-Z
        if 'a' <= c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    return result

"""ord(c):
    The ord() function takes a character (in this case, c) and returns its Unicode code point (an integer). For example, ord('A') returns 65, and ord('a') returns 97."""


def str_lower(s):
    # Returns the string in lowercase
    result = ''
    for c in s:
        # Check if character is uppercase A-Z and convert to lowercase a-z
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c
    return result



def str_find(s, substring):
    # Returns the index of the first occurrence of substring in s, or -1 if not found
    n, m = len(s), len(substring)
    for i in range(n - m + 1):
        if s[i:i + m] == substring:
            return i
    return -1




"""
Explanation of Built-in String Methods Used:

    <, >: Comparison operators to determine lexicographic order.
    
    len(s): Returns the number of characters in the string s.
    
    s1 + s2: Concatenates two strings s1 and s2.
    
    s * n: Repeats the string s n times.
    
    s.upper(): Converts all characters in s to uppercase.
    
    s.lower(): Converts all characters in s to lowercase.
        
    s.find(substring): Returns the lowest index of the substring if found in s, else returns -1.
    
    """
