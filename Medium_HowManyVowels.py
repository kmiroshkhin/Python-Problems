"""
Create a function that takes a string and returns the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5

count_vowels("Palm") ➞ 1

count_vowels("Prediction") ➞ 4
"""
def count_vowels(txt):
    vowel_list=['a','e','i','o','u']
    counter = 0
    for i in txt:
        if i in vowel_list:
            counter +=1
    return counter
