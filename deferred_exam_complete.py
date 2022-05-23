# ESC180 Final Examination, Fall 2020, deferred
#
# Aids allowed: the ESC180 website, a Python IDE. You must *not* use any other
# notes or internet website. You may must not communicate about the exam with
# anyone except the course instructor at guerzhoy@cs.toronto.edu
#
# You have 2.5 hours to work on the exam, and 30 minutes to submit it. You may
# keep writing the exam during the submission window, but it is your
# responsibility to make sure that the exam is submitted before the submission
# window closes.
#
# Submit the exam to the course instructor at guerzhoy@cs.toronto.edu
#
# By themselves, comments/docstrings will not earn any points. However, they may
# help in deciding how to award partial credit.
#
# Unless otherwise specified, you may import math and numpy, but not other
# modules.
#

# All questions below have been answered by Ibrahim Hassan on 22 Jan. 2022

# Problem 1 (25 pts)
#    Assume you are given a list of file names of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#    Assume all the text in the files is lower-case.
#
#    For each pair of words, we could compute the number of files in which
#    they co-occur.
#
#    For example, if the input files are ["f1.txt", "f2.txt", "f3.txt"], and
#    "dog" occurs in f1.txt and f3.txt, and "cat" occurs in f1.txt, f2.txt,
#    and f3.txt, we'll say that "cat" and "dog" co-occur in the input
#    files 2 times.
#
#    Write a function that finds the pair of words that co-occur in files
#    most often. Return the pair of words as an alphabetically-sorted list.


def words_cooccur_most_often(files):
    allfiles=list()
    for file in files:
        data = open(file, "r")
        dic = dict()

        for singleline in data:
            singleline = singleline.lower()
            singleline = singleline.strip()

            words = singleline.split(" ")

            for word in words:
                if word in dic:
                    dic[word] = dic[word] + 1
                else:
                    dic[word] = 1

        allfiles.append(dic)
    finalDic=dict()

    for dic in allfiles:
        for key in list(dic.keys()):
            if key in finalDic:
                finalDic[key] = finalDic[key] + 1
            else:
                finalDic[key] = 1

    for key in sorted(finalDic) :
        print(f"{key} co-occurs {finalDic[key]} times.")

# line below to run after changing file names accordingly
# words_cooccur_most_often(['first.txt','second.txt','third.txt'])



###########################################################################
# Problem 2 (20 pts)
#
#  In this problem, you will be writing a function that processes a string
#  of lower-case English characters (and no other characters apart from spaces).
#
#  Words that do not denote digits ("one", "two", "three", "four", "five", "six",
#  "seven", "eight", "nine", and "zero") should be unaltered. Words that
#  denote digits that do not occur next to other words that denote digits
#  should also be unaltered. Sequences of digit words that occur together
#  should be transformed into digits, without separating spaces.
#
# For example,
#   transform_digits("three people took a class in the year two zero two one. and one other.")
# should return
# "three people took a class in the year 2021. and one other."


def transform_digits(s):
    newStr = ""
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words = s.split()

    for word in words:
        f = 0
        if words.index(word)> 0:
            prevIndex=words.index(word) - 1
            nextIndex=words.index(word) + 1
            if word[-1] == '.':
                word = word[0:len(word) - 1]
                f = 1
            if word in digits:
                if words[prevIndex] in digits or words[nextIndex] in digits:
                    newStr+=str(digits.index(word))
                else:
                    newStr += word
                    newStr += " "
            else:
                newStr += word
                newStr += " "
        else:
            nextIndex = words.index(word) + 1
            if word in digits:
                if words[nextIndex] in digits:
                    words += str(digits.index(word))
                else:
                    newStr += word
                    newStr += " "
            else:
                newStr += word
                newStr += " "
        if f == 1:
            newStr += ". "

    print(newStr)

# line below to run after changing text accordingly
# transform_digits("three people took a class in the year two zero two one. and one other.")



############################################################################
#
# Problem 3 (15 pts)
#
# Write a function that returns the deep copy of the input object. The input object
# can be a list or a dictionary, and can itself contain nested list and/or dictionaries
# of integers.
#
# An example of the usage of the function is
#
# obj = [{1:2, 3:[4, {1:2}, []]} , 2]
#
# You may NOT import any modules apart from math and numpy


def deep_copy(obj):
    if isinstance(obj,list):
        objCopy=list()
        for data in obj:
            objCopy.append(data)
    print(f"original object : {obj}")

    objCopy[1]=10
    print(f"copied object with changes : {objCopy}")
    print(f"original object after chnages : {obj}")

# line below to run after changing text accordingly
# deep_copy([{1:2, 3:[4, {1:2}, []]} , 2])



##############################################################################
#
# Problem 4 (10 pts)
#
# What is the tight asymptotic  bound on the runtime complexity of the following function?
# Briefly justify your answer. Assume L is a list of floats.
#
# Include the answer as a comment in the file.


def f(L):
  if len(L) < 2:   #1
    return L[0]   #2

  s = 0   #3
  k = len(L)//3   #4
  for i in range(0, k):   #n
    s += L[i]
  return s + f(L[:k])   #5

# Line referrence marks are at the end of each line if needed
# For this function, f(n) = n + 5
# Tight bound of f(n):
# 0 <= n + 3 <= 4n, for all n >= 1
#Therefore complexity using Big-Oh notation is O(n)



############################################################################
#
# Problem 5 (10 pts)
#
# We can use a dictionary to record who is friends with whom by recording the lists of friends in a dictionary.
#For example:
# friends = {"Carl Gauss": ["Isaac Newton",  "Charles Babbage"],
#            "Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
#            "Ada Lovelace": ["Michael Faraday", "Charles Babbage"],
#            "Isaac Newton": ["Charles Babbage"],
#            "Michael Faraday"" ["Ada Lovelace"] }
# Here, Carl Gauss is friends with Isaac Newton, Gottfried Leibniz, and Charles Babbage. Assume that
# friendships are symmetric, so that if X is friends with Y, then it’s guaranteed that Y is friends with X.
#
# Write a program that finds the pair of people the "friendship path" between whom is the longest. For example,
# the path between Carl Gauss and Michael Faraday is of length 4 (Carl Gauss->Charles Babbage->Ada Lovelace->Michael Faraday),
# and is the longest in friends


# The code below is not complete, but does not show any errors when run
# which is why I did not comment it out
friends = {"Carl Gauss": ["Isaac Newton",  "Charles Babbage"],
"Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
"Ada Lovelace": ["Michael Faraday", "Charles Babbage"],
"Isaac Newton": ["Charles Babbage","Carl Gauss"],
"Michael Faraday": ["Ada Lovelace"] }

def find_longPath(friends):
    allFriends=list(friends.keys())
    pathFriends=dict()
    i=0
    for friend in allFriends:
        j=i
        while j < len(allFriends)-1:

            if allFriends[j+1] in friends[friend]:
                pathFriends[friend+" to "+ allFriends[j+1]]=1
            else:
                for secondF in friends[friend]:
                    if allFriends[j+1] in friends[secondF]:
                        pathFriends[friend+" to "+ allFriends[j+1]]=2
            j=j+1
        i=i+1


    print(pathFriends)

# line below to run
# find_longPath(friends)

