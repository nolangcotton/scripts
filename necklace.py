#!/usr/local/bin/python3

'''

Imagine a necklace with lettered beads that can slide along the string. 
In this example, you could take the N off NICOLE and slide it around to the other end to make ICOLEN. 
Do it again to get COLENI, and so on. 
For the purpose of today's challenge, we'll say that the strings "nicole", "icolen", and "coleni" describe the same necklace.

Generally, two strings describe the same necklace if you can remove some number of letters from the beginning of one, 
attach them to the end in their original ordering, and get the other string. 
Reordering the letters in some other way does not, in general, produce a string that describes the same necklace.

Write a function that returns whether two strings describe the same necklace.

same_necklace("nicole", "icolen") => true
same_necklace("nicole", "lenico") => true
same_necklace("nicole", "coneli") => false
same_necklace("aabaaaaabaab", "aabaabaabaaa") => true
same_necklace("abc", "cba") => false
same_necklace("xxyyy", "xxxyy") => false
same_necklace("xyxxz", "xxyxz") => false
same_necklace("x", "x") => true
same_necklace("x", "xx") => false
same_necklace("x", "") => false
same_necklace("", "") => true

Optional Bonus 1:

If you have a string of N letters and you move each letter one at a time from the start to the end, 
you'll eventually get back to the string you started with, after N steps. 
Sometimes, you'll see the same string you started with before N steps. 
For instance, if you start with "abcabcabc", 
you'll see the same string ("abcabcabc") 3 times over the course of moving a letter 9 times.

Write a function that returns the number of times you encounter the same 
starting string if you move each letter in the string from the start to the end, one at a time.

repeats("abc") => 1
repeats("abcabcabc") => 3
repeats("abcabcabcx") => 1
repeats("aaaaaa") => 6
repeats("a") => 1
repeats("") => 1

'''

def same_necklace(n1, n2):
    if n1 == n2:
        return True
    for i in range(len(n1)):
        tmp_str=n1[i:] + n1[:i]
        if n2 == tmp_str:
            return True
    return False

def repeats(n1):
    repeat_count=0
    if n1 == "":
        repeat_count += 1
    for i in range(len(n1)):
        tmp_str=n1[i:] + n1[:i]
        if tmp_str == n1:
            repeat_count += 1
    return repeat_count