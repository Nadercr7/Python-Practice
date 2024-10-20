def str_min(s1, s2):
    # Returns the lexicographically smaller string
    return s1 if s1 < s2 else s2


def str_max(s1, s2):
    # Returns the lexicographically larger string
    return s1 if s1 > s2 else s2


def str_length(s):
    # Returns the length of the string
    return len(s)

def str_concat(s1, s2):
    # Returns the concatenation of two strings
    return s1 + s2 


def str_repeat(s, n):
    # Returns the string repeated n times
    return s * n 


def str_upper(s):
    # Returns the string in uppercase
    return s.upper() 


def str_lower(s):
    # Returns the string in lowercase
    return s.lower() 


def str_strip(s):
    # Returns the string with leading and trailing whitespace removed
    return s.strip()  


def str_find(s, substring):
    # Returns the index of the first occurrence of substring in s, or -1 if not found
    return s.find(substring) 


def str_replace(s, old, new):
    # Returns a new string with all occurrences of old replaced by new
    return s.replace(old, new) 



"""
Explanation of Built-in String Methods Used:

    <, >: Comparison operators to determine lexicographic order.
    
    len(s): Returns the number of characters in the string s.
    
    s1 + s2: Concatenates two strings s1 and s2.
    
    s * n: Repeats the string s n times.
    
    s.upper(): Converts all characters in s to uppercase.
    
    s.lower(): Converts all characters in s to lowercase.
    
    s.strip(): Removes leading and trailing whitespace from the string s.
    
    s.find(substring): Returns the lowest index of the substring if found in s, else returns -1.
    
    s.replace(old, new): Replaces all occurrences of old with new in the string s.
    """
