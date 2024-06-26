'''Eva has a string S containing lowercase English letters. She wants to transform this 
string into a Magic String, where all the characters in the string are the same. To do 
so, she can replace any letter in the string with another letter present in that string. 6
Your task is to help Eva find and return an integer value, representing the minimum 
number of steps required to form a Magic String. Return 0, if S is already a Magic 
String.
Input Specification:
input1: A string S, containing lowercase English letters.
Output Specification:
Return an integer value, representing the minimum number of steps required to form 
a Magic String. Return 0, if S is already a Magic String.
Sample Input:
aaabbbccdddd
Sample Output:
8'''
#collections has many fucn and counter is one of it
from collections import Counter

def min_magicstring(s):
    frequency=Counter(s)
    max_freq=max(frequency.values())
    min_steps=len(s)-max_freq
    return min_steps
s='aaabbbcccdddd'
print(min_magicstring(s))