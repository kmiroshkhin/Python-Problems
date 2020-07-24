'''
Write a function that finds the longest word in a sentence. If two or more words are found,
return the first longest word. Characters such as apostophe, comma, period (and the like)
count as part of the word (e.g. O'Connor is 8 characters long).
'''


def longest_word(txt):
    split_txt=txt.split();maxchar=""
    for word in split_txt:
        if len(word)>len(maxchar):
            maxchar = word
    return maxchar