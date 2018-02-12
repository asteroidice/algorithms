# Name: Ryan Rabello
# Chapter 6.1 Problem 11

# Problem Statement: Anagram detection
#    a. Design an efficient algorithm for finding all sets of anagrams in a
#       large file such as a dictionary of English words.
#    b. Write a program implementing the algorithm.

# The name of the file with all the English words.
filename = "./words_alpha.txt"

# Import all english words as a list of strings.
raw_words = open(filename).read().splitlines()

# A custom class that stores both the actual word "apple" and the sorted word
# "aelpp". The letters in sorted word are aranged alphabetically.
class Word():
    word = ""
    sorted_word = ""

    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def __repr__(self):
        # return self.word + "->" + self.sorted_word
        return self.word

# Convert all the strings to Word() objects and add them to words[] O(n)
words = []
for word in raw_words:
    words.append(Word(word))

# Sort words by "sorted word". O(n log n)
sorted_words = sorted(words, key=lambda x: x.sorted_word)

# Go through every word, check it against it's neighbor and (if it is also an
# anagram) add it to a list of words that are anagrams. Then add that list of
# anagrams (current_anagrams[]) to anagrams[].  O(n)
anagrams = []
i = 0
while i < len(sorted_words):
    current_anagrams = []
    while i + 1 < len(sorted_words) and \
            sorted_words[i].sorted_word == sorted_words[i + 1].sorted_word:
        current_anagrams.append(sorted_words[i])
        i += 1
    if len(current_anagrams) > 0:
        current_anagrams.append(sorted_words[i])
        anagrams.append(current_anagrams)
    i += 1

print("The first 20 sets of anagrams")
print(anagrams[0:20])

# This is a O(n + n + n log n) => O(n log n) algorithm becuase of the
# presorting. One could also develop a O(n) algorithm using hash tables.
