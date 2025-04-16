import unittest



def reverse_string(s):

    return s[::-1]

def is_palindrome(s):

    return s == s[::-1]

def extract_vowels(s):

    vowels = 'авыаываываываыаывапррап'
    return ''.join([char for char in s if char in vowels])

def remove_duplicates(s):

    return ''.join(sorted(set(s), key=s.index))