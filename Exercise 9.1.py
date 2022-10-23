# 9.1  Exercises

# Download file "words.txt" here:  https://www.geeksforgeeks.org/python-program-to-read-file-word-by-word/
# Exercise 9.1   Write a program that reads words.txt and prints only the words with more than 20 characters
# (not counting whitespace).
import re
import string

# first import the module
import webbrowser

# then make a url variable
url = "https://www.geeksforgeeks.org"

# then call the default open method described above
webbrowser.open(url)

# Quick Two Line Codes
countOfWords = len("Geeksforgeeks is best Computer Science Portal".split())
print("Count of Words in the given Sentence:", countOfWords)

# Quick One Line Codes
print(len("Geeksforgeeks is best Computer Science Portal".split()))

# Quick One Line Code with User Input
print(len(input("Enter Input:").split()))

def characterCount():
    fin = open ('GFG.txt','r')
    for line in fin:
        words = line.strip()
        if len(words) > 19:
            print(words)


# Python program to read
# file word by word

    for line in file:

        # reading each word
        for word in line.split():
            # displaying the words
            print(word)
